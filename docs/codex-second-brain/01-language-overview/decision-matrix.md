---
title: "Decision Matrix"
language: "cross-language"
level: "foundation"
topics:
  - "decisions"
related:
last_verified: "2026-06-13"
source_type: "derived-example"
---

# Decision Matrix

Use Python when you need rapid delivery, APIs, bots, automation, data processing, RAG pipelines, or glue code.

Use C when you need hardware-near code, minimal runtime, protocol parsers, firmware modules, or exact memory layout.

Use Lua when designers or operators need safe, configurable runtime behavior such as quests, events, NPC behavior, and rewards without recompiling the core.

Use C++ when you need performance, rich abstractions, RAII, large game systems, Unreal Engine integration, or complex resource ownership.

Combine Python and C++ when Python orchestrates workflows while C++ performs latency-sensitive simulation or game-core work.

Combine C++ and Lua when C++ owns the engine/runtime and Lua owns dynamic gameplay rules.

Use C instead of C++ when the target toolchain is tiny, ABI simplicity matters, or firmware conventions require C.

Use Lua instead of compiled gameplay logic when rules change frequently and can be restricted through a sandbox.

Avoid a language when its failure mode dominates the project: avoid C/C++ for simple CRUD APIs, avoid Python for hard real-time firmware, avoid Lua for core security decisions.
