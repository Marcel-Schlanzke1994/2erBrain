---
title: "Lua Exercises"
language: "lua"
level: "intermediate"
topics:
  - "tables"
  - "closures"
  - "modules"
  - "metatables"
  - "events"
  - "sandboxing"
  - "testing"
related:
last_verified: "2026-06-13"
source_type: "derived-example"
---

# Lua Exercises

Status: CREATED. NOT VERIFIED unless a command is listed in this repository.

## Purpose

Lua is best for lightweight, embeddable gameplay scripting, configuration, events, quests, and runtime customization.

## Core rules

- Keep identifiers, comments, module names, and file names in English.
- Prefer small modules with explicit ownership and error handling.
- Validate external input before parsing, storing, or executing it.
- Write tests for normal cases, edge cases, and failure cases.
- Document assumptions and version-sensitive behavior.

## Minimal example

```lua
local EventEngine = {}

function EventEngine.run(event, context)
  if event.condition(context) then
    return event.reward(context)
  end
  return nil
end

return EventEngine
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

- Lua module.
- event system.
- quest definition.
- NPC behavior.
- reward table.
- sandbox.
- C++ interface.
- pcall error handling.
