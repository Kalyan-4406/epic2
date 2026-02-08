#!/usr/bin/env python3
"""
EPIC-2 Documentation Generator
Orchestrates all documentation generation tasks based on impact report from EPIC-1
"""
import os
import sys
import json
import requests
from pathlib import Path

# Import all generators
from loader import load_impact_report
from readme_generator import generate_readme
from api_generator import generate_api_docs
from adr_generator import generate_adr
from diagram_generator import system_diagram, sequence_diagram, er_diagram
from tree_generator import generate_tree
from snapshot_writer import write_snapshot

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000/impact-report")
INPUT_PATH = "sprint1/input/impact_report.json"
OUTPUT_BASE = "sprint1/artifacts/docs"

def ensure_directories():
    """Create all required output directories"""
    dirs = [
        OUTPUT_BASE,
        f"{OUTPUT_BASE}/api",
        f"{OUTPUT_BASE}/adr",
        f"{OUTPUT_BASE}/architecture",
    ]
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
    print(f"✅ Created output directories in {OUTPUT_BASE}")

def get_impact_report():
    """Fetch or load impact report"""
    # First check if file exists locally
    if os.path.exists(INPUT_PATH):
        print(f"📂 Loading existing impact report from {INPUT_PATH}")
        return load_impact_report()

    # Otherwise fetch from backend
    print("📡 Fetching impact report from backend...")
    try:
        response = requests.post(
            BACKEND_URL,
            json={
                "repo_url": "https://github.com/owner/repo.git",
                "branch": "main"
            },
            timeout=30
        )
        response.raise_for_status()

        # Save for future use
        os.makedirs(os.path.dirname(INPUT_PATH), exist_ok=True)
        with open(INPUT_PATH, "w") as f:
            f.write(response.text)
        
        print(f"✅ Saved impact report to {INPUT_PATH}")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching impact report: {e}")
        sys.exit(1)

def write_file(path, content):
    """Write content to file with error handling"""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Generated: {path}")
    except Exception as e:
        print(f"❌ Error writing {path}: {e}")
        raise

def generate_all_docs(report):
    """Generate all documentation files from impact report"""
    print("\n🚀 Starting documentation generation...")
    
    try:
        # 1. Generate README
        readme_content = generate_readme(report)
        write_file(f"{OUTPUT_BASE}/README.generated.md", readme_content)
        
        # 2. Generate API documentation
        api_content = generate_api_docs(report)
        write_file(f"{OUTPUT_BASE}/api/api-reference.md", api_content)
        
        # 3. Generate ADR
        adr_content = generate_adr(report)
        write_file(f"{OUTPUT_BASE}/adr/ADR-001.md", adr_content)
        
        # 4. Generate Architecture Diagram
        system_content = system_diagram()
        write_file(f"{OUTPUT_BASE}/architecture/system.mmd", system_content)
        
        # 5. Generate Sequence Diagram
        sequence_content = sequence_diagram()
        write_file(f"{OUTPUT_BASE}/architecture/sequence.mmd", sequence_content)
        
        # 6. Generate ER Diagram
        er_content = er_diagram()
        write_file(f"{OUTPUT_BASE}/architecture/er.mmd", er_content)
        
        # 7. Generate folder tree
        tree_content = generate_tree(report)
        write_file(f"{OUTPUT_BASE}/tree.txt", tree_content)
        
        # 8. Generate documentation snapshot JSON
        snapshot_content = write_snapshot(report)
        write_file(f"{OUTPUT_BASE}/doc_snapshot.json", snapshot_content)
        
        print("\n✨ Documentation generation complete!")
        print(f"📁 All files saved to: {OUTPUT_BASE}/")
        
    except Exception as e:
        print(f"\n❌ Documentation generation failed: {e}")
        sys.exit(1)

def main():
    """Main execution flow"""
    print("=" * 60)
    print("EPIC-2 Documentation Generator")
    print("=" * 60)
    
    # Step 1: Ensure output directories exist
    ensure_directories()
    
    # Step 2: Get impact report (from file or backend)
    report = get_impact_report()
    
    # Step 3: Generate all documentation
    generate_all_docs(report)
    
    print("\n" + "=" * 60)
    print("✅ EPIC-2 pipeline completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
