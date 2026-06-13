FINAL IMPLEMENTATION ORDER
Complete the Codex Second Brain for Python, C, Lua, and Modern C++
0. Mission

You are working inside the following GitHub repository:

https://github.com/Marcel-Schlanzke1994/2erBrain

Your task is to transform the existing repository from a documentation scaffold into a complete, technically useful, RAG-friendly, production-oriented Codex Second Brain for:

Python
C
Lua
modern C++
cross-language integration
software architecture
secure coding
testing
CI/CD
embedded programming
game-development architecture
Unreal-adjacent gameplay systems
AI and RAG pipelines

The repository already contains a large number of Markdown files under:

docs/codex-second-brain/

However, many of these files are currently only shallow templates, repeated placeholders, one-sentence summaries, or minimal examples.

Your responsibility is to finish the implementation properly.

Do not merely create additional outlines.
Do not create placeholder-only files.
Do not repeat the same generic explanation across multiple chapters.
Do not stop after planning.
Do not claim completion unless the required work has actually been implemented and verified.

The final repository must function simultaneously as:

a structured learning system;
a practical engineering handbook;
a RAG-friendly technical knowledge base;
a reference implementation collection;
a repository-level instruction source for future Codex agents;
a secure foundation for later FUR, Aetherfall, Discord, Flask, embedded, and game-system projects.
1. Current Repository State

Assume the repository currently contains:

a useful documentation directory structure;
a root README.md;
a stored German master order;
an English master-order translation;
navigation files;
language comparison files;
short architecture notes;
security placeholders;
language chapter placeholders;
reference-project descriptions;
evaluation placeholders;
an AGENTS.second-brain.template.md.

The structure is useful, but the implementation is incomplete.

The repository currently lacks sufficient depth in several critical areas:

topic-specific explanations;
realistic examples;
executable reference projects;
tests;
build configurations;
Python packaging;
C compilation targets;
Lua test runners;
C++ CMake targets;
GitHub Actions workflows;
verified quality gates;
meaningful exercise solutions;
complete architecture decisions;
complete security guidance;
integration smoke tests;
final verification reports.

Your task is not to redesign the repository unnecessarily.
Your task is to complete it.

2. Mandatory Operating Rules
2.1 Inspect Before Editing

Before making changes:

Read the root README.md.
Read the original German master order.
Read the English master-order translation.
Read:
docs/codex-second-brain/README.md
docs/codex-second-brain/00-system/navigation.md
docs/codex-second-brain/00-system/source-policy.md
docs/codex-second-brain/00-system/definition-of-done.md
docs/codex-second-brain/00-system/learning-roadmap.md
docs/codex-second-brain/10-templates/AGENTS.second-brain.template.md
Inventory all files in the repository.
Detect duplicate or near-duplicate documentation bodies.
Identify placeholder-only files.
Identify missing executable artifacts.
Check whether .gitignore, .github/workflows/, AGENTS.md, and build files exist.
Create an initial audit report before implementing the remaining work.

Create:

docs/codex-second-brain/00-system/implementation-audit.md

The audit must include:

discovered repository structure;
missing artifacts;
duplicate-template findings;
files requiring expansion;
security observations;
testability observations;
implementation phases;
known limitations.

Do not include secret values in the report.

2.2 Work on a Dedicated Branch

Create and use:

codex/finalize-second-brain

Do not work directly on main.

Use meaningful checkpoint commits. Keep each commit focused.

Recommended commit sequence:

chore: add repository instructions and implementation audit
feat: implement Python knowledge ingestion reference project
docs: complete Python learning track
feat: implement C embedded event parser reference project
docs: complete C learning track
feat: implement Lua gameplay event engine
docs: complete Lua learning track
feat: implement C++ modular gameplay core
docs: complete modern C++ learning track
feat: add cross-language contracts and integration smoke test
docs: complete architecture security and evaluation guides
ci: add automated quality gates
docs: add final verification report and completion status

Do not create empty commits.

2.3 Secret Hygiene Is Non-Negotiable

Never print, copy, expose, or commit:

API keys;
access tokens;
Discord bot tokens;
GitHub tokens;
OpenAI keys;
webhook URLs;
client secrets;
database passwords;
private keys;
session secrets;
credentials from local configuration.

Do not read or display .env values.

You may create safe examples such as:

OPENAI_API_KEY=<set-in-environment>
DISCORD_TOKEN=<set-in-environment>
DATABASE_URL=sqlite:///local.db
APP_ENV=development
LOG_LEVEL=INFO

Ensure .gitignore includes at least:

.env
.env.*
!.env.example
*.db
*.sqlite
*.sqlite3
__pycache__/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
venv/
build/
dist/
cmake-build-*/
CMakeFiles/
Testing/
.codex-log/
*.log

When scanning for accidentally committed secrets:

