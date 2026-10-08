# Portable selected maintenance

This implements the accepted REM-42/52 owned-data maintenance requirements in
bounded increments. SCRAPPY owns storage; Main retains domain decoding, historical
intent semantics and native admission. The first increment is verified export and
offline inspection, independent of the unfinished domain projector/admission.
Restore/migration and runtime worker integration remain disabled where their actual
activation policy is not implemented. This is part of the unfinished linked delivery.

## Archive and validation increment

Reuse the existing manifest plus content-addressed objects backup layout. Legacy
format1 exports/restore retain their behavior. Explicit `Store::export_selected`
produces format2 with an optional selected-history descriptor; ordinary format1
export continues refusing selected stores. A complete `backup.json` marker is written
last, only after required bytes and metadata have been staged and validated. A
destination must be new and cannot overlap data/cache/credential roots.

The descriptor records original actor/generation, the supported actor/generation
feature marker, and original current selection transaction ObjectRefs. Archive
objects include exact original transaction/history bytes reachable from each current
head, all referenced winner/retained manifests and immutable record/media objects,
and unrelated ordinary committed scopes. Hash links, operation identity/depth,
scope/generation, causal closure, namespaces and media coverage are checked. Orphan
staging is not accepted history and is not exported. Existing bounds apply to the
whole archive metadata/inventory as well as each selection chain; capacity refuses
instead of dropping history or receipts.

The archive inventory/manifests and total reachable selection receipt count each
have a 4096-item limit. Selection metadata together and unique encoded envelope
bytes together each have an 8 MiB limit; each envelope is limited to 1 MiB. Media
uses the existing streamed per-object limit. Inspection also applies these bounds
to legacy archives; legacy export/restore retain their existing capacity behavior.
An over-capacity inspection/export refuses explicitly rather than reporting a
partial history as complete. These are the current offline library capacities,
not a promise that every otherwise valid legacy archive fits the inspector.

`Store::inspect_backup` is offline/read-only and validates both supported formats.
It returns sanitized counts and media completeness, not configuration secrets or
live tokens. Unknown fields/formats/features, collisions, missing/hash-mismatched
objects, false completeness, extra inventory and incompatible selections refuse.
Stored envelope ObjectRefs refer to exact raw bytes; validation never substitutes
reserialization digests. Selection transactions and source identity are historical
evidence, not current membership, admission or an instruction to replay effects.

This increment excludes configuration rather than serialize device paths,
connections, group membership, runtime settings or credentials. Portable
configuration requires its separate allowlist; its absence is explicit. Only
declared Buddy-owned manifests/objects and selected metadata are copied. No native
document/page/ink tree, cache, diagnostics, binaries, locks, status, account tokens
or source credentials are copied. Domain ownership/strict payload semantics remain
the domain owner's separate validation boundary.

## Remaining activation policy

Format2 inspection cannot activate a Store selection or mint a `SelectionToken`.
Existing `restore` refuses selected archives and selected targets before changing
CURRENT, actor, selected membership or configuration. A future maintenance restore
must stage an additive generation, preserve originals/unrelated scopes and rollback,
establish new local identity, retain original immutable history/pins as evidence, and
keep imported intent/binding state non-authoritative. It cannot copy source group
membership/settings or resume a source device's output. The domain adapter must
define historical receipt/latch intake and native verification before that path can
be enabled; this dependency does not block archive custody/validation.

Registered selected migrations similarly require an explicit transformation policy
that preserves original immutable receipts/history and their meaning across a new
generation. Unsupported paths retain current refusal. No format number alone
authorizes transformation. These are data formats, independent of Git-tag releases.

## Qualification

Use real disposable Store fixtures with winner plus retained admitted evidence,
historical settlement, several accepted transactions, unrelated selected/local data,
tombstones and exact noncanonical bytes. Export, inspect, reopen and compare original
references and readable included media. Intentionally omitted media remains partial;
missing promised media refuses. Corrupt/missing chain links, unknown feature/schema,
wrong scope/generation, conflicting inventory and failed staging never publish a
complete marker or mutate source/target state. Legacy backup fixtures must still pass.
Successful inspection is not restore, provider or native qualification.

The storage fixture module `storage::selection::publication_tests::portable_tests`
exercises exact history/head bytes, reverse causal record order, retained settlement
with media, a second selected scope, unrelated ordinary tombstones, source reopen,
configuration/credential/native/orphan exclusion, format2 restore refusal, each
export publication fault, mutated format/origin/inventory/manifest/feature/head,
missing promised versus deliberately omitted media, legacy shape/restore, owned
root/symlink/existing destination refusal, and aggregate metadata capacity refusal.
Run `cargo test --locked --all-features --lib portable_` for this bounded fixture
set, followed by the repository's full `cargo test --locked --all-features` and
`cargo clippy --locked --all-targets --all-features -- -D warnings` checks. The
report includes format, counts and completeness only; an archive remains evidence,
and a successful inspection does not bypass the remaining activation policy.

The REM-42 prior-art requirement was refreshed against [RCU's official overview](https://www.davisr.me/projects/rcu/):
offline snapshots, compatibility state and recovery-oriented safeguards inform the
maintenance boundary. RCU's device-wide snapshots/firmware/native-document features
are outside this Buddy-owned archive. Existing Store filesystem/lease/content-hash
primitives are reused; no RCU code or account access is imported.
