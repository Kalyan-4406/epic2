import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

EPIC1_URL = "https://code-detect.onrender.com/analyze"

@app.route("/generate-docs", methods=["POST"])
def generate_docs():
    payload = request.json

    # Call EPIC-1
    response = requests.post(EPIC1_URL, json=payload)
    impact_report = response.json()

    # Save JSON for EPIC-2
    with open("sprint1/input/impact_report.json", "w") as f:
        json.dump(impact_report, f, indent=2)

    # Trigger EPIC-2 generator
    os.system("python sprint1/src/run_epic2.py")

    return jsonify({"status": "docs generated"})
