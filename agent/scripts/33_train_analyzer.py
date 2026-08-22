"""Analyzer fine-tuning skeleton (Phase 3) — SFT of a seq2seq model on
trainset_v1, evaluated on the frozen benchmark with exact-feature scoring.

NOT RUN AT SCALE YET. `--smoke` proves the plumbing (tiny subset, few steps,
MPS/CPU) so a real run is a flag flip once the eval gate says go.

Task format (own, not ByT5's undocumented tags):
  input : "A <surface> ‖ <sentence or surface>"
  target: "pos=tinanta root=gam prayoga=Kartari lakara=Lun purusha=Prathama vacana=Eka"
A byte-level base (ByT5) reads IAST natively — the reason it's the default
candidate (see data/benchmark/base_model_memo.md).

Stages:
  1. build   — trainset_v1.jsonl → HF datasets (input/target text), weights
  2. train   — Seq2SeqTrainer, weighted sampling by record weight
  3. eval    — decode benchmark, parse targets, score fields+lemma exactly,
               write results_<tag>.jsonl + a report row comparable to
               baseline_report.md
Later (RL phase): replace 2's loss with rejection sampling / GRPO where the
reward is vidyut's verify_*_claim pass/fail — the "Pāṇini as reward" loop.

Usage:
  .venv/bin/python scripts/33_train_analyzer.py --smoke
  .venv/bin/python scripts/33_train_analyzer.py --base chronbmm/sanskrit5-multitask \
      --epochs 3 --out models/vyakarani-v1
"""

import argparse
import json
import os
import random
import sys
from collections import Counter
from pathlib import Path

AGENT = Path(__file__).resolve().parents[1]
TRAIN = AGENT / "data" / "training"
BENCH = AGENT / "data" / "benchmark"

FIELD_ORDER = ["pos", "stem", "linga", "vibhakti", "vacana",
               "root", "prefixes", "prayoga", "lakara", "purusha", "lemma"]
SUB_FIELDS = ("vibhakti", "vacana", "linga")
TIN_FIELDS = ("lakara", "purusha", "vacana")


def to_target(claim: dict) -> str:
    parts = []
    for f in FIELD_ORDER:
        v = claim.get(f)
        if v is None:
            continue
        if isinstance(v, list):
            v = "+".join(v) if v else "-"
        parts.append(f"{f}={v}")
    return " ".join(parts)


def parse_target(s: str) -> dict:
    out = {}
    for tok in s.split():
        if "=" in tok:
            k, v = tok.split("=", 1)
            out[k] = v.split("+") if k == "prefixes" else v
    if out.get("prefixes") == ["-"]:
        out["prefixes"] = []
    return out


def to_input(sentence: str | None, surface: str) -> str:
    # surface FIRST: byte-level inputs get truncated at max_len and the
    # target word must never be what falls off the end
    return f"A {surface} ‖ {sentence or surface}"


def load_trainset(limit=None, seed=0, name="trainset_v1.jsonl"):
    rows = [json.loads(l) for l in (TRAIN / name).open(encoding="utf-8")]
    # v2 sets carry per-record repeat counts (context examples oversampled)
    rows = [r for r in rows for _ in range(int(r.get("repeat", 1)))]
    if limit:
        random.Random(seed).shuffle(rows)
        rows = rows[:limit]
    return rows


def build_examples(rows):
    return [{"input": to_input(r["sentence"], r["surface"]),
             "target": to_target(r["claim"]), "weight": r["weight"]} for r in rows]


