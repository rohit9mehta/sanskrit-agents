"""Deploy the live ask-box to Render (free web service).

Needs in PROJECT_ROOT/.env:
  RENDER_API_KEY=rnd_...   (render.com → Account Settings → API Keys)
  OPENAI_API_KEY=sk-...    (becomes a Render env secret, never committed)

Creates (or updates) a free-tier Python web service that runs
agent/space-build/app.py straight from the public GitHub repo, sets the
rate-limit env vars, waits for the first deploy, and prints the URL.

NOTE: autoDeploy is set, but push-webhooks do NOT fire for API-created
services without Render's GitHub App installed on the repo — after
pushing, re-run this script (its update path triggers a deploy), or the
site keeps serving the old commit (observed 2026-08-20).

KEEP-WARM NOTE (deliberately NOT enabled — Rohit's call, 2026-08-12):
free services spin down after 15 idle minutes and take ~1 min to wake.
Render grants 750 free instance-hours/month (a full month is 744), so a
ping every ~10 minutes from any free cron (GitHub Actions, cron-job.org)
can keep it warm during a launch window, within the allowance. When
wanted: ping GET {url}/healthz. Until then, cold visitors see Render's
loading page for ~a minute, and the HF static page stays the instant
front door.
"""

import os
import sys
import time

import requests

from shastrartha.llm import load_env

API = "https://api.render.com/v1"
SERVICE_NAME = "shastrartha"
REPO = "https://github.com/rohit9mehta/sanskrit-agents"

LIMITS = {
    "RL_PER_MIN": "4",
    "RL_PER_DAY": "20",
    "RL_GLOBAL_CALLS_PER_DAY": "150",
    "RL_GLOBAL_USD_PER_DAY": "3.0",
}


def main() -> int:
    load_env()
    key = os.environ.get("RENDER_API_KEY")
    if not key:
        print("RENDER_API_KEY missing from .env (render.com → Account Settings → API Keys)")
        return 1
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    owner = requests.get(f"{API}/owners", headers=h, timeout=30).json()
    owner_id = owner[0]["owner"]["id"]

    existing = requests.get(f"{API}/services", headers=h,
                            params={"name": SERVICE_NAME, "limit": 5}, timeout=30).json()
    svc = next((s["service"] for s in existing
                if s["service"]["name"] == SERVICE_NAME), None)

    env_vars = [{"key": "OPENAI_API_KEY", "value": os.environ["OPENAI_API_KEY"]}]
    env_vars += [{"key": k, "value": v} for k, v in LIMITS.items()]

    if svc is None:
        body = {
            "type": "web_service",
            "name": SERVICE_NAME,
            "ownerId": owner_id,
            "repo": REPO,
            "branch": "main",
            "autoDeploy": "yes",
            "rootDir": "agent/space-build",
            "serviceDetails": {
                "runtime": "python",
                "plan": "free",
                "region": "oregon",
                "envSpecificDetails": {
                    "buildCommand": "pip install -r requirements.txt",
                    "startCommand": "python app.py",
                },
            },
            "envVars": env_vars,
        }
        r = requests.post(f"{API}/services", headers=h, json=body, timeout=60)
        if r.status_code not in (200, 201):
            print("create failed:", r.status_code, r.text[:500])
            return 1
        svc = r.json()["service"]
        print("service created:", svc["id"])
    else:
        print("service exists:", svc["id"], "— updating env + redeploying")
        requests.put(f"{API}/services/{svc['id']}/env-vars", headers=h,
                     json=env_vars, timeout=60)
        requests.post(f"{API}/services/{svc['id']}/deploys", headers=h,
                      json={}, timeout=60)

    url = svc.get("serviceDetails", {}).get("url") or f"https://{SERVICE_NAME}.onrender.com"
    print("waiting for deploy (build + start usually 2-5 min)...")
    for _ in range(60):
        time.sleep(15)
        deps = requests.get(f"{API}/services/{svc['id']}/deploys",
                            headers=h, params={"limit": 1}, timeout=30).json()
        status = deps[0]["deploy"]["status"] if deps else "?"
        print("  deploy status:", status, flush=True)
        if status == "live":
            print(f"LIVE: {url}")
            return 0
        if status in ("build_failed", "update_failed", "canceled"):
            print("deploy failed — check the Render dashboard logs")
            return 1
    print("timed out waiting; check the Render dashboard")
    return 1


if __name__ == "__main__":
    sys.exit(main())
