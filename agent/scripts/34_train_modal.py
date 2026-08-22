"""Run the analyzer fine-tune (scripts/33_train_analyzer.py) on a rented GPU
via Modal, and bring the results home.

One-time setup (human): `.venv/bin/modal token new` (browser login).
Then:
  .venv/bin/modal run scripts/34_train_modal.py --run-name analyzer-v1 \
      --gpu A10G --epochs 3
  .venv/bin/modal run scripts/34_train_modal.py --run-name analyzer-v1 --fetch

What happens:
  * the container gets the SAME layout as this repo (/root/agent/scripts,
    /root/agent/data/training, /root/agent/data/benchmark) so 33_* runs
    unmodified; trainset + benchmark are shipped with the image
  * outputs (model weights, results_<run>.jsonl, leaderboard row, log) go to a
    persistent Modal Volume `shastrartha-models` under /vol/<run-name>/
  * `--fetch` copies the benchmark results + leaderboard row back into
    agent/data/benchmark/ (weights stay on the volume; pull with
    `modal volume get shastrartha-models <run-name> agent/models/` if needed)

Cost guard: timeout 5 h. A100 (default; MODAL_GPU overrides) ≈ $2.5/h; with bf16
the 3-epoch run is ~1 h → a few dollars. (Run 1 on A10G in fp32 hit the 5 h
timeout with buffered logs — hence bf16, checkpoints, and streaming now.)
"""

import os
import subprocess
import sys
from pathlib import Path

import modal

AGENT = Path(__file__).resolve().parents[1]
REMOTE = Path("/root/agent")

app = modal.App("shastrartha-analyzer")
vol = modal.Volume.from_name("shastrartha-models", create_if_missing=True)

image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("torch", "transformers>=4.44", "datasets", "accelerate>=1.1.0",
                 "sentencepiece", "protobuf")
    .add_local_file(AGENT / "scripts" / "33_train_analyzer.py",
                    str(REMOTE / "scripts" / "33_train_analyzer.py"))
    .add_local_file(AGENT / "data" / "training" / "trainset_v1.jsonl",
                    str(REMOTE / "data" / "training" / "trainset_v1.jsonl"))
    .add_local_file(AGENT / "data" / "benchmark" / "analyzer_benchmark_v1.jsonl",
                    str(REMOTE / "data" / "benchmark" / "analyzer_benchmark_v1.jsonl"))
)


@app.function(image=image, gpu=os.environ.get("MODAL_GPU", "A100"), timeout=5 * 60 * 60,
              volumes={"/vol": vol})
def train(run_name: str, base: str, epochs: float, lr: float, bs: int,
          max_len: int, max_steps: int) -> dict:
    out_dir = Path("/vol") / run_name
    out_dir.mkdir(parents=True, exist_ok=True)
    (REMOTE / "data" / "benchmark").mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(REMOTE / "scripts" / "33_train_analyzer.py"),
           "--base", base, "--out", str(out_dir / "model"),
           "--epochs", str(epochs), "--lr", str(lr), "--bs", str(bs),
           "--max-len", str(max_len), "--max-steps", str(max_steps)]
    # stream the trainer's output (Modal relays stdout live) AND keep it on the volume
    lines = []
    with (out_dir / "train.log").open("w") as lf:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, bufsize=1, env={**os.environ, "RUN_TAG": run_name})
        for line in proc.stdout:
            print(line, end="", flush=True)
            lf.write(line); lf.flush()
            lines.append(line)
            if len(lines) % 200 == 0:
                vol.commit()
        proc.wait()

    class _Log:  # keep the downstream code unchanged
        returncode = proc.returncode
        stdout = "".join(lines)
        stderr = ""
    log = _Log()
    bench = REMOTE / "data" / "benchmark"
    results = {}
    for p in bench.glob("results_*.jsonl"):
        results[p.name] = p.read_text()
        (out_dir / p.name).write_text(results[p.name])
    lb = bench / "leaderboard.md"
    row = lb.read_text().strip().splitlines()[-1] if lb.exists() else ""
    (out_dir / "leaderboard_row.md").write_text(row + "\n")
    vol.commit()
    return {"returncode": log.returncode, "leaderboard_row": row,
            "results_files": list(results), **results,   # contents too → written locally
            "tail": log.stdout[-3000:], "stderr_tail": log.stderr[-2000:]}


@app.function(image=image, volumes={"/vol": vol})
def fetch(run_name: str) -> dict:
    d = Path("/vol") / run_name
    if not d.exists():
        return {"error": f"no run {run_name!r} on volume"}
    out = {"leaderboard_row": (d / "leaderboard_row.md").read_text()
           if (d / "leaderboard_row.md").exists() else ""}
    for p in d.glob("results_*.jsonl"):
        out[p.name] = p.read_text()
    out["train_log_tail"] = (d / "train.log").read_text()[-4000:] \
        if (d / "train.log").exists() else ""
    return out


@app.local_entrypoint()
def main(run_name: str = "analyzer-v1", base: str = "chronbmm/sanskrit5-multitask",
         epochs: float = 3.0, lr: float = 3e-4, bs: int = 16, max_len: int = 512,
         max_steps: int = -1, fetch_only: bool = False):
    bench = AGENT / "data" / "benchmark"
    if fetch_only:
        r = fetch.remote(run_name)
    else:
        print(f"launching {run_name}: base={base} epochs={epochs} lr={lr} bs={bs}")
        r = train.remote(run_name, base, epochs, lr, bs, max_len, max_steps)
        print(r.get("tail", "")[-1500:])
        if r.get("returncode"):
            print("TRAINING FAILED — stderr tail:\n", r.get("stderr_tail"))
    if "error" in r:
        print(r["error"]); return
    for name, text in r.items():
        if name.startswith("results_") and name.endswith(".jsonl"):
            (bench / name).write_text(text); print(f"wrote {bench / name}")
    row = (r.get("leaderboard_row") or "").strip()
    if row:
        lb = bench / "leaderboard.md"
        if row not in lb.read_text():
            with lb.open("a") as f:
                f.write(row + "\n")
        print("leaderboard:", row)
    if r.get("train_log_tail"):
        print(r["train_log_tail"][-1500:])
