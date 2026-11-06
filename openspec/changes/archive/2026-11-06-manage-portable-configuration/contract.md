# Consumer boundary proposal

## Public bridge
One optional ManagerHost capability portableConfiguration accepts exactly one
request and returns one bounded result. Browser route is POST
/manager-portable-configuration with the existing exact loopback Host/Origin,
session cookie, JSON content type and no query checks; Electron uses one fixed
IPC name manager:portableConfiguration with existing exact sender/frame/arity
checks. No new external origin, URL navigation, arbitrary filename or filesystem
capability is exposed. Reject recursive duplicate members, unknown fields,
invalid UTF8/surrogates, invalid types/versions and trailing data before I/O.

Closed public requests are:
- `{action:"export",connection_id,boot_id}`.
- `{action:"prepare",connection_id,boot_id,artifact_base64}`.
- `{action:"confirm",connection_id,boot_id,reference}`.
- `{action:"status",connection_id,boot_id,reference}`.
- `{action:"cancel",reference}`.
- `{action:"retained"}`.

Identity uses the existing observation validators; reference is a fresh opaque
64 lowercase-hex host capability. Base64 must be canonical and decode to at most
131072 bytes. Raw file validation precedes normalization; only the V1 two-member
artifact and existing three-setting schema are allowed. Product/personalization
schema members and artifact version are integer1, not booleans/floats/exponents;
unknown settings/children and unsupported versions refuse. Preserve exact validated
strings, absence and supported null. This is transport validation, not a second
Config overlay, destination validator or Store admission policy.

Request bound is 196608 bytes. Results contain exactly contract_version1,
status, observation and portable_configuration. The latter contains exactly state,
reference, summary, report, retained and export_file. Normal reduced results cap
8192 bytes; explicit export results cap196608 bytes. Only an identity-matched
successful export may have export_file, exactly
`{name:"remarkable-buddies-preferences.json",bytes_base64:CANONICAL_BASE64}`;
it contains the validated compact artifact plus one newline, at most131072bytes.
All other export_file values are null. Consume it only in the explicit file-save
handoff, then discard it; ordinary UI state receives only the reduced result.

States are none, exported, ready, no-change, invalidated, verified,
not-dispatched, unknown, desired-file-observed, unresolved, unsupported,
unavailable, busy and capacity. A reference is null for none, exported, no-change, invalidated and capacity;
ready and original diagnostic states carry the same original opaque reference.
A refused confirm/status may echo only its requested known reference.
Invalidation never mints another operation. Retained is at most eight
closed `{reference,connection_id,boot_id,state}` records, state unknown/unresolved.
Summary is null outside admitted successful file/preview/original-result states.
Export summary is exactly `{kind:"export",declared_settings:INTEGER0_TO_3,
personalization_included:BOOLEAN}`. Import summary is exactly
`{kind:"import",changed_settings:NAMES,before:ORIGINS_OR_NULL,after:ORIGINS_OR_NULL}`.
Names are a lexically sorted unique subset of product_settings/personalization/
research_policy; changed Prepare requires nonempty names drawn only from the
selected artifact's present parents. Origins have exactly those three keys with
absent/declared-null/declared. Prepared before must equal original Inspect current;
after is the admitted producer after, never a UI-computed overlay. No-change has
empty names and both origins null. Apply and original Status may reuse only the
original prepared summary, labeled as that preview rather than fresh values.
No summary includes an intent.
Export report is null or exactly `{status,runtime_activation}`. Import report is
null or exactly `{status,outcome,disk_readback_verified,runtime_activation}`,
with the exact admitted producer values; never a producer data object. No path, hash, artifact, intent, arbitrary error
or text enters a reduced result. Public export payload is the deliberate exception.

