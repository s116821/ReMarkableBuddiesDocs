# Bounded one-shot memory maintenance

Extend the existing `reader-buddy` binary in this same delivery; do not add an app,
listener, admin service, dependency or storage/sync engine. The new route is
`--memory-operation inspect|query|put|forget --memory-input FILE`. Both options
require each other and conflict with simulation/provider/model/trigger/debug and
logging overrides. Parse arguments and route maintenance before `.env`, credential
resolution, logging, sync, Workflow/device initialization or the normal loop.

Read the ordinary selected nonsecret configuration and its explicit portable memory
profile. Maintenance is an explicit operation, independent of the response-enrichment
enabled flag. It does not implicitly turn that flag on or edit configuration.
Require the existing config selected explicitly by `REMARKABLE_BUDDIES_CONFIG`;
missing selector is unavailable, not a default-root initialization or `.env` lookup.
Inspect input is a `Key`; query input is `Query`; put input is `Mutation`; forget
input is `Forget`. Use strict known JSON fields, bounded regular-file input up to
1 MiB, existing domain validators and matching configured profile before opening
the Store. Validate nil identities, expected parents, canonical claim keys and
query limits without echoing parser values, filenames or memory text on failure.

Only explicit `put` may initialize a missing empty owned Store through the existing
Store primitive. Inspect/query/forget require the existing ownership marker,
CURRENT and regular lock; missing state is unavailable, never created as empty
inspection or deletion. Normal Store opening can recover/create known metadata or
clean staging under its existing lease; these commands are not the nonmutating
inventory contract. Do not pretend read commands preserve every filesystem write.

Initialization permission is limited to an absent data root or an actually empty
directory after safe path validation. A nonempty/partly owned root missing any
identity/CURRENT/regular lock is unavailable even for put; do not repair it through
normal Store startup. Validate strict identity format/actor and nonnil CURRENT,
safe regular markers/lock, all StorePaths and configured profile before opening.
Put/forget operation UUIDs and expected parent identities/counts, full Fact/Key
validation, and nonempty forget parents are pure input preflight, not post-startup
checks. This is not an atomic guarantee against external filesystem replacement.
Fresh initialization also requires an explicit creation put with empty expected
parents; an update expecting existing revisions cannot initialize a missing Store.

For an existing lock, validate a safe regular file before any open, then perform
a nonblocking read-only preflight lock check. WouldBlock yields busy; unsupported
locking yields unsupported. Release the preflight handle before normal Store
opening. If another writer wins that gap, classify the existing Store's exact
known busy refusal as busy; expose no raw error. Never stop/retry/kill a service or
fall back to unleased reads. The domain lifetime lease still refuses selected
storage and unavailable recovered state; no sync flag can bypass that boundary.

The race classifier is exactly the trusted top-level Store lock refusal
`store is owned by another process`, reached only after successful lock preflight
and the normal Store open attempt. No substring matching on parser/user data,
arbitrary exception text or guessed operating-system messages is allowed.

Emit one JSON `report_version: 1` response with operation, fixed status and bounded
result data. Status is `ok`, `partial`, `busy`, `unavailable`, `unsupported`,
`conflict`, `invalid-input` or `failed`. Domain query status/diagnostics remain
explicit inside results; withheld-only/byte-limited is partial, not empty success.
Conflict may return only current revision UUIDs for an explicit caller refresh;
no automatic rebase. Put/forget returns transaction identity; inspection returns
bounded current envelopes including tombstones/conflicts; query returns bounded
labeled facts/diagnostics. Inspect/query intentionally disclose saved values on
stdout to the explicit requesting caller, never routine logs. Exit zero means a
report was emitted, not that status is healthy; argument syntax errors remain
Clap errors with no operation/provider execution.

Use compact JSON and bound the exact total serialized response to 8 MiB + 64 KiB,
including wrapper/status/data/escaping and the final newline. Current conflict
revisions are at most
4096 UUIDs, and their encoded result must fit the total cap. If all heads/data
cannot be represented, return unavailable with explicit incomplete indication and
no partial head refresh set. Do not silently truncate a successful result or retry
an already-published mutation after an output limit. Under these envelopes, known
operation receipts are small; inspect and query data remain bounded by their
existing domain snapshot/context limits before final response serialization.

Test actual binary subprocesses with real temporary Stores: successful offline
put/query/inspect/forget/replay, expected-head conflict, missing read state, busy
lease, selected-state refusal, unsupported/incomplete state, invalid/oversized/
unsafe JSON input, profile mismatch, private sentinels and poison `.env`. Verify
ordinary default/simulation paths and no model/device/sync invocation. Preserve
prior exact-source evidence as its own revision; verify the new committed source
and paired Docs revisions independently. Full Writer/Manager/REM-52/native and
unwaived required-check/lifecycle gates remain open.


## Selected receiving setup extension (before implementation)

Selected mode is explicit configuration containing catalog group/profile/binding
identity; it never follows from turning on the legacy sync switch. Ordinary
put/forget/inspect/query use the actual selected Provider after complete catalog
and aggregate validation. They never initialize an absent selected scope.

Add three bounded file-input values to the existing memory-operation option:

- `initialize-aggregate`: operation UUID, accepted-base digest and one complete
  Fact. Explicitly initialize a new independent global or memory-only document
  aggregate. Refuse an existing scope rather than replacing its mixed records.
- `initialize-selection`: operation UUID, accepted-base digest and complete
  registration set. Validate every already-initialized aggregate/immutable genesis
  before publishing the catalog root plus registrations. A root-only catalog is
  the explicit complete empty case. No automatic ordinary-head import.
- `register-selection`: operation UUID and registration. Validate the current
  catalog plus registered aggregate. Append absent membership preserving all
  accepted registrations; identical existing membership yields a distinct current
  adoption acknowledgment. Changed owner/genesis refuses, and adoption never
  republishes a losing fact payload.

All strict input/profile/identity/budget checks apply before Store startup where
possible. These setup operations require explicit selected configuration; default
local operation refuses them. The same regular-file, pre-runtime, privacy, lease
and output limits apply. Actual aggregate/catalog publication uses existing
selected Store primitives and common domain admission. It grants no cloud,
account/provider, selected restore, device or native permission.

This extension requires focused review before CLI implementation. Its current
catalog projection is not permission to bypass the pending generic cumulative
pre-I/O/validated-lineage seam.

Focused Sol setup review accepted the following freeze. Only explicit setup
initializers may create an absent/actually empty Store; register and ordinary
selected operations require owned existing state. Nonempty partial state is
never repaired by input validation. Pure input checks precede startup; catalog,
genesis and ownership checks honestly follow normal Store open/recovery. All
setup uses the same cumulative caps, exact configured group/profile/binding,
canonical recipes, nonnil operations and lowercase 64-hex accepted-base digest.

An existing aggregate refuses a different initializer; an exact initializer retry
returns its original receipt without replacing today's winner. Document setup
never imports/converts ordinary legacy document records. If their ownership
cannot be ruled out safely, initialization refuses; a new memory-only document
scope does not establish native document existence. Existing mixed documents
can only be registered after validating their full existing closure.

Setup manifests and envelope operation/revision identities are deterministic from
the explicit operation and input, allowing exact original bootstrap replay.
Registration retry returns an original historical acknowledgment; identical
membership adopted under another operation is explicitly `adopted`, distinct from
`replayed` and `published`. Collision or unavailable lineage never falls back to
a fresh write. A published but unregistered aggregate is an orphan with no query
membership; no automatic recovery/retry advertises it.