report only the affected path;
report the variable name or redacted pattern;
never reproduce the discovered credential;
recommend rotation when applicable.

Do not deploy anything.
Do not invoke external production services.
Do not send network requests requiring real credentials.
Do not alter infrastructure.

2.4 Create a Real Root AGENTS.md

The repository already contains:

docs/codex-second-brain/10-templates/AGENTS.second-brain.template.md

Create a concise and actionable repository-level file:

AGENTS.md

It must include:

repository mission;
exact test commands;
formatting and linting commands;
secret-handling rules;
no-deployment rule;
documentation rules;
status-label rules;
instructions to avoid placeholder-only documentation;
instructions to update tests whenever behavior changes;
rules for reporting blocked verification honestly;
rules for cross-language ownership and error boundaries;
instructions to use checkpoint commits;
instructions to preserve existing architecture unless a documented ADR justifies a change.

Keep root AGENTS.md concise enough to be useful in future Codex sessions.

Create specialized nested instruction files only when they add real value, for example:

examples/python/AGENTS.md
examples/c/AGENTS.md
examples/lua/AGENTS.md
examples/cpp/AGENTS.md

Do not duplicate the entire root file in nested files. Add only language-specific commands and constraints.

Because AGENTS.md created during the current session may not automatically reload into the active instruction chain, read it manually after creating it and follow it for the remainder of the current implementation.

3. Documentation Quality Standard

Every existing chapter must be rewritten into a topic-specific document.

Generic duplicated bodies are forbidden.

Each substantial documentation chapter must contain:

1. Purpose
2. Why the topic matters
3. Core concepts
4. Terminology
5. Minimal example
6. Realistic applied example
7. Common failure patterns
8. Corrected implementation
9. Security considerations
10. Testing and debugging notes
11. Practical checklist
12. Exercises
13. Links to related chapters
14. Links to the relevant reference project
15. Official or high-quality source references

Use front matter consistently:

---
title: "..."
language: "python | c | lua | cpp | cross-language | architecture | security"
level: "foundation | intermediate | advanced | production"
topics:
  - "..."
related:
  - "..."
last_verified: "YYYY-MM-DD"
source_type: "official-docs | standard | guideline | derived-example"
---

Rules:

Use English for documentation.
Use English for code identifiers and comments.
Explain difficult concepts in accessible language.
Prefer concrete examples over abstract claims.
Use Mermaid diagrams where they clarify architecture, data flow, ownership, state transitions, or dependencies.
Distinguish facts from recommendations.
Label unexecuted examples as NOT VERIFIED.
Do not label content as VERIFIED unless a corresponding command was run successfully.
Add local links between related documents.
Avoid broken links.
Avoid giant monolithic files when a topic belongs in a dedicated chapter.
Avoid shallow files that contain only one sentence.
4. Required Repository Structure

Preserve and expand the existing documentation structure under:

docs/codex-second-brain/

Add executable examples under:

examples/

Add validation scripts under:

scripts/

Add CI under:

.github/workflows/

The completed high-level structure must include:

.
├── AGENTS.md
├── README.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   └── codex-second-brain/
│       ├── README.md
│       ├── 00-system/
│       ├── 01-language-overview/
│       ├── 02-python/
│       ├── 03-c/
│       ├── 04-lua/
│       ├── 05-cpp/
│       ├── 06-cross-language/
│       ├── 07-architecture/
│       ├── 08-security/
│       ├── 09-projects/
│       ├── 10-templates/
│       ├── 11-evaluations/
│       └── 12-sources/
├── examples/
│   ├── python/
│   │   └── knowledge_ingestion_api/
│   ├── c/
│   │   └── event_parser/
│   ├── lua/
│   │   └── gameplay_event_engine/
│   ├── cpp/
│   │   └── modular_gameplay_core/
│   └── integrated/
│       └── second_brain_reference/
└── scripts/
    ├── validate_docs.py
    ├── check_local_links.py
    ├── check_placeholder_content.py
    └── run_all_checks.py

You may add files when they improve correctness, maintainability, or testing.

Do not add unnecessary dependencies or unused files.

5. Implement the Documentation Tracks Properly
5.1 Complete the Python Track

Rewrite and complete every file under:

docs/codex-second-brain/02-python/

Cover at least:

Python execution model;
indentation and syntax;
variables;
dynamic typing;
type hints;
primitive types;
lists;
tuples;
dictionaries;
sets;
control flow;
functions;
positional and keyword arguments;
default arguments;
return values;
scope;
modules;
packages;
imports;
virtual environments;
dependency management;
classes;
composition;
inheritance;
dataclasses;
exceptions;
custom exceptions;
context managers;
file I/O;
JSON;
CSV;
SQLite;
PostgreSQL concepts;
MongoDB concepts;
repository pattern;
configuration management;
environment variables;
structured logging;
Flask;
REST endpoints;
request validation;
API error envelopes;
asyncio;
asynchronous HTTP concepts;
retry strategies;
timeouts;
rate limiting;
threads;
processes;
unit tests;
pytest;
fixtures;
mocking;
linting;
formatting;
type checking;
debugging;
profiling;
Discord bot cog architecture;
RAG ingestion;
chunking;
metadata;
search;
agent orchestration;
safe secret handling;
common production pitfalls.

