# Design

## Executable tool and bounded private phase diagnostics

One shared helper retains the actual regular/non-symlink/name/content pin checks
and adds ordinary POSIX readiness before builds or image execution. The task owner
must have effective read/execute access. For the immutable image's default UID/GID
0 with capabilities dropped, the applicable owner/group/other permission class
must have read/execute. Reject special mode bits. Normal 0755/0775 are examples,
not a mode whitelist: equivalent non-special 0555/0705 permissions remain valid
for an ordinary UID/GID1000 file. Owner-only0744 does not satisfy the container.
Keep non-POSIX behavior explicit without claiming this validates Windows bind
permissions. Production admission never chmods. Repeat this helper at existing
phase/completion rechecks; a later mode change refuses completion.

Reuse `run(private_diagnostics)` and its existing finally writer. Permit the exact
already-bounded generation combination stdout_limit65536/combined_limitNone in
addition to the existing8192/16384 combined profiles. Stdout still stops at64KiB,
stderr at16KiB, phase timeout120s and process cleanup are unchanged. No arbitrary
new profile or new logger. Pass fresh private work/generation-diagnostics and
observation-diagnostics through existing phase kwargs; no argv/mount/resource/
key or public inventory change. Known command streams contain control metadata,
progress/errors and tracebacks; private keys remain only in disposed generation
tmpfs. No key/file/environment dump is introduced. The outer trace still cannot
recover stderr discarded by a nested failing run; do not overstate diagnostics.

Host controls use real owned file modes, mock phase/build boundaries, and owned
nonsecret toy subprocesses to verify early refusal, equivalent modes, later-mode
drift, private success/nonzero/deadline retention, unchanged output caps and
unsupported profile refusal. Actual package runs remain separately selected.

Use a separate explicit `apk_package_inputs.py` CLI. Its external completion hash
and original producer SHA are independent inputs, not inferred from adjacent JSON.
Run the unchanged strict verifier, then bind actual full source/license and
independent SDK release proof to both retained target records. Normalize tuples
and lists through JSON representation only; compare every proof field, including
types and missing/extra dictionary members or list entries.

## Historical correspondence and current-operation stability

Keep `sdk_release_source` unchanged. It must continue refusing any location,
snapshot, local/remote tag or other proof change during a single observation.
After strict input verification, both retained target proofs must match each other
in full. Capture a new independent proof through that unchanged observer.

Classify the complete recursive historical/current comparison:

- No differences: `historical-proof-equal`.
- Exactly one differing leaf, `$.location_identity[1][3]`, with both old/current
  values nonnegative integers (not booleans), in two well-formed four-integer
  root/Git location identities: `historical-git-ctime-only-revalidated`.
- Every other difference or malformed proof: refuse before staging/generation.

The second classification records content correspondence after fresh independent
validation; it does not declare directory metadata unchanged or explain the cause
as a fact. Do not remove/replace a field to compare projections, infer missing
proof, rewrite historical evidence, or provide an allow-drift CLI flag. Compare
all keys, shapes, values and types; root ctime, Git dev/inode/mode, tracked-file
identity, manifest, local tag object/peel, remote observations, conversion and
unknown-field changes all refuse. No externally supplied exception record or
general transition framework is introduced.

The implementation uses structured key/index components to identify the sole
classified leaf. Human-readable bracketed JSON paths are evidence only; an extra
dictionary key resembling a dotted/indexed path cannot alias that location.

Retain a private `sdk-proof-correspondence.json` in the packaging work directory:
complete normalized historical and admitted-current proofs, classification,
explicit old/current values at every differing field, and
`continuous_custody_claimed=false`. The two original per-target private records
remain unchanged. Bind this new record's exact bytes/digest plus classification
and explicit difference into final `build_input_provenance`. This references the
private record; it does not add an APK/index/public artifact or change signed
build metadata. The private record is retained and delivered with operation
evidence, never treated as adjacent self-authentication or production trust.

Every subsequent recheck calls the unchanged observer again and demands complete
equality with the newly captured proof, including its admitted ctime. Do not
reclassify later changes. A second ctime change after admission refuses just like
any other current-proof change, before generation/observation/completion at the
next boundary. Rehash the private correspondence record across the same boundaries.

Keep original producer and new packaging executor checkouts and revisions
distinct. The original tagged producer/release/SDK inputs remain read-only. Use
fresh disjoint external work/final roots. Stage exact binary and canonical build
metadata bytes with checked copies; source LICENSE and the pinned resident bundle
complete the existing generator inventory. Private build evidence stays private.

Extract the original builder's generation/observation tail into one helper. Both
CLIs use its unchanged container arguments, pins, 120-second phases, owned cleanup,
ephemeral private key and separately supplied generation-control SPKI pin. A
receipt consumer callback rechecks source, proof and inputs before generation,
after observation and before exclusive completion. The final receipt identifies
both the accepted build receipt/original producer and the packaging executor.

Host tests use owned synthetic files and mock only external source/tool/phase
boundaries. They prove refusal before launch, no compiler/build calls, checked
copies, unchanged metadata, failure without completion and separate public-key
observation. Actual signing/container/device execution remains a later explicit
operation, not a requirement for completing this bounded source capability.

## Correction controls before renewed review

Exercise the classification through the actual receipt consumer with mocked phase
boundaries: a genuine historical/current ctime-only fixture difference completes
both phases without build calls, preserves original bytes and retains full proofs
and explicit difference in evidence/provenance. Also retain the equal-proof case.

Parameterized refusals cover root path/device/inode/mode/ctime; Git
device/inode/mode; manifest; source repository/tag/commit/epoch; local tag object;
remote tag object/peel and key inventory; raw working/committed/file identities;
conversion; missing/extra/unknown nested keys; list length/type and invalid ctime
types; ctime plus any second difference. Check source observer's implementation
unchanged. During a successful mocked package operation, change only fresh Git
ctime after admission (before generation, between phases, after observation and
during final copies): no later classification or completion is allowed.

## Fixed bind-mount access

Both phases bind only the admitted tool file readonly at /tool/apk; retain its
private host parent. Receipt-only staging creates work0700 (existing builder
mkdtemp already does); only newly created artifacts is initialized0777 beneath
that private owned parent. Container UID/GID0 and cap-dropALL remain unchanged,
as do root/root payload inventory, signing and public-only observation.

Shared existing-module admission refuses symlink/non-directory or non-owned/non-
private work roots, then checks fixed child roots and ordinary staged entries:
applicable pinned UID0/GID0 read/traverse, plus artifact root read/write/traverse.
No chmod occurs in admission. Restrictive umask input/module/control permissions
refuse rather than broadening frozen sources. Recheck before generation, between
phases including actual generated-control access, after observer and final copy/
completion boundaries. Preserve all source/SDK/content evidence and prior failures.
