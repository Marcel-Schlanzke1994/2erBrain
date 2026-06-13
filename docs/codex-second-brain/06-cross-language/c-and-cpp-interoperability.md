---
title: "C And Cpp Interoperability"
language: "cross-language"
level: "production"
topics:
  - "reference"
related:
last_verified: "2026-06-13"
source_type: "derived-example"
---

# C And Cpp Interoperability

Use extern "C" boundaries for ABI stability. Keep ownership explicit: caller allocates/callee fills, callee allocates/caller frees through a matching destroy function, or immutable borrowed views.

## Verification

Status: CREATED. NOT VERIFIED for executable behavior unless separately tested.