Include realistic examples for:

a Flask health endpoint;
a validated document-ingestion endpoint;
a SQLite repository class;
structured logging;
an async client with timeout handling;
retry logic;
a Discord bot cog;
pytest tests;
a safe .env.example;
a Markdown-ingestion pipeline.

Do not use real API keys or external production calls.

5.2 Complete the C Track

Rewrite and complete every file under:

docs/codex-second-brain/03-c/

Cover at least:

source files;
header files;
translation units;
compiler;
linker;
preprocessing;
include guards;
types;
integer widths;
operators;
control flow;
functions;
scope;
call-by-value;
pointer-based output parameters;
arrays;
strings;
pointer arithmetic;
const;
structs;
enums;
unions;
typedef;
stack;
heap;
static storage duration;
malloc;
calloc;
realloc;
free;
ownership;
memory leaks;
double free;
use-after-free;
dangling pointers;
null pointers;
buffer overflow;
integer overflow;
file I/O;
bitwise operators;
masks;
flags;
state machines;
Moore machines;
Mealy machines;
message framing;
start bytes;
end bytes;
parsers;
bounded buffers;
embedded design;
registers;
timers;
interrupts;
hardware abstraction;
error codes;
defensive programming;
compiler warnings;
sanitizers;
static analysis;
hardware-independent test harnesses;
common production pitfalls.

Include realistic examples for:

.h and .c separation;
pointer output parameters;
safe bounded copying;
a state machine;
a framed-message parser;
bit masks;
safe allocation and cleanup;
enum-based error codes;
unit-style tests without hardware;
sanitizer usage.
5.3 Complete the Lua Track

Rewrite and complete every file under:

docs/codex-second-brain/04-lua/

Cover at least:

Lua syntax;
dynamic typing;
local variables;
global variables;
control flow;
functions;
multiple return values;
tables;
arrays;
dictionaries;
tables as objects;
closures;
higher-order functions;
modules;
require;
metatables;
metamethods;
object-pattern approaches;
assert;
pcall;
xpcall;
file access;
configuration tables;
event handlers;
quest definitions;
NPC behavior;
cooldowns;
rewards;
gameplay rules;
script boundaries;
Lua C API concepts;
C++ embedding;
sandbox design;
allowlists;
restricted environments;
prevention of unsafe global access;
execution-budget concepts;
logging;
testing;
debugging;
common production pitfalls.

Include realistic examples for:

a Lua module;
an event registry;
a quest definition;
an NPC behavior module;
a reward table;
cooldown logic;
pcall error handling;
a restricted sandbox environment;
a script-runtime abstraction;
integration guidance for a C++ host.
5.4 Complete the Modern C++ Track

Rewrite and complete every file under:

docs/codex-second-brain/05-cpp/

Use modern C++ principles.

Cover at least:

compiler;
linker;
source files;
header files;
namespaces;
types;
references;
pointers;
const;
functions;
overloads;
classes;
constructors;
destructors;
access control;
inheritance;
composition;
polymorphism;
abstract interfaces;
virtual destructors;
object lifetime;
ownership;
RAII;
std::unique_ptr;
std::shared_ptr;
std::weak_ptr;
copy semantics;
move semantics;
Rule of Zero;
Rule of Five;
STL containers;
std::vector;
std::array;
std::string;
std::unordered_map;
algorithms;
iterators;
lambdas;
templates;
concepts;
exceptions;
error codes;
result types;
concurrency;
threads;
mutexes;
deadlocks;
data races;
performance;
profiling;
cache awareness;
build systems;
CMake;
dependency management;
unit testing;
CTest;
compiler warnings;
sanitizers;
static analysis;
secure coding;
game-core architecture;
components;
event buses;
Unreal-adjacent architecture;
UObject concepts;
AActor concepts;
UActorComponent concepts;
delegates;
subsystems;
Blueprint boundaries;
Gameplay Ability System as an advanced concept;
client-server principles;
replication concepts;
C++ and Lua integration;
common production pitfalls.

Do not pretend that Unreal Engine itself is installed unless it is actually available.

Explain Unreal-specific examples conceptually where engine compilation is unavailable.

Include realistic examples for:

an RAII wrapper;
correct std::unique_ptr ownership;
composition over inheritance;
a modular gameplay component;
an event bus;
a CMake project;
unit-style tests;
an optional Lua-runtime adapter;
an Unreal-adjacent mapping guide;
error-boundary design.
6. Build Real Executable Reference Projects

