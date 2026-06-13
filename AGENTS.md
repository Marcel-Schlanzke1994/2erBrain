# Repository Instructions

Mission: maintain a production-oriented Codex Second Brain for Python, C, Lua, C++, cross-language architecture, security, and RAG-friendly engineering knowledge.

## Required checks
- All checks: `python scripts/run_all_checks.py`
- Docs: `python scripts/validate_docs.py`, `python scripts/check_local_links.py`, `python scripts/check_placeholder_content.py`
- Python API: `cd examples/python/knowledge_ingestion_api && python -m pytest -q && ruff check . && ruff format --check . && mypy src`
- C parser: `cd examples/c/event_parser && cmake -S . -B build && cmake --build build && ctest --test-dir build --output-on-failure`
- Lua engine: `cd examples/lua/gameplay_event_engine && lua tests/run_tests.lua`
- C++ core: `cd examples/cpp/modular_gameplay_core && cmake -S . -B build && cmake --build build && ctest --test-dir build --output-on-failure`

## Rules
- Never read, print, commit, or log real secrets. Use `.env.example` placeholders only.
- Do not deploy or call production services from this repo.
- Documentation must be topic-specific, source-aware, and avoid placeholder-only content.
- Update tests when behavior changes; report blocked verification honestly.
- Preserve architecture unless an ADR documents the reason for change.
- Keep cross-language boundaries explicit: validate inputs, translate errors, and document ownership/lifetime.
- Use checkpoint commits for meaningful changes.
