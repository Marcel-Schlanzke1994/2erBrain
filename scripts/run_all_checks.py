import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    ["python", "scripts/validate_docs.py"],
    ["python", "scripts/check_local_links.py"],
    ["python", "scripts/check_placeholder_content.py"],
    ["python", "-m", "pytest", "-q", "examples/python/knowledge_ingestion_api/tests"],
]

failed = []
for command in COMMANDS:
    print("$", " ".join(command))
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode != 0:
        failed.append(command)

sys.exit(1 if failed else 0)
