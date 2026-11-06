# Consume strict package inputs

## Why

The strict producer now freezes both target builds independently, but the APK
builder always recompiles them. Packaging must reuse an independently accepted
completion receipt without treating arbitrary JSON as build provenance.

Preflight of the initial consumer found that it also equated historical SDK
directory metadata with the full proof captured for a later packaging operation.
Exactly the SDK Git-directory ctime changed while all other proof fields matched.
The same change is reopened to represent that observation honestly, without a
continuous-custody claim or repeating successful target builds.

## What Changes

- Add an explicit finite receipt consumer and share the existing generation and
  separate public-key-only observation tail with the original build-based CLI.
- Bind retained bytes to an external receipt digest, original producer, actual
  release source and full independent SDK proof; keep original build metadata.
- Preserve pinned tooling, resident bundle, isolated ephemeral fixture signing,
  bounded owned cleanup and not-qualified completion.
- Classify an explicitly recorded historical Git-directory ctime-only difference
  as freshly revalidated content correspondence. Preserve full historical/current
  proofs; every other identity difference refuses. Full current proof equality
  stays strict throughout each observation and the complete packaging operation.

## Impact

Buddy release helpers and focused host controls; central package-build-inputs
contract. No automatic workflow, target rebuild, production signing, publication,
installation or device qualification follows from source delivery.
