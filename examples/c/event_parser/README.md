# Embedded Event Parser

C17 framed protocol parser. Frames start with `0x7E`, end with `0x7F`, and carry up to 32 bytes.

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```