Documentation alone is insufficient.

Implement the following executable projects.

6.1 Python Reference Project
Knowledge Ingestion API

Create:

examples/python/knowledge_ingestion_api/
├── AGENTS.md
├── README.md
├── .env.example
├── pyproject.toml
├── src/
│   └── second_brain_api/
│       ├── __init__.py
│       ├── app.py
│       ├── config.py
│       ├── database.py
│       ├── errors.py
│       ├── ingestion.py
│       ├── logging_config.py
│       ├── models.py
│       ├── repository.py
│       └── search.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_api.py
    ├── test_config.py
    ├── test_ingestion.py
    ├── test_repository.py
    └── test_search.py

Functional requirements:

Use Python standard library where practical.
Use Flask for the HTTP API.
Use SQLite for local persistence.
Parse Markdown front matter safely.
Store document metadata and content.
Expose:
GET /health
POST /documents
GET /documents
GET /documents/<id>
GET /search?q=<query>
Validate external input.
Return structured JSON error envelopes.
Use configurable logging.
Never log secrets.
Add tests for:
valid ingestion;
missing title;
malformed metadata;
duplicate ingestion behavior;
successful search;
empty search;
missing document;
configuration defaults;
database initialization.

Add precise setup and execution commands to the project README.md.

Preferred local verification:

cd examples/python/knowledge_ingestion_api
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest -q
ruff check .
ruff format --check .
mypy src

If the environment uses Windows PowerShell, document the equivalent activation command.

Do not claim a command passed unless it was executed successfully.

6.2 C Reference Project
Embedded Event Parser

Create:

examples/c/event_parser/
├── AGENTS.md
├── README.md
├── CMakeLists.txt
├── include/
│   └── event_parser.h
├── src/
│   ├── event_parser.c
│   └── demo.c
└── tests/
    └── test_event_parser.c

Functional requirements:

Use portable C17.
Parse a framed byte protocol.
Use an explicit start byte.
Use an explicit end byte.
Use bounded payload buffers.
Reject oversized payloads.
Model parser states with an enum.
Model parser results with an enum.
Reset safely after malformed messages.
Avoid global mutable state.
Provide a hardware-independent test harness.
Include tests for:
a valid frame;
an empty payload;
an incomplete frame;
overflow;
malformed frame recovery;
multiple sequential frames;
parser reset.

Preferred local verification:

cd examples/c/event_parser
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure

When supported, also run a sanitizer build.

Example:

cmake -S . -B build-sanitize -DENABLE_SANITIZERS=ON
cmake --build build-sanitize
ctest --test-dir build-sanitize --output-on-failure

Document compiler limitations honestly.

6.3 Lua Reference Project
Gameplay Event Engine

Create:

examples/lua/gameplay_event_engine/
├── AGENTS.md
├── README.md
├── src/
│   ├── cooldowns.lua
│   ├── event_engine.lua
│   ├── logger.lua
│   ├── reward_engine.lua
│   └── sandbox.lua
├── scripts/
│   ├── events/
│   │   └── daily_rift_event.lua
│   ├── npcs/
│   │   └── gatekeeper.lua
│   └── quests/
│       └── first_rift_quest.lua
└── tests/
    ├── run_tests.lua
    ├── test_cooldowns.lua
    ├── test_event_engine.lua
    ├── test_rewards.lua
    └── test_sandbox.lua

Functional requirements:

Use local modules.
Avoid uncontrolled globals.
Support event registration.
Support event conditions.
Support reward resolution.
Support cooldown checks.
Support safe error handling with pcall.
Provide a restricted sandbox for untrusted gameplay scripts.
Use an allowlist.
Demonstrate restricted access to dangerous functions.
Include tests for:
event registration;
condition success;
condition failure;
reward lookup;
cooldown active;
cooldown expired;
script error isolation;
blocked unsafe global access.

Preferred local verification:

cd examples/lua/gameplay_event_engine
lua tests/run_tests.lua

If luacheck is installed, also run:

luacheck .

If Lua or luacheck is unavailable, document that verification as BLOCKED. Do not pretend it passed.

6.4 C++ Reference Project
Modular Gameplay Core

Create:

examples/cpp/modular_gameplay_core/
├── AGENTS.md
├── README.md
├── CMakeLists.txt
├── include/
│   └── gameplay/
│       ├── component.hpp
│       ├── entity.hpp
│       ├── event.hpp
│       ├── event_bus.hpp
│       ├── health_component.hpp
│       ├── result.hpp
│       ├── script_runtime.hpp
│       └── lua_runtime.hpp
├── src/
│   ├── entity.cpp
│   ├── event_bus.cpp
│   ├── health_component.cpp
│   ├── lua_runtime.cpp
│   └── main.cpp
└── tests/
    ├── test_entity.cpp
    ├── test_event_bus.cpp
    ├── test_health_component.cpp
    └── test_result.cpp

