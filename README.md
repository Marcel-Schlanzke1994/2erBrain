# 2erBrain

`2erBrain` is a production-oriented Codex Second Brain for Python, C, Lua, modern C++, cross-language boundaries, secure coding, architecture, testing, CI/CD, embedded-style parsers, gameplay systems, and RAG pipelines.

## Quick start

```bash
python scripts/run_all_checks.py
```

## Start location
- [Codex Second Brain overview](docs/codex-second-brain/README.md)
- [Navigation](docs/codex-second-brain/00-system/navigation.md)
- [Learning roadmap](docs/codex-second-brain/00-system/learning-roadmap.md)
- [Quality gates](docs/codex-second-brain/11-evaluations/quality-gates.md)
- [Final verification report](docs/codex-second-brain/00-system/final-verification-report.md)

## Executable examples
- `examples/python/knowledge_ingestion_api`: Flask + SQLite Markdown ingestion API.
- `examples/c/event_parser`: C17 framed byte parser with CTest.
- `examples/lua/gameplay_event_engine`: Lua event, reward, cooldown, and sandbox engine.
- `examples/cpp/modular_gameplay_core`: C++20 event bus and gameplay component core.
- `examples/integrated/second_brain_reference`: versioned cross-language JSON contract and fixture.

## CI workflow
`.github/workflows/ci.yml` runs documentation checks, Python tests/lint/type checks, C and C++ CMake/CTest builds, and Lua tests where Lua is installed.

## Secret safety
Never commit real `.env` files, tokens, private keys, webhook URLs, database passwords, or production credentials. Use safe placeholders such as `OPENAI_API_KEY=<set-in-environment>`.

## Future Codex agents
Read `AGENTS.md` before editing. Preserve the architecture unless an ADR justifies a change, update tests with behavior changes, and report blocked verification honestly.

## Completion status
The repository has executable reference projects, validators, CI, audit documentation, and final verification reporting. Known limitations are documented in the final verification report.
