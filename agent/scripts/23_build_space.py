"""Assemble the deployable ask-box bundle into space-build/ (committed:
Render builds the web service straight from this directory of the GitHub
repo, and scripts/24_deploy_space.py pushes it to the HF Space repo).

Contents: app.py + Dockerfile + README (Space front-matter) + the minimal
package slice (llm/ask/webui/normalize/texts) + apparatus JSONs + canned.json
(pre-computed answers from agent/data/canned_answers.json, cites left as
[slug unit] for client-side linking).
"""

import json
import shutil
import sys

from shastrartha.ask import TEXT_META
from shastrartha.canned import canned_answer
from shastrartha.llm import MODEL
from shastrartha.texts import AGENT_DIR, DATA_DIR
from shastrartha.webui import CANNED_QUESTIONS, md_lite

BUILD = AGENT_DIR / "space-build"
OUTPUT = AGENT_DIR / "output"

README = """---
title: Śāstrārtha
emoji: 🪷
colorFrom: yellow
colorTo: red
sdk: docker
app_port: 7860
pinned: false
license: mit
short_description: Ask the śāstras. Cited, grammar-checked answers.
---

# Śāstrārtha: ask the śāstras

A research demo: questions answered ONLY from a library of Sanskrit
commentary-grounded, Pāṇini-grammar-checked machine translations —
every claim cited to the tradition's own commentaries, clickable through
to the verse apparatus.

Library: Triṃśikā (Sthiramati), Īśopaniṣad (Śaṅkara), Bhagavad-Gītā ch. 2
(Śaṅkara), Yoga-sūtras ch. 1 (Vyāsa).

Source + method: https://github.com/rohit9mehta/sanskrit-agents
"""

DOCKERFILE = f"""FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
EXPOSE 7860
CMD ["python", "app.py"]
"""


def main() -> int:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    # Mirror the repo's agent/src/shastrartha depth: texts.py finds
    # PROJECT_ROOT three parents up, so /app/agent/src/shastrartha → /app.
    pkg = BUILD / "agent" / "src" / "shastrartha"
    pkg.mkdir(parents=True)
    src = AGENT_DIR / "src" / "shastrartha"
    for mod in ("llm", "ask", "webui", "normalize", "texts"):
        shutil.copy(src / f"{mod}.py", pkg / f"{mod}.py")
    (pkg / "__init__.py").write_text(
        '"""Śāstrārtha demo slice (see github.com/rohit9mehta/sanskrit-agents)."""\n')

    # data: apparatus JSONs (layout mirrors the repo so texts.py paths work)
    n = 0
    for slug in TEXT_META:
        pattern = "v[0-9][0-9]" if slug == "trimsika" else "*"
        base = OUTPUT if slug == "trimsika" else OUTPUT / slug
        for p in sorted(base.glob(f"{pattern}/apparatus.json")):
            rel = p.relative_to(AGENT_DIR)
            dst = BUILD / "agent" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(p, dst)
            n += 1
    mula_dst = BUILD / "agent" / "data" / "mula" / "trimsika.json"
    mula_dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(DATA_DIR / "mula" / "trimsika.json", mula_dst)

    # canned answers (cites left un-linked; the client links them)
    canned = {}
    for q in CANNED_QUESTIONS:
        res = canned_answer(q)
        canned[q] = {
            "answer_html_plain": md_lite(res["answer"]),
            "citations": res["citations"],
        }
    (BUILD / "canned.json").write_text(
        json.dumps(canned, ensure_ascii=False), encoding="utf-8")

    shutil.copy(AGENT_DIR / "space" / "app.py", BUILD / "app.py")
    (BUILD / "requirements.txt").write_text("openai>=2.45.0\n")
    (BUILD / "README.md").write_text(README, encoding="utf-8")
    (BUILD / "Dockerfile").write_text(DOCKERFILE, encoding="utf-8")
    (BUILD / ".gitignore").write_text("__pycache__/\n")

    print(f"space-build/: {n} apparatus files, {len(canned)} canned answers, model {MODEL}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