Functional requirements:

Use modern C++20-compatible code.
Use RAII.
Use explicit ownership.
Prefer std::unique_ptr where exclusive ownership is correct.
Avoid raw owning pointers.
Use composition for gameplay features.
Implement an event bus.
Implement a basic entity.
Implement a health component.
Implement a small result type or structured error mechanism.
Add a script-runtime abstraction.
Prepare optional Lua integration.
Keep the baseline C++ build functional even when Lua development headers are unavailable.
Enable the Lua adapter only when the required dependency is detected.
Include tests for:
adding components;
component updates;
event publication;
event subscription;
health reduction;
health floor behavior;
result success;
result error.

Preferred local verification:

cd examples/cpp/modular_gameplay_core
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure

When supported, also run:

cmake -S . -B build-sanitize -DENABLE_SANITIZERS=ON
cmake --build build-sanitize
ctest --test-dir build-sanitize --output-on-failure

Document whether Lua integration was enabled, disabled, verified, or blocked.

6.5 Integrated Reference Project
Cross-Language Second Brain Demo

Create:

examples/integrated/second_brain_reference/
├── README.md
├── contracts/
│   ├── event-contract-v1.json
│   ├── event-contract-v1.schema.json
│   └── README.md
├── fixtures/
│   ├── valid-event.json
│   └── invalid-event.json
└── scripts/
    └── smoke_test.py

The integration documentation must explain this architecture:

C embedded-style event parser
        |
        v
serialized event contract
        |
        v
Python control plane and knowledge API
        |
        v
C++ modular gameplay core
        |
        v
Lua gameplay rules

Add a Mermaid diagram.

The integration project must:

define a versioned JSON event contract;
validate required fields;
explain compatibility rules;
explain error boundaries;
explain ownership boundaries;
explain logging boundaries;
include valid and invalid fixtures;
include a Python smoke-test script;
run all available example-project checks;
clearly mark unavailable toolchains as BLOCKED;
fail when an available project fails;
avoid external network calls;
avoid production credentials.

Preferred command:

python scripts/run_all_checks.py
7. Add Validation Scripts

Create:

scripts/validate_docs.py
scripts/check_local_links.py
scripts/check_placeholder_content.py
scripts/run_all_checks.py
7.1 validate_docs.py

Validate Markdown files under:

docs/codex-second-brain/

Check:

required front matter exists;
required fields exist;
language values are allowed;
level values are allowed;
last_verified is present;
major files are not empty;
headings are present;
local documentation links resolve where applicable.
7.2 check_local_links.py

Check repository-local Markdown links.

Ignore:

external HTTP URLs;
anchor fragments when robust anchor validation is unavailable;
intentionally documented example paths when clearly marked.

Fail on broken repository-local file paths.

7.3 check_placeholder_content.py

Detect shallow or duplicated documentation.

Check for:

repeated generic paragraph bodies;
files that contain only a title and one sentence;
placeholder phrases such as:
TODO
TBD
coming soon
defines production rules
add content here
suspiciously short production chapters;
identical code examples copied into unrelated chapters.

Use reasonable thresholds.
Avoid false positives where possible.
Document the limitations of heuristic detection.

7.4 run_all_checks.py

Run all applicable checks:

documentation validators;
Python tests and quality gates;
C configure, build, and tests;
Lua tests when Lua exists;
C++ configure, build, and tests;
optional sanitizer builds where available;
integrated smoke tests.

Return a non-zero exit code when an available required gate fails.

Print a readable summary:

PASS
FAIL
BLOCKED
SKIPPED

Do not silently swallow failures.

8. Add CI/CD Quality Gates

Create:

.github/workflows/ci.yml

Use GitHub Actions.

Run on:

push
pull_request

Include jobs for:

documentation validation;
Python linting, formatting, typing, and tests;
C build and tests;
Lua tests and linting;
C++ build and tests;
integrated smoke test.

Use an Ubuntu runner unless another runner is clearly justified.

Install only necessary dependencies.

Prefer stable, explicit tool installation.

Do not deploy.

Do not require secrets.

Do not invoke external production APIs.

The CI workflow must fail when required checks fail.

Document local equivalents in:

docs/codex-second-brain/11-evaluations/quality-gates.md
docs/codex-second-brain/07-architecture/ci-cd.md
9. Complete Cross-Language Documentation

Rewrite and complete every file under:

docs/codex-second-brain/06-cross-language/

Cover:

Python and C++ boundaries;
Lua embedding in C++;
C and C++ interoperability;
C ABI concepts;
JSON contracts;
versioned message formats;
REST boundaries;
WebSocket concepts;
message-queue concepts;
file-based configuration;
direct calls versus process boundaries;
exception translation;
error-code translation;
memory ownership;
lifetime rules;
encoding;
ABI stability;
API stability;
serialization;
backward compatibility;
testing boundaries;
logging boundaries;
security boundaries.

