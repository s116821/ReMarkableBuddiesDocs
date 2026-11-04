# Existing custody and format boundary

Pin Buddy main b008027b378f8f06422c17d5e58ed7bb041e402b and Docs main
0813397d9530e6bcc93a6dea5207efe5fec5d58c. The existing
`storage::selection::outbox` inventory at outbox.rs:82–116 and
`Store::selected_attempt_inventory` at outbox.rs:234 are the source of truth.
They validate the bounded journal's exact record/filename, actor, schema and
request fingerprint. The result includes historical stale and withdrawn
records by design. Count the typed states only. Do not deserialize the
journal in a second CLI parser, inspect provider IDs, reauthorize records,
check current slot suitability or follow descriptor/media contents.

Use a narrowly named selected-aware existing maintenance entry over
`Store::open_existing_inner` from storage/maintenance.rs. Keep the outer
path and owner checks, exclusive existing OS lock, valid current generation
and existing in-memory index recovery. This constructs no directories,
initializes no Store, cleans no staging, and writes no capabilities.
The report object holds custody through the one serialization/write/flush
attempt and its failure or drop. The inherited admission still checks
existing Store state. The journal bounds apply to inventory reads and
the report bound applies to output.

The admitted existing formats are ordinary format 1, selected format 2
and feedback format 3 with or without admitted selected feature metadata.
This is useful to host maintenance and future Manager diagnostics on idle
Stores that still use those layouts. A complete zero is only the inventory
fact for that Store. Counts include actor-owned historical records from prior
generations, not just attempts that could be replayed on the current one.
No selected mode must be activated to inspect historical records.

## Generation 4 decision

The delivered report3 observer is a Linux-only accounting scanner.
`inspection_v3::Inspection` owns private `Access` and a read-only lock and
verifies device/inode witnesses before and after output. It never builds a
Store, and scan.rs currently treats sync/selected-outbox as an unexpected
entry. Neither the public accounting report nor the scan validates journal
content or returns a reusable typed inventory. Reusing the fd-relative
primitives in a future generation-4 journal observer is possible without
mutable adoption, but would require a new parser/access integration and
separate custody, feature-marker, budget and witness controls. Do not feed
accounting lengths or partial output into status.

V1 deliberately retains the existing maintenance opener's refusal for
format 4 and for any notebook feature marker, including interrupted
adoption. Return unsupported with null counts before touching the outbox.
The delivered generation-4 capability declaration itself says
unsupported-notebook-generation for sync. This boundary does not imply
there are no retained records on that Store. No widening of the legacy
opener, mutable notebook adoption, or change to report3 is part of V1.

## Admission and errors

Use the existing complete inventory, including filename/identity, schema,
actor, record fingerprints and state validation. Preserve existing public
Store APIs and behavior. The internal inventory may gain typed failure
classification so the new boundary can distinguish invalid journal content,
unreadable I/O and unsupported layout/limits without string matching.
Use a definitive missing-directory result for zero, preserving I/O refusal.
Enforce the existing 4096-entry and 8 MiB aggregate metadata limits while
reading the inventory. Charge the remaining bytes before a read. Existing
per-record type and scope bounds continue to apply. No partial counts follow
a later bad row. A missing configured Store is unavailable. Outer
maintenance refusal remains unsupported for a Store that cannot admit its
existing layout. Corrupt applies to journal contents that fail validation
after Store custody is admitted.

The one JSON frame contains no private diagnostic, UUID, config path,
provider binding, remote revision or stored request. With a failed writer,
return an output error and make no second attempt.
