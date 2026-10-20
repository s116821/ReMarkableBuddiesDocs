# Host mode commands and lifetime

## Source and ownership
Current REM36 description/all four comments and REM52 description/all74 comments
were read chronologically. Delivered mode.rs already owns choice validation,
actor/device/epoch identity, isolated namespace continuity, conditional replacement,
exact original-operation replay and mode leases. Do not duplicate that logic or
parse private mode.json. The generic storage owner must coordinate the narrow
maintenance/token seams; no implementation is started by this precode document.

## Input and operation contract
Expose `--sync-mode-operation initialize|inspect|choose`. Only choose accepts
`--sync-mode-input ABSOLUTE_FILE` or exact dash stdin. Other operations reject an
input marker before configuration/input/Store access. Choose input is one strict
JSON object `{operation,expected,choice}`: nonnil operation UUID, the original
serialized expected token `{actor,sha256}`, and existing SyncModeChoice. Validate
unknown fields, nil IDs, exact digest and existing choice syntax before opening
the Store. Input is at most16KiB; stdin requires EOF and the caller owns its
deadline/cancellation. No logging/model/device/simulation/other maintenance flags
may be combined, and the route returns before dotenv/runtime initialization.

Keep SyncModeToken's public surface Serialize-only. Add a validated crate-private
maintenance constructor for actor/digest and expose existing choice validation
inside the crate, rather than substituting today's snapshot token or adding a
public token deserializer. Stored token bytes are a conditional precondition,
not a live selection, provider or native capability.

## Existing versus explicit initialization
Inspect and choose require an already valid owned Store and retain its whole-store
OS lease through output. Reuse Store::open_existing admission/refusal behavior.
Its current generation check is format1-only, so factor a narrow crate-private
selected-aware mode-maintenance opener using the existing selected generation and
recovery validators. Preserve the public legacy opener and personalization's
existing selected-format refusal. Neither mode opener creates/repairs directories,
markers or staging. It returns no partial authority after corrupt state.

Initialize alone explicitly permits normal Store::open initialization/recovery of
configured owned roots; it returns the current unconfigured/chosen snapshot and
does not itself choose a mode or fabricate an operation receipt. Unknown/nonowned
roots remain refused. Choosing/initializing with legacy sync enabled refuses;
commands never stop a service or publisher. A Busy Store stays Busy.

## Choice, original retry and output
Pass the caller's original expected token and operation directly to set_sync_mode.
Do not retry a failed/uncertain mutation automatically. The setter intentionally
returns an exact old operation receipt before checking current token/leases;
therefore output separates `receipt` from `current_snapshot`, and distinguishes
receipt-current from historical replay by exact epoch/mode equality. A successful
old retry never claims the old mode is current. Changed replay, stale or foreign
preconditions refuse with sanitized status; uncertainty does not prove no commit.

The version1 report is one bounded JSON line, at most16KiB, with operation/status,
incomplete and activation_performed=false. Snapshots expose chosen metadata and
the conditional token, not provider qualification or runtime activation. The
report owns the Store and an ordinary or explicit current mode lease until its
single consuming write completes/fails. Original receipt and current snapshot
remain separate if an old operation is replayed after another mode choice. A
partial writer failure never appends a replacement JSON or replays a mutation.

## Ordinary runtime fence is required
Current main lacks an ordinary mode lifetime. Exposing mode choice must not let a
later normal Reader silently ignore shared/isolated choice. Add only a small
ordinary-startup admission helper and named real main lifetime, before config
snapshot, model client, Workflow or domain runtime initialization. It holds the
delivered OrdinaryModeLease plus the distinct legacy-data lease through run_loop,
allowing absent/LocalOnly mode while refusing selected generations and unsupported
explicit modes. Explicit LocalOnly with the legacy publisher enabled refuses.
No reader_runtime, memory context, selected Reader publication, Orchestrator/prompt
or model client implementation is imported. This qualifies host startup/lifetime
behavior only; existing broader Reader/model/native requirements stay open.

## Meaningful verification
Actual CLI: initialize/inspect/choose/reopen; original-token exact retries after
later mode replacement; changed/stale/foreign/nil/malformed/oversize input; stdin/
file parity; Busy and missing/nonowned/partial roots without repair; selected
format2 inspect/choice preserving all records/media/current selection; public
legacy opener/personalization still refuse that format. Byte inventories prove
inspect unchanged and choice changes only committed mode metadata.

Actual Store/writer controls: active publisher and ordinary/explicit lease denial,
mode/Store lifetime held inside the writer and released on success/partial error,
original historical receipt separate from current snapshot and no second report.
Exercise true shared/local/isolated transitions and keep their existing namespace/
outbox semantics; do not rerun unchanged historical matrices unnecessarily.

Ordinary startup helper controls prove absent/LocalOnly positive admission,
shared/isolated and selected-data refusal, held lease exclusion and later release.
Actual binary negative startup uses dummy credentials and must refuse before any
model/device constructor, without printing values. No ordinary native/live run is
claimed. Run affected memory/maintenance/routing controls, strict lint/no-default,
normal full hosted CI and independent final review. SDK/Cargo remain unchanged.