Include Mermaid diagrams and decision tables.

Explicitly explain:

Use Python and C++ together when ...
Use C++ and Lua together when ...
Use C instead of C++ when ...
Use JSON or REST when ...
Use direct bindings when ...
Avoid direct bindings when ...
10. Complete Architecture Documentation

Rewrite and complete every file under:

docs/codex-second-brain/07-architecture/

Cover:

modular monolith versus services;
clean architecture;
dependency rules;
configuration management;
logging;
observability;
database strategy;
SQLite;
PostgreSQL;
MongoDB;
migrations;
error taxonomy;
testing strategy;
CI/CD;
deployment checklist.

Include:

trade-offs;
decision tables;
failure modes;
Mermaid diagrams;
concrete examples;
references to executable projects;
production checklists.

Do not claim that microservices are always better.
Prefer the simplest architecture that satisfies the requirements.

Create at least one Architecture Decision Record using:

docs/codex-second-brain/10-templates/ADR.template.md

Store it under:

docs/codex-second-brain/07-architecture/adr/

Recommended ADR:

0001-reference-project-layout.md
11. Complete Security Documentation

Rewrite and complete every file under:

docs/codex-second-brain/08-security/

Cover:

secret management;
.env rules;
secret rotation;
least privilege;
input validation;
output encoding;
authentication concepts;
authorization concepts;
dependency security;
logging without data leaks;
incident response;
safe configuration;
safe test fixtures;
sandboxing;
Lua script isolation;
Python API validation;
C buffer safety;
C++ ownership safety;
CI safety;
supply-chain awareness;
redacted security reporting.

Include language-specific secure-coding checklists.

Add a repository-level security checklist that future agents can apply before opening a pull request.

Never include real credentials.

12. Complete Templates

Expand the files under:

docs/codex-second-brain/10-templates/

Ensure they are actually usable.

Include:

AGENTS.second-brain.template.md
README.template.md
ADR.template.md
bug-report.template.md
feature-spec.template.md
code-review-checklist.md
.env.example.template

The code-review checklist must include:

correctness;
tests;
failure cases;
security;
secrets;
logging;
ownership;
memory lifetime;
performance;
documentation;
migration risk;
rollback;
compatibility;
CI status.
13. Complete Exercises and Evaluation

Rewrite and complete every file under:

docs/codex-second-brain/11-evaluations/

Create meaningful exercises for each language.

Use levels:

FOUNDATION
INTERMEDIATE
ADVANCED
PRODUCTION

For each language, include:

conceptual questions;
code-reading exercises;
debugging tasks;
implementation tasks;
refactoring tasks;
security-review tasks;
mini-project extensions;
realistic production scenarios.

Create actual solutions in:

docs/codex-second-brain/11-evaluations/exercise-solutions.md

Solutions must include:

explanation;
code where appropriate;
edge cases;
testing guidance;
links to relevant chapters;
clear NOT VERIFIED labels where execution was not performed.

Create a skills matrix with measurable criteria.

A score must not depend only on theoretical knowledge.

Evaluate:

implementation ability;
debugging;
testing;
architecture reasoning;
security awareness;
code review;
documentation;
production readiness.
14. Curate Sources Properly

Rewrite and complete:

docs/codex-second-brain/12-sources/official-sources.md
docs/codex-second-brain/12-sources/further-reading.md

Use current sources.

Prioritize primary sources.

Recommended categories:

Python
official Python documentation;
Python tutorial;
standard library docs;
venv;
asyncio;
sqlite3;
packaging guidance;
Flask official documentation;
pytest official documentation;
Ruff official documentation;
mypy official documentation.
C
ISO or WG14 references where accessible;
compiler documentation;
sanitizer documentation;
CMake documentation;
clearly labeled secondary references where official explanatory resources are insufficient.
Lua
official Lua manual;
official Lua reference material;
Lua C API documentation;
Lua version guidance.
C++
ISO C++ references;
WG21 references where useful;
C++ Core Guidelines;
compiler documentation;
CMake documentation;
sanitizer documentation;
clearly labeled secondary references such as cppreference when appropriate.
Security
OWASP Top Ten;
OWASP Cheat Sheet Series;
relevant official dependency and tool documentation.

For each resource, state:

purpose;
level;
free or paid;
primary or secondary source;
recommended stage in the learning roadmap.

Do not invent version numbers.
Verify version-sensitive claims when network access is available.
When network access is unavailable, state that version verification is blocked.

15. Update the Root README

Rewrite the root:

README.md

It must explain:

repository purpose;
start location;
documentation structure;
executable example projects;
local verification command;
CI workflow;
secret-safety rule;
how future Codex agents should use AGENTS.md;
completion status;
known limitations.

Include a quick-start section:

