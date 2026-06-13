---
title: "C 13 Common Pitfalls"
language: "c"
level: "intermediate"
topics:
  - "translation units"
  - "pointers"
  - "memory"
  - "parsers"
  - "embedded"
  - "testing"
  - "security"
related:
last_verified: "2026-06-13"
source_type: "derived-example"
---

# C 13 Common Pitfalls

Status: CREATED. NOT VERIFIED unless a command is listed in this repository.

## Purpose

C is best for hardware-near systems, protocol parsers, embedded modules, and precise memory control.

## Core rules

- Keep identifiers, comments, module names, and file names in English.
- Prefer small modules with explicit ownership and error handling.
- Validate external input before parsing, storing, or executing it.
- Write tests for normal cases, edge cases, and failure cases.
- Document assumptions and version-sensitive behavior.

## Minimal example

```c
#include <stddef.h>
#include <stdint.h>

typedef enum { PARSER_OK, PARSER_INCOMPLETE, PARSER_OVERFLOW } ParserStatus;

ParserStatus copy_payload(const uint8_t *input, size_t input_len, uint8_t *output, size_t output_cap, size_t *written) {
    if (input_len > output_cap) return PARSER_OVERFLOW;
    for (size_t i = 0; i < input_len; ++i) output[i] = input[i];
    *written = input_len;
    return PARSER_OK;
}
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

- header/source split.
- pointer output parameter.
- safe array handling.
- message parser.
- state machine.
- bit masks.
- safe allocation.
- enum error codes.
- hardware test harness.
