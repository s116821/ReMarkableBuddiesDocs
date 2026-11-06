## ADDED Requirements

### Requirement: Executable pinned tool admission and bounded private diagnostics
Both package entry points SHALL share regular/name/content-pin admission and
ordinary POSIX read/execute readiness checks before build/container/signing. The
task owner's effective access and pinned cap-dropped image identity's applicable
permission class SHALL permit tool use; equivalent non-special modes SHALL NOT
be needlessly excluded. Production admission SHALL NOT change permissions.
Existing rechecks SHALL refuse later loss of readiness before completion.

Private phase diagnostics SHALL reuse the existing finally-based stream writer,
accepting only the existing8192/16384 combined profiles or the exact existing
generation65536-stdout/None-combined profile. All output/stderr/time/process bounds
SHALL remain unchanged. Fresh private work paths SHALL retain outer phase errors
without new key access, environment dump, container mount or public artifacts.
They SHALL NOT claim recovery of discarded nested-tool stderr.

#### Scenario: Correct bytes without executable readiness
- **WHEN** the pinned POSIX tool has0664 or owner-only0744 permissions for the selected owner/image identities
- **THEN** admission refuses before build/image execution or signing, without chmod or retry

#### Scenario: Equivalent readable executable modes
- **WHEN** actual tool bytes and effective permissions satisfy both task-owner and image read/execute needs with ordinary non-special modes
- **THEN** ordinary admission proceeds without an exact0755 whitelist or loss of other source checks

#### Scenario: Phase failure with private diagnostics
- **WHEN** a bounded generation or observation command fails or reaches its unchanged deadline/output cap
- **THEN** captured bounded outer stdout/stderr remain private while owned cleanup and refusal semantics remain unchanged

### Requirement: Explicit strict receipt consumption
The packaging-only consumer SHALL accept an independently supplied completion
digest and original producer identity, call the strict input verifier without
weakening its canonical inventory/hash/profile/source/SDK checks, and stage the
original binary and build metadata bytes without rebuilding. It SHALL recheck the
actual full release source/license and every field of the historical and newly
observed independent SDK proofs under the correspondence requirement below.
Tuple/list JSON normalization SHALL NOT discard identity fields.
Original build producer and packaging executor revisions SHALL remain distinct.

#### Scenario: Accepted frozen input bundle
- **WHEN** externally pinned completion, all actual input bytes and original producer/source/SDK identities agree
- **THEN** packaging stages checked original bytes without calling a compiler or target runtime

#### Scenario: Changed or substituted input
- **WHEN** completion, inventory, bytes, source/license, producer, an unclassifiable SDK proof identity, tool or required resident bundle differs
- **THEN** admission refuses before generation, without rebuilding, rewriting metadata or substituting inputs

### Requirement: Shared bounded test-key packaging
The consumer SHALL reuse the original builder's generation and separate
public-key-only observation stages with unchanged tool/image/bundle pins,
isolation, timeouts, owned cleanup and generation-control SPKI channel. Source,
receipt/proof and staged inputs SHALL be rechecked across operation boundaries.
Only a successful complete observation SHALL publish an exclusive final receipt
bound to accepted build inputs and packaging executor, with not-qualified status.
The original build-based CLI SHALL retain its existing behavior.

#### Scenario: Both packaging phases succeed
- **WHEN** generation completes, its ephemeral private key is disposed and owned container absence confirmed, then separate public-key-only observation succeeds
- **THEN** only checked actual artifacts and the final not-qualified completion are retained without exporting a private key or granting installation authority

#### Scenario: Refusal, failure or changed inputs
- **WHEN** generation or observation fails or any admitted input/proof changes before completion
- **THEN** no completion receipt is published, useful diagnostics remain and no retry or trust bypass occurs

### Requirement: Explicit historical SDK proof correspondence
The consumer SHALL compare all fields, types and structure of both retained
target proofs and a newly observed independent SDK proof. The existing
`sdk_release_source` observer SHALL remain unchanged and SHALL require complete
stability within every observation. Historical/current equality MAY be recorded
as `historical-proof-equal`. Exactly one Git-directory ctime leaf difference at
`$.location_identity[1][3]` between well-formed location records MAY be classified
as `historical-git-ctime-only-revalidated`, with actual old/current nonnegative
integer values retained. Every other difference SHALL refuse before generation.
Neither classification SHALL claim continuous historical custody.

The consumer SHALL preserve both complete normalized proofs, classification and
explicit difference in private operation evidence, and bind that record's
bytes/digest, classification and difference into completion provenance. Original
build receipts/private evidence and signed metadata SHALL remain unchanged.
No allow-drift flag, field-dropping projection, replacement proof or compiler
rerun SHALL establish correspondence. After admission, each fresh full proof
SHALL equal the initially admitted current proof, including ctime; later changes
SHALL refuse rather than being reclassified.

#### Scenario: Historical Git-directory ctime alone differs
- **WHEN** both complete retained proofs agree and fresh independent observation differs only at the Git-directory ctime leaf with valid actual values
- **THEN** packaging may proceed as freshly revalidated content correspondence, preserving full proofs and explicit difference without claiming unchanged historical custody

#### Scenario: Historical proof is identical
- **WHEN** complete historical/current proofs agree after tuple/list normalization
- **THEN** equality is recorded without implying continuous observation or weakening later full-proof stability

#### Scenario: Any other historical identity differs
- **WHEN** root identity/ctime, Git device/inode/mode, source/raw-file/tag/manifest/remote/conversion field, type, key inventory or proof structure differs, alone or alongside ctime
- **THEN** correspondence refuses before generation without rewriting evidence or substituting a source

#### Scenario: Current proof changes after admission
- **WHEN** even Git-directory ctime alone changes during later packaging rechecks
- **THEN** the operation refuses at the next boundary and publishes no completion, preserving the first failure without reclassification or retry
