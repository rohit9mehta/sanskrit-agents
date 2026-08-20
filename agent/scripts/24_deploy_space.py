"""Deploy space-build/ to Hugging Face Spaces.

Needs in PROJECT_ROOT/.env:
  HF_TOKEN=hf_...        (a WRITE token from huggingface.co/settings/tokens)
  OPENAI_API_KEY=sk-...  (already present; becomes a Space *secret*)

Creates/updates the Space, uploads the bundle, sets the OpenAI key as a
secret and the rate limits as variables, then prints the URL.
"""

import os
import sys

from shastrartha.llm import load_env
from shastrartha.texts import AGENT_DIR

BUILD = AGENT_DIR / "space-build"
SPACE_NAME = "shastrartha"

LIMITS = {
    "RL_PER_MIN": "4",
    "RL_PER_DAY": "20",
    "RL_GLOBAL_CALLS_PER_DAY": "150",
    "RL_GLOBAL_USD_PER_DAY": "3.0",
}


def main() -> int:
    load_env()
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("HF_TOKEN missing: create a WRITE token at "
              "huggingface.co/settings/tokens and add HF_TOKEN=hf_... to .env")
        return 1
    if not BUILD.exists():
        print("space-build/ missing — run scripts/23_build_space.py first")
        return 1

    from huggingface_hub import HfApi

    api = HfApi(token=token)
    user = api.whoami()["name"]
    repo_id = f"{user}/{SPACE_NAME}"
    api.create_repo(repo_id, repo_type="space", space_sdk="docker",
                    exist_ok=True, private=False)

    api.add_space_secret(repo_id, "OPENAI_API_KEY", os.environ["OPENAI_API_KEY"])
    for k, v in LIMITS.items():
        api.add_space_variable(repo_id, k, v)

    api.upload_folder(folder_path=str(BUILD), repo_id=repo_id,
                      repo_type="space",
                      commit_message="Deploy Śāstrārtha demo")
    print(f"deployed: https://huggingface.co/spaces/{repo_id}")
    print("(first build takes a few minutes; watch the Space's Logs tab)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
