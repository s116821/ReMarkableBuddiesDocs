# Consume strict package inputs

## Why

The strict producer now freezes both target builds independently, but the APK
builder always recompiles them. Packaging must reuse an independently accepted
completion receipt without treating arbitrary JSON as build provenance.

## What Changes

- Add an explicit finite receipt consumer and share the existing generation and
  separate public-key-only observation tail with the original build-based CLI.
- Bind retained bytes to an external receipt digest, original producer, actual
  release source and full independent SDK proof; keep original build metadata.
- Preserve pinned tooling, resident bundle, isolated ephemeral fixture signing,
  bounded owned cleanup and not-qualified completion.

## Impact

Buddy release helpers and focused host controls; central package-build-inputs
contract. No automatic workflow, target rebuild, production signing, publication,
installation or device qualification follows from source delivery.
