# Shared saved-configuration consumer contract (proposed)

Producer wire is exactly Docs71 at2a320181739e0d598ed830d31329214e036df646,
[inspect-saved-configuration/contract.md](https://github.com/s116821/ReMarkableBuddiesDocs/blob/2a320181739e0d598ed830d31329214e036df646/openspec/changes/inspect-saved-configuration/contract.md).
Full independent review5584589306 and explicit consumer agreement6290198071 are
read/accepted as design. This consumer contract is precode, not an available API.
Main owns the producer and actual specimens. Existing Manager source3c789a0 is
shipped; no source body changes precede this consumer's independent review.

## Exact public capability
One optional `ManagerHost.inspectSavedConfiguration(request)`; one authenticated
loopback POST `/manager-saved-configuration`; one exact-arity1 authorized main-frame
IPC `manager:inspectSavedConfiguration`. Exact request:
`{connection_id:LOWER_HEX64,boot_id:NONNIL_LOWER_UUID}`.
No action/selector/config path/operation/digest/field/filter/command/root/identity
or stdin is accepted. Request is canonical strict JSON <=256 UTF8 bytes; duplicates,
invalid UTF8, extras, wrong verb/origin/session/route/query and input overflow refuse
before dispatch. Use existing wired observation UUID/digest rules. Helper retains
exact loopback Host/Origin/HttpOnly SameSite session checks; Electron retains
sender/main-frame/UI URL authorization and sandbox/preload isolation.

Observed original connection+boot must match host lastObservation before dispatch
and private before/after wired samples. UI probe admission uses the existing
known-model/nonconflicting firmware/architecture profile, not an installed release
threshold or native/package qualification. Unknown/old command support refuses,
never falls back to reading arbitrary files or the running Buddy API.

Exact public outer result:
`{contract_version:1,status:OBSERVATION_STATUS,observation:SAMPLE_OR_NULL,
saved_configuration:{status:reported|unsupported|unavailable,view:VIEW_OR_NULL}}`.
The nested status describes transport/protocol capability. A reported view requires
outer observed status and the exact original target/boot. Nonreported view is null.
VIEW is exactly `{status:PRODUCER_STATUS,runtime_activation:"unverified",
snapshot:REDUCED_SNAPSHOT_OR_NULL}`. Producer statuses are only ok, unavailable,
invalid-input, unsupported; non-ok snapshot is null. Do not invent incomplete,
partial, effective, active, default-success, disk-reload or mutation outcomes.

REDUCED_SNAPSHOT exact keys:
`{schema_version:1,byte_basis:"saved-file-bytes",validation_basis:"typed-values-only",
declared_roots_validated:false,fields:EXACT25_FIELDS,unsupported:EXACT_GAPS}`.
It contains NO config_sha256 or raw report. Public view and outer schema deny
extras recursively; a private report or digest offered to HTTP/IPC/controller
refuses rather than being interpreted as an alternate public shape. Public response
is <=32768 UTF8 bytes; reader bounds it before JSON decoding and controller validation.

## Exact scalar/origin validation
Pin the producer's complete synthetic default matrix from the exact immutable
contract; it is not actual CLI evidence. Twenty-five flat literal field names,
not nested maps; each value is exactly `{origin:default|declared|declared-null,value}`.
Validate exact booleans, nullability, enums, safe integers and inclusive ranges;
never round, truncate or coerce. Validate all fields or refuse the whole view.

- Default origin requires its pinned current value. The actual media ceiling is
  268435456 (256MiB), with default33554432; poll5..3600/default60, batch1..128/default32.
- Only the nine actual Option leaves admit declared-null. The six presence-only
  Options are false for default/declared-null and true for declared. Trigger corner,
  log level and debug flag are null for default/declared-null; declared means the
  producer's nonnull enum/boolean value. Other nonoptional fields cannot be null.
- All three path values are true and have one shared origin: default together if
  paths was omitted, or declared together for its complete required object. Never
  declared-null or mixed child origins. This establishes no path validity/existence.
- Personalization text-present and text_bytes have the same default/declared origin;
  presence equals bytes>0, with default false/0. Byte length0..16384 is not text,
  a text digest or effective personalization. Declared enabled with empty text is valid.
- Memory enabled or selection-present implies profile-present. sync.create_new=true
  implies collection-present. Refuse enabled sync with selected memory,
  or enabled sync plus enabled memory and subject-memory namespace.
- Namespace strings are unique, lexically sorted members of the exact five-name
  allowlist, at most5. Do not use Rust enum ordering. Unsupported settings preserve
  the producer's exact fixed ordered six-string array and remain explicit gaps.

No raw model/endpoint/reference/path/identity/group/binding/pins/personalization
text enters renderer state, storage, logs or errors. The host validates the private
raw digest shape but never hashes reduced fields to impersonate it, returns it,
persists it or grants later write/CAS authority. No provider credential resolution,
environment interpretation, declared-root probing or Store admission is introduced.
Existing protected SSH transport prerequisites remain separate and unchanged.

## Private transport and reduction
Internal observer action `saved-configuration`, fixed sibling
`host/saved_configuration_transport.py`, uses existing trusted Linux/Windows wired
callbacks and config/identity custody. Python stdin carries ONLY the bounded private
host connection/boot request; it is not CLI input. The remote fixed command is:

```text
/usr/bin/env -i HOME=/home/root PATH=/opt/bin:/usr/bin:/bin REMARKABLE_BUDDIES_CONFIG=/home/root/.config/remarkable-buddies/config.json /opt/bin/reader-buddy --configuration-operation inspect
```

No remote stdin bytes, --configuration-input, --config, supplied argv or staging.
Remote inspect never waits for EOF. Fixed one-shot path; no service/model/provider
contact or automatic retry. Python verifies boot before command and full existing
wired sample/route/trust afterward; zero exit and exactly one complete UTF8 JSON
line including LF are required. Recursive duplicates, NaN/invalid encodings, extra
trailing material, partial output, caps, exit or deadlines refuse the complete view.
Stderr is discarded, never reflected.

Limits: public/private request256; raw CLI stdout131072 including LF; stderr8192;
private child envelope139264; public result32768 bytes. Preserve existing channel2s,
collection8s, Python12s, Node13s and browser14s deadlines, all below the producer's
at-most30s ceiling. Do not enlarge shared observer timeouts. If Python serialization
would exceed a child cap, refuse rather than truncate or weaken validation.

Private Python/Node envelope uses the same outer observation but
`saved_configuration:{status,report:RAW_PRODUCER_REPORT_OR_NULL}`. Raw producer report
has exactly its five published keys; successful snapshot includes the private
config_sha256. Node strictly validates it, removes only that private digest and
unneeded fixed report_version/operation, then validates the public view. Unsupported
positive future report version maps to capability unsupported with null view; other
unknown schema/status/shape refuses with no partial field list. Unsupported CLI
exit2/126/127 also maps unsupported; other transport failures unavailable. A complete
non-ok producer report retains its exact status, never a successful default matrix.

## Host and controller lifetime
Register `inspectSavedConfiguration` as external maintenance in the existing
MemoryForgetHost wrapper BEFORE any child or inspection I/O. Keep the original
observer as method receiver: internal run cancellation must not accidentally create
a second external protocol. Ready forget references invalidate; possible-dispatch
unknown retains original private bytes and receipt-only semantics. The settings
snapshot cannot settle, replace, rearm or retry an uncertain mutation.

Use the existing observer cancellation generation and original target/boot. Capture
the launch generation after run's own cancellation, reject stale completions before
reduction and before releasing public output, and recheck after any awaited validation.
Do not rely on renderer suppression alone. Explicit observe/refresh/cancel/disconnect
and competing maintenance invalidate pending settings reads even with identical IDs.

Navigation currently invalidates only the forget epoch. For this new read, main
browser document GET `/`, `/preview/`, `/preview/index.html` and Electron main-frame
navigation will use the wrapped observer's existing external cancel path, so it
also invalidates pending observation-generation results. Resource fetches/subframes
are not document refreshes. Existing possible-dispatch forget uncertainty survives
this stronger local-wait cancellation; it never asserts remote rollback. This
intentional shared navigation wiring is reviewed here before code.

A shared SavedConfigurationController exposes only busy/status/reduced view. Explicit
inspection clears old view, pauses ordinary connection polling, then rechecks the
same displayed observation generation before calling the host. It validates the
returned public shape and generation again before publishing. Clearing on refresh,
new inspection, cancel, disconnect, target change or component disposal suppresses
all late results, including same-ID reads. No automatic startup inspection or data
persistence/cache is added. Known probe admission never proves installed support.

Serialize cancel through the existing ConnectionController.pause cancellation queue,
not an independent fire-and-forget host.cancel. Hold local pending state until cancel
completion; new inspect/read waits behind that queue. A manual refresh/disconnect
can clear the local view without letting an old queued cancellation kill a later
read. Controls and regressions must cover that ordering.

## Shared UI and evidence
Panel title Saved configuration. Explicit Inspect saved configuration and Cancel
inspection actions with text-only pending feedback; no new spinner/background loop.
Show setting, safe value/presence and exact declared/default/explicit-null origin,
grouped into model/basic, path declarations, memory/sync, personalization summaries.
No raw JSON dump. Presence false means no configured value in this saved source, not an
absent/invalid runtime credential or missing effective model. Default null never
substitutes an effective runtime default. Paths always state details withheld and
validity unchecked. Existing dedicated personalization/saved-mode controls remain
separate; no new edit, enable, provider test, credential, path browser, reload,
service, installation or mutation capability. Unsupported six settings get a
separate not-represented section, never false/default toggles.

Actual attributed producer specimens must verify original report hashes and exact
fields/origins/refusals privately, without inventing CLI evidence from the default
vector. Synthetic fault transport/SSH peers/controller races remain separate.
Verify strict parser/reduced guards, before-I/O forget invalidation and preserved
unknown bytes, cancel queue, same-ID/navigation/late-result cases, both real
HTTP/IPC paths and390/1280 responsive captures. Required ordinary Linux/Windows
source/development/retained-package checks stay inside existing jobs. Review,
canonical sync/archive and final composition with qualified producer delivery stay
in one linked own delivery; actual trees/main CI/tag/provenance are later observations.
No tablet/provider/native qualification or new worker follows from this precode.