## Fixed producer transport
Only the host-fixed Config path
/home/root/.config/remarkable-buddies/config.json is selected. Export invokes the
existing explicit --export-portable-configuration selector; it sends no stdin and
validates the complete original report/artifact/summary before extracting a file.
Import invokes only --portable-configuration-operation inspect|prepare|apply|status
with --portable-configuration-input - for non-Inspect phases and the explicit
REMARKABLE_BUDDIES_CONFIG environment under the existing clean fixed environment.
Never upload to a remote artifact pathname, invoke the file-only offline inspector
with a fabricated path, run a shell supplied by the renderer or query Buddy API.
Identity is verified before/after every phase using current shared wired callbacks.

Private decoded requests cap262144bytes; compact embedded artifact cap131072bytes;
import producer report cap16384bytes; export producer report cap131072bytes,
including newline framing. Use the producer's complete duplicate-free report
validator, not its process exit code alone. Base64 private request envelopes cap
360448bytes; export response envelopes cap196608bytes, import envelopes24576bytes.
Enforce bounds as streaming input/output arrives, kill only the owned child on
excess/deadline, ignore raw stderr and do not log private stdin/stdout/errors.
No pretty-printing or reparsing through a text input that changes characters.

Inspect/Prepare/Apply/Status shapes, path/base/artifact/target digests, names/origins,
status/outcome/readback/activation relationships must match the pinned producer
contract. Compute only documented correspondence digests using validated closed
artifact data and the producer's compact ordering/escaping recipe; prove parity
with actual exported/imported Unicode and control-text captures. Digests do not
authenticate the artifact. Prepare intent must bind the host's new operation UUID and original Inspect
base/path, the exact validated artifact digest and a distinct target hash.
No-change must bind that same original base/artifact with no intent. Apply changed
names/target must equal the original Prepare. Status observed digest must equal
target only for desired-file-observed and differ for unresolved. Origins cannot
prove child-value equality; do not invent stronger cross-checks from redacted
metadata. Preserve the original private response bytes and intent before dispatch. Never expose backend base/path/target/artifact hashes to the UI.

Import Review performs fresh Inspect then Prepare with selected original artifact;
Confirm supplies the original intent plus that same validated artifact. No-change
ends at Prepare. Status supplies exactly `{intent:ORIGINAL_INTENT}`, no artifact,
new base or Store. Neither a delivered source revision nor equal component versions establishes installed capability. Only the complete recognized producer response admits the current invocation. Producer absence/unsupported capability yields unsupported,
without fallback to direct Config editing or older preference writers. Only the
backend admits legacy1 or ready ordinary notebook4 in absent/LocalOnly mode and
owns all canonical/root separation, mutex, publication and write_all custody.

## Failure states
Prepare/Inspect failure and expiration before possible Apply are not-dispatched
or unavailable/unsupported/busy as admitted; they never report a saved change.
Verified Apply requires original target correspondence, ok/verified, true disk
readback and runtime_activation unverified. Complete original producer
not-dispatched may clear that reference. Everything else after possible dispatch
remains unknown, including malformed/mismatched output and late identity changes.
No automatic Apply retry, condition refresh, rollback, second frame or replay.
Original Status reports only desired-file-observed/unresolved for an exact valid
response. An unresolved observation followed by transport loss returns unknown,
without reusing an old observation as a fresh result. Malformed JSON and cyclic
bridge input yield only fixed errors, never parser excerpts in IPC diagnostics.
A complete verified private reply reserves its original slot through the final
bridge generation/publication guard; intervening invalidation preserves unknown
rather than dropping the original before rejecting the late reply. It can retire local uncertainty when the target is currently observed,
but does not change the recorded historical claim or imply who published it.

Cancel targets only the exact lane/reference/token. Ready expires at120seconds.
One active slot and eight non-evicted unresolved originals remain bounded. The
artifact and mutable text buffers are released after dispatch lifetime; original
intent/status evidence remains until explicit current observation or host exit.
No saved-file durability/private-permission claim follows from export download;
no service restart, credentials/provider, archive/sync or native authority follows.
