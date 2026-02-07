import json
from datetime import datetime

def write_snapshot(report):
    snapshot = {
        "commit": report["context"]["commit_sha"],
        "generated_at": datetime.utcnow().isoformat(),
        "files_generated": [
            "README.generated.md",
            "api-reference.md",
            "ADR-001.md",
            "system.mmd",
            "sequence.mmd",
            "er.mmd"
        ]
    }
    return json.dumps(snapshot, indent=2)
