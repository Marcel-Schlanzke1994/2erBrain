---
title: "C++ 01 Foundations"
language: "cpp"
level: "foundation"
topics:
  - "raii"
  - "smart pointers"
  - "stl"
  - "templates"
  - "concurrency"
  - "cmake"
  - "unreal"
  - "security"
related:
last_verified: "2026-06-13"
source_type: "derived-example"
---

# C++ 01 Foundations

Status: CREATED. NOT VERIFIED unless a command is listed in this repository.

## Purpose

Modern C++ is best for performance, game cores, Unreal-adjacent systems, resource ownership, and engine modules.

## Core rules

- Keep identifiers, comments, module names, and file names in English.
- Prefer small modules with explicit ownership and error handling.
- Validate external input before parsing, storing, or executing it.
- Write tests for normal cases, edge cases, and failure cases.
- Document assumptions and version-sensitive behavior.

## Minimal example

```cpp
#include <memory>
#include <vector>

class Component {
public:
  virtual ~Component() = default;
  virtual void tick(float delta_seconds) = 0;
};

class Entity {
public:
  void add(std::unique_ptr<Component> component) { components_.push_back(std::move(component)); }
  void tick(float dt) { for (auto& component : components_) component->tick(dt); }
private:
  std::vector<std::unique_ptr<Component>> components_;
};
```


## Common failure and correction

Bad pattern: hidden global state, unchecked input, or unclear ownership.

Correct pattern: pass dependencies explicitly, validate inputs, return structured errors, and test boundaries.

## Production checklist

- [ ] Inputs validated.
- [ ] Errors are explicit and logged without secrets.
- [ ] Dependencies and versions documented.
- [ ] Tests exist and can be run locally.
- [ ] Security review completed.

## Exercises

1. FOUNDATION: explain the minimal example line by line.
2. INTERMEDIATE: add one error path and one test.
3. ADVANCED: refactor the example into modules.
4. PRODUCTION: document data flow, failure modes, and quality gates.

## Required example coverage

- RAII class.
- std::unique_ptr.
- composition over inheritance.
- gameplay component.
- event bus.
- CMake project.
- unit tests.
- C++ to Lua integration.
- Unreal-like class structure.
