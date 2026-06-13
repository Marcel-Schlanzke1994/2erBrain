# Knowledge Ingestion API

Local Flask reference project for Markdown ingestion, metadata storage, and simple search.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
flask --app second_brain_api.app:create_app run
```
PowerShell: `.venv\Scripts\Activate.ps1`.

## Verify
```bash
python -m pytest -q
ruff check .
ruff format --check .
mypy src
```
