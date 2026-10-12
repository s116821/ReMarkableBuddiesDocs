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
including wrapper/status/data/escaping. Current conflict revisions are at most
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
