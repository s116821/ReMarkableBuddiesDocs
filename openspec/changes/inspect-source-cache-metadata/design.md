# Design

## Current project facts
Current source17675f5 and canonical Docs3e3d4eb provide aggregate cache accounting
and a selected-UUID cleanup producer, but no bounded list of source-cache IDs.
The private cleanup custody reads Config plus five bounded ownership/current
headers without constructing Store or reading durable payloads. Legacy cache open
may initialize/clean staging; ordinary Store admission recovers durable history.
Neither is suitable for this observer. This is source/contract evidence, not a
claim that an installed Reader currently populates this cache.

## Decisions
Expose a separate boolean CLI flag and closed report so existing cleanup,
configuration and general inspection wires remain byte-compatible. No stdin,
filters, file path, UUID, pagination or arbitrary command input. Linux only;
non-Linux returns unsupported before Config, filesystem, leases or input reads.

Reuse private existing-only custody/known header validation, never expose an
unrecovered ordinary Store. If extracting a private header observation type is
necessary, retain existing cleanup intents/reports/status semantics, validation,
lease retention and all frozen digest vectors. Do not manufacture fake mutation
intents to implement inventory. Keep legacy Store/cache APIs unchanged.

Enumerate only normalized-sources-v1, max18 entries (owner/lock plus16slots).
Validate names, regular-file/reparse safety and apparent lengths only; do not open
any slot payload or use its own key as current-source authority. Empty/corrupt or
unsupported entry JSON can be listed as unvalidated metadata, with later selected
prepare refusing it. Unknown marker format/name/type, staging, over-capacity or
oversized slot metadata refuses rather than being skipped/adopted/cleaned.

Under both held nonblocking leases, bracket Config/root/owner/actor/current-format
and generation/namespace identity; take two sorted metadata observations and
compare every selected name, stable device/inode identity and length. Changed
observation returns conflict with no partial entries. Cooperating OS custody and
existing safe-path checks are not a hostile-filesystem or historical-identity
sandbox. Listing has no mutation/cause/freshness authority or receipt token.

## Verification
Synthetic roots only. Prove0/1/16slots,17refusal, deterministic ordering,0 and32MiB
lengths, oversized metadata, unknown/staging/reparse/marker formats and ownership,
missing/busy/replaced locks, changed bracket/metadata, output prefix failure while
both leases remain held, byte/mode/mtime preservation and no create/chmod/repair.
Deny every entry-payload and durable-history read/enumeration through an exact
known-header allowlist. Include corrupt/empty/inaccessible slot payloads to show
metadata-only admission, plus missing/poisoned durable payload directories.

Exercise actual Linux CLI and non-Linux early unsupported/no-stdin/Config controls,
strict bounded report validation, no protected sentinel echo, clean executable/tree
provenance and raw stream hashes. Retain failures and each capture's own identity.
Run all existing cleanup regression/vector controls to prove compatibility.
