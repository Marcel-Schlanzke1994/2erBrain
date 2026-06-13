---
title: "Serialization And Message Contracts"
language: "cross-language"
level: "production"
topics:
  - "reference"
related:
last_verified: "2026-06-13"
source_type: "derived-example"
---

# Serialization And Message Contracts

Prefer versioned JSON for debuggable control-plane contracts and binary frames for constrained embedded links. Every contract needs schema version, message type, correlation id, timestamp, payload, and error envelope.

## Verification

Status: CREATED. NOT VERIFIED for executable behavior unless separately tested.
