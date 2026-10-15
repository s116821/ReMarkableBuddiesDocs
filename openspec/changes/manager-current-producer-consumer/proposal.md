## Why
The accepted Manager download consumer and desktop packaging load hash-qualified release/policy.py and release/coordinator.py. REM-56's live producer99bde579 removed those files and exposes the same package identity predicate in release/artifacts.py. The actual existing consumer/package path must stop requiring deleted producer implementation before coordinated integration.

## What Changes
Replace only the selected identity-validator dependency in the existing bounded Manager bundle verifier. Reuse byte-identical current producer artifacts.py as a hash-qualified runtime resource, update the fixed package inventory and exercise actual current-producer ZIP fixtures. Preserve all download/ZIP/source/embedded identity/cancellation checks and ineligibility flags. Do not restore an obsolete release engine or invent another verifier.

## Scope
SCRAPPY owns the consumer adapter, its packaged resources, affected controls and guide. Root owns live release/artifacts code; Main owns Reader/runtime/OpenAI/Cargo. No producer/workflow/version/device/provider changes. Preserve accepted PR18 and all parent/physical holds on a new topic from4a9ef9b. This central active change and linked implementation are one delivery, never a separately completed plan or full REM-41/42 acceptance.