def score_predictions(items, preds, tag):
    agg, per = Counter(), {}
    rows = []
    for it, pred_s in zip(items, preds):
        gold, pred = it["gold"], parse_target(pred_s)
        fields = TIN_FIELDS if gold["pos"] == "tinanta" else SUB_FIELDS
        if gold["pos"] == "tinanta":
            glem = "".join(gold.get("prefixes") or []) + (gold.get("root") or "")
            plem = "".join(pred.get("prefixes") or []) + (pred.get("root") or "")
        else:
            glem, plem = gold.get("stem") or gold.get("lemma"), pred.get("stem") or pred.get("lemma")
        ok = {f: pred.get(f) == gold.get(f) for f in fields}
        full = all(ok.values()) and pred.get("pos") == gold["pos"]
        lemma_ok = (plem or "").lower() == (glem or "").lower()
        agg["n"] += 1; agg["full"] += full; agg["lemma"] += lemma_ok
        agg["claim"] += (full and lemma_ok)
        for f, v in ok.items():
            agg[f] += v
        rows.append({"id": it["id"], "pred": pred, "fields_ok": ok,
                     "lemma_ok": lemma_ok, "full_ok": full})
    with (BENCH / f"results_{tag}.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n = agg["n"]
    line = (f"| {tag} | {n} | {100*agg['full']/n:.1f}% | {100*agg['lemma']/n:.1f}% "
            f"| {100*agg['claim']/n:.1f}% |")
    with (BENCH / "leaderboard.md").open("a", encoding="utf-8") as f:
        f.write(line + "\n")
    print("leaderboard:", line)
    return agg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="chronbmm/sanskrit5-multitask")
    ap.add_argument("--out", default=str(AGENT / "models" / "analyzer-smoke"))
    ap.add_argument("--epochs", type=float, default=1.0)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--bs", type=int, default=8)
    ap.add_argument("--smoke", action="store_true",
                    help="200 examples, 20 steps, eval on 40 benchmark items")
    ap.add_argument("--max-steps", type=int, default=-1)
    ap.add_argument("--trainset", default="trainset_v1.jsonl")
    ap.add_argument("--eval-only", action="store_true",
                    help="skip training; --base is a checkpoint dir to evaluate")
    ap.add_argument("--max-len", type=int, default=512,
                    help="input byte length cap (smoke uses 256)")
    args = ap.parse_args()
    if args.smoke:
        args.bs, args.max_len = 2, min(args.max_len, 256)

    import torch
    from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer,
                              DataCollatorForSeq2Seq, Seq2SeqTrainer,
                              Seq2SeqTrainingArguments)
    from datasets import Dataset

    rows = load_trainset(limit=200 if args.smoke else None, name=args.trainset)
    ex = build_examples(rows)
    print(f"examples: {len(ex)}  (e.g. {ex[0]['input'][:60]!r} → {ex[0]['target']!r})")

    # Trainer checkpoints carry weights only; the byte tokenizer comes from the
    # original base model in eval-only mode
    tok = AutoTokenizer.from_pretrained(
        "chronbmm/sanskrit5-multitask" if args.eval_only else args.base)
    model = AutoModelForSeq2SeqLM.from_pretrained(args.base)

    def enc(batch):
        m = tok(batch["input"], max_length=args.max_len, truncation=True)
        m["labels"] = tok(text_target=batch["target"], max_length=128,
                          truncation=True)["input_ids"]
        return m

    ds = Dataset.from_list(ex).map(enc, batched=True, remove_columns=["input", "target", "weight"])
    cuda = torch.cuda.is_available()
    device = "cuda" if cuda else ("mps" if torch.backends.mps.is_available() else "cpu")
    targs = Seq2SeqTrainingArguments(
        output_dir=args.out, per_device_train_batch_size=args.bs,
        learning_rate=args.lr, num_train_epochs=args.epochs,
        max_steps=20 if args.smoke else args.max_steps,
        logging_steps=5 if args.smoke else 50, report_to=[],
        # checkpoints so a timeout is never a total loss (smoke: none)
        save_strategy="no" if args.smoke else "steps", save_steps=1500, save_total_limit=1,
        bf16=cuda,                                   # A10G/A100: ~3x over fp32
        gradient_checkpointing=(not cuda),           # only needed on MPS/CPU memory
        use_cpu=(device == "cpu"), predict_with_generate=True,
        disable_tqdm=not args.smoke,                 # line logs stream better
    )
    if not args.eval_only:
        trainer = Seq2SeqTrainer(model=model, args=targs, train_dataset=ds,
                                 data_collator=DataCollatorForSeq2Seq(tok, model=model))
        trainer.train()
        if not args.smoke:
            trainer.save_model(args.out); tok.save_pretrained(args.out)

    # eval on the frozen benchmark
    items = [json.loads(l) for l in (BENCH / "analyzer_benchmark_v1.jsonl").open(encoding="utf-8")]
    if args.smoke:
        items = items[:40]
    model.to(device).eval()
    preds = []
    for i in range(0, len(items), 16):
        batch = [to_input(it["sentence"], it["surface"]) for it in items[i:i+16]]
        e = tok(batch, return_tensors="pt", padding=True, truncation=True, max_length=args.max_len).to(device)
        with torch.no_grad():
            g = model.generate(**e, max_new_tokens=96, num_beams=1)
        preds.extend(tok.batch_decode(g, skip_special_tokens=True))
    tag = "smoke" if args.smoke else (os.environ.get("RUN_TAG") or Path(args.out).name)
    score_predictions(items, preds, tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