python scripts/run_all_checks.py

Include links to:

docs/codex-second-brain/README.md
docs/codex-second-brain/00-system/navigation.md
docs/codex-second-brain/00-system/learning-roadmap.md
docs/codex-second-brain/11-evaluations/quality-gates.md
docs/codex-second-brain/00-system/final-verification-report.md
16. Verification Requirements

Create:

docs/codex-second-brain/00-system/final-verification-report.md

The report must include:

1. Date
2. Environment summary
3. Files created
4. Files updated
5. Commands executed
6. Commands passed
7. Commands failed
8. Commands blocked
9. Toolchains unavailable
10. Security checks
11. Documentation checks
12. Known limitations
13. Remaining backlog
14. Final completion statement

Use precise labels:

CREATED
UPDATED
VERIFIED
NOT VERIFIED
BLOCKED
SKIPPED
RECOMMENDED NEXT STEP

Do not state that the repository is complete merely because files exist.

A feature is VERIFIED only when its command passed.

A feature is BLOCKED when the environment prevented execution.

A feature is NOT VERIFIED when implementation exists but execution was not performed.

17. Mandatory Commands

Run as many of the following commands as the environment supports.

Documentation
python scripts/validate_docs.py
python scripts/check_local_links.py
python scripts/check_placeholder_content.py
Python
cd examples/python/knowledge_ingestion_api
python -m pip install -e ".[dev]"
python -m pytest -q
ruff check .
ruff format --check .
mypy src
cd ../../..
C
cd examples/c/event_parser
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
cd ../../..
Lua
cd examples/lua/gameplay_event_engine
lua tests/run_tests.lua
luacheck .
cd ../../..
C++
cd examples/cpp/modular_gameplay_core
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
cd ../../..
Integrated
python scripts/run_all_checks.py

Where appropriate and supported, add sanitizer builds for C and C++.

If a tool is unavailable:

do not hide the issue;
record the missing tool;
mark the related step as BLOCKED;
keep the code buildable and document how to run the check locally.
18. Acceptance Criteria

The task is complete only when all of the following are true.

18.1 Structure
 Root AGENTS.md exists.
 .gitignore exists and excludes sensitive and generated files.
 CI workflow exists.
 All existing documentation sections are preserved or intentionally improved.
 New executable examples exist under examples/.
 Validation scripts exist under scripts/.
18.2 Documentation
 Python chapters are topic-specific and complete.
 C chapters are topic-specific and complete.
 Lua chapters are topic-specific and complete.
 C++ chapters are topic-specific and complete.
 Cross-language documentation is complete.
 Architecture documentation is complete.
 Security documentation is complete.
 Evaluation files contain real exercises and solutions.
 Sources are curated.
 Local links resolve.
 Placeholder-content validation passes.
 Duplicate generic content has been removed.
18.3 Executable Projects
 Python Knowledge Ingestion API exists.
 Python tests exist.
 C event parser exists.
 C tests exist.
 Lua gameplay event engine exists.
 Lua tests exist.
 C++ modular gameplay core exists.
 C++ tests exist.
 Integrated smoke test exists.
 Versioned JSON contract exists.
18.4 Quality Gates
 Documentation validation passes.
 Link validation passes.
 Placeholder-content validation passes.
 Python tests pass where the toolchain exists.
 Python linting passes where the toolchain exists.
 Python type checking passes where the toolchain exists.
 C build passes where the toolchain exists.
 C tests pass where the toolchain exists.
 Lua tests pass where the toolchain exists.
 Lua linting passes where the toolchain exists.
 C++ build passes where the toolchain exists.
 C++ tests pass where the toolchain exists.
 CI workflow is syntactically valid.
 Integrated checks pass or blocked items are documented honestly.
18.5 Security
 No real secrets were added.
 No .env values were exposed.
 Safe placeholders are used.
 Logging avoids credentials.
 Input validation exists in executable examples.
 C bounded-buffer behavior is tested.
 Lua sandbox restrictions are tested.
 C++ ownership rules are documented and tested.
 Security checklist is complete.
18.6 Reporting
 Implementation audit exists.
 Final verification report exists.
 Commands and outcomes are recorded.
 Blocked steps are explicit.
 Known limitations are explicit.
 Remaining backlog is explicit.
 No unverified claim is presented as verified.
19. Anti-Shortcut Rules

The following behaviors are explicitly forbidden:

- Creating dozens of files containing only one sentence.
- Copying the same generic chapter body into unrelated files.
- Replacing detailed implementation with bullet-point promises.
- Claiming that tests passed without running them.
- Claiming production readiness because files exist.
- Adding real secrets.
- Reading or printing .env values.
- Skipping tests silently.
- Hiding unavailable tools.
- Creating CI that deploys.
- Introducing unnecessary dependencies.
- Pretending Unreal Engine compilation occurred when Unreal is unavailable.
- Leaving exercise-solutions.md as an empty promise.
- Leaving security documents as one-line reminders.
- Stopping after the audit.
- Stopping after Python unless the environment genuinely prevents further progress.

