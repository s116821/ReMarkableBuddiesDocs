# Prepared logical deletion of one ordinary historical conversation

## Why
The historical Ledger already atomically tombstones a conversation root and its
optional historical page binding, retaining source images, history and export
associations. External maintenance has no original-bound prepare/apply/status
interface. Aggregate owned-data inspection grants no logical-liveness or deletion
authority. Selective owned-data management needs a deliberate, reference-safe path.

## What changes
Add a separate Linux-only conversation-maintenance CLI and closed version-one
report for inspect/prepare/apply/status of one explicitly selected ordinary
schema-one conversation. Require observed inactive fixed Buddy unit, existing
Store custody, ordinary local mode, explicit settled-exchange eligibility and exact
original intent. Reserve publication/reconciliation headroom and cumulative recovery
work; recognize an exact historical receipt independently of later current history.
Publish only root/optional binding tombstones and one historical receipt together.
Expose no text, source images, native identifiers, arbitrary paths or remote action.

## Scope and delivery
One Buddy/central Docs pair. This is logical local deletion, not physical purge,
space reclamation, remote deletion or current native authority. Selected storage,
schema-two domain records, unfinished/uncertain effects, service changes, Manager
consumer code and protected Reader/Writer paths remain excluded. A bound ordinary
schema-one historical binding may be tombstoned; its native page remains intact.
Concrete precode and implementation/coverage reviews were completed before this
own canonical sync/archive. Exact-current source/fixture/CLI and normal delivery CI
passed. Final composed review and actual Docs-first delivery/main/publication
remain separate observed gates; no native or integrated completion follows.
