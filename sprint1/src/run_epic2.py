import os
import requests
import json
from loader import load_impact_report
from snapshot_visualizer import generate_snapshot_md

BACKEND_URL = "http://localhost:5000/impact-report"
INPUT_PATH = "input/impact_report.json"

def get_impact_report():
    if os.path.exists(INPUT_PATH):
        return load_impact_report(INPUT_PATH)

    print("📡 Fetching impact report from backend...")
    response = requests.post(
        BACKEND_URL,
        json={
            "repo_url": "https://github.com/owner/repo.git",
            "branch": "main"
        }
    )
    response.raise_for_status()

    os.makedirs("input", exist_ok=True)
    with open(INPUT_PATH, "w") as f:
        f.write(response.text)

    return response.json()