When blocked, complete the maximum safe subset and document the exact continuation point.

20. Implementation Order

Execute the work in this order.

Phase 0 — Audit and Rules
Inspect repository.
Create branch.
Add root AGENTS.md.
Add or improve .gitignore.
Create implementation audit.
Identify placeholders and duplicates.
Commit.
Phase 1 — Validation Foundation
Add documentation validators.
Add placeholder detector.
Add local-link checker.
Add aggregate check runner.
Add tests for validation scripts where useful.
Commit.
Phase 2 — Python
Implement Python reference project.
Run Python tests and gates.
Rewrite Python documentation.
Add Python exercises and solutions.
Commit.
Phase 3 — C
Implement C parser.
Run C build and tests.
Rewrite C documentation.
Add C exercises and solutions.
Commit.
Phase 4 — Lua
Implement Lua event engine.
Run Lua tests where available.
Rewrite Lua documentation.
Add Lua exercises and solutions.
Commit.
Phase 5 — C++
Implement C++ gameplay core.
Run C++ build and tests.
Add optional Lua adapter.
Rewrite C++ documentation.
Add C++ exercises and solutions.
Commit.
Phase 6 — Integration
Add versioned JSON contract.
Add fixtures.
Add integrated smoke tests.
Rewrite cross-language documentation.
Commit.
Phase 7 — Architecture and Security
Expand architecture documents.
Expand security documents.
Expand templates.
Add ADR.
Commit.
Phase 8 — CI and Evaluation
Add GitHub Actions CI.
Complete evaluation files.
Complete quality-gate documentation.
Run repository-wide checks.
Commit.
Phase 9 — Final Review
Run all available checks again.
Run placeholder detector.
Run link checker.
Review changed files.
Update root README.
Create final verification report.
Commit.
21. Progress Reporting

After each phase, print:

## Phase X Completed

### Created
- `path/to/file`

### Updated
- `path/to/file`

### Commands Executed
```bash
...
Verified
PASS: ...
Blocked
BLOCKED: ...
Reason: ...
Security Review
...
Remaining Work
...
Next Phase
...

Keep progress reports concise but accurate.

Do not stop after producing a report. Continue to the next phase.

---

# 22. Final Response Format

At the end of the task, provide:

```markdown
# Codex Second Brain Final Implementation Summary

## Branch
`codex/finalize-second-brain`

## Overall Status
`COMPLETE`, `PARTIALLY COMPLETE`, or `BLOCKED`

## What Was Implemented
...

## Executable Projects
...

## Documentation Completed
...

## Tests and Quality Gates
| Area | Command | Result |
|---|---|---|
| Documentation | `python scripts/validate_docs.py` | PASS / FAIL / BLOCKED |
| Links | `python scripts/check_local_links.py` | PASS / FAIL / BLOCKED |
| Placeholders | `python scripts/check_placeholder_content.py` | PASS / FAIL / BLOCKED |
| Python | `python -m pytest -q` | PASS / FAIL / BLOCKED |
| C | `ctest --test-dir build --output-on-failure` | PASS / FAIL / BLOCKED |
| Lua | `lua tests/run_tests.lua` | PASS / FAIL / BLOCKED |
| C++ | `ctest --test-dir build --output-on-failure` | PASS / FAIL / BLOCKED |
| Integrated | `python scripts/run_all_checks.py` | PASS / FAIL / BLOCKED |

## Security Review
...

## Blocked Items
...

## Known Limitations
...

## Remaining Backlog
...

## Final Verification Report
`docs/codex-second-brain/00-system/final-verification-report.md`

## Recommended Pull Request Title
`Finalize Codex Second Brain with executable multi-language reference projects and verified quality gates`

## Recommended Pull Request Description
...

Be honest.

Do not use the word COMPLETE unless every mandatory acceptance criterion is either:

verified successfully; or
clearly documented as blocked by an unavailable environment capability without leaving the implementation itself unfinished.
23. Start Now

Begin immediately with Phase 0.

Do not merely explain what you intend to do.

Inspect the repository, create the branch, add the audit, create the real root AGENTS.md, and continue through the implementation phases until the acceptance criteria are satisfied or an actual environment limitation blocks a specific verification step.
:::

Der Prompt lässt Codex bewusst keine Ausweichroute über weitere Platzhalter. Eine sinnvolle Ergänzung nach der ersten Ausführung ist nur dann nötig, wenn Codex wegen eines Sitzungs- oder Toolchain-Limits einzelne Phasen als BLOCKED dokumentiert. In diesem Fall kannst du den nächsten Lauf mit folgendem kurzen Fortsetzungsauftrag starten:
