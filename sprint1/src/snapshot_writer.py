import json
import uuid
from datetime import datetime
from pathlib import Path


def write_snapshot(impact_report: dict) -> str:
    """
    Generate EPIC-2 Sprint-1 documentation snapshot JSON
    """

    repo_name = impact_report["context"]["repository"]
    branch = impact_report["context"]["branch"]
    commit = impact_report["context"]["commit_sha"]

    snapshot = {
        "snapshot_id": str(uuid.uuid4()),
        "repo": {
            "name": repo_name,
            "branch": branch,
            "commit": commit
        },
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "docs_bucket_path": f"s3://ci-living-docs/{repo_name}/sprint1/{commit}/",
        "generated_files": [
            {
                "file": "README.generated.md",
                "type": "README"
            },
            {
                "file": "api/api-reference.md",
                "type": "API_DOC"
            },
            {
                "file": "adr/ADR-001.md",
                "type": "ADR"
            },
            {
                "file": "architecture/system.mmd",
                "type": "ARCHITECTURE_DIAGRAM"
            },
            {
                "file": "architecture/sequence.mmd",
                "type": "SEQUENCE_DIAGRAM"
            },
            {
                "file": "architecture/er.mmd",
                "type": "ER_DIAGRAM"
            },
            {
                "file": "tree.txt",
                "type": "FOLDER_STRUCTURE"
            }
        ],
        "documentation_health": {
            "missing_sections": [],
            "template_followed": True
        }
    }

    return json.dumps(snapshot, indent=2)
