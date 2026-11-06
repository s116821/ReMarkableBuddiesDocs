# Source-admission correction delivery

## Scope and canonical ownership

This is the bounded correction in existing Buddy PR38 / Docs PR25, not a new
packaging feature or a completed production package. The original producer and
resident extension are already in main. Current source0e5f0b13919ed5bbb92b873c8af86ff07a5dea56
(tree345ab88a3887dbd6527518efc00e63242dbd646e) changes seven files,237additions/23deletions:
Cargo manifest/lock SDK adoption; resident SDK pin; overlap refusal; independent
SDK tag/source proof and continuity plumbing; host/local-Git tests. The native
bundle hash, public signed schema and installation-ineligible test profile stay
unchanged. No tablet capability is advertised by these source corrections.

The precise implemented behavior is synchronized in
[canonical source admission](../../specs/buddy-package-source-admission/spec.md).
Its transferred scenario bodies are removed from the active signed-artifact
delta. This is partial contract synchronization in the same coordinated pair;
the broader parent is deliberately not archived. The user-authorized bug repair
and implemented source-proof contract do not wait for production package rollout.

## Exact validation and provenance

The pre-closeout Docs head is38f1e270d10ee4820ffc00c3e0fc8d82647d8661
(treee276af01740d4d7f7648c08b53aaea47f2f33279). Root independently reviewed the
source/proof repair and exact evidence. Actual owner controls:48host cases,
44pass/four explicit existing skips;11actual local-Git integration cases pass.
These fixtures replace canonical network/Cargo transport, not real local Git
objects, source checks or mutation cases. Original failures remain unchanged.

Exact-source hosted [Buddy42100511365](https://github.com/s116821/ReMarkableBuddies/actions/runs/42100511365)
and [Docs42100483318](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/42100483318)
passed. Those checks validate their original heads, not this later Docs amendment.
Current review intake found both PRs draft/MERGEABLE with no unresolved review
threads; historical changes-requested reviews are not new unaddressed findings.
Root's [source review](https://github.com/s116821/ReMarkableBuddies/pull/38#issuecomment-6668097388)
and [paired Docs review](https://github.com/s116821/ReMarkableBuddiesDocs/pull/25#issuecomment-6668097798)
remain exact-revision records. Final closeout review/Docs CI remains separate.

### Actual independent SDK release-source proof

One admitted production sdk_release_source invocation passed against a clean full
standalone canonical SDK checkout. Tagv0.2.0 actual annotated object
876f90b62ae4623b31295d45b3d13e2f99b99b72 peels to
a0c6480be6785480c2e0da76a3c06697a18efae4; tree82a90167dbcc67133ad308ef902878c41143af9b.
Both bounded canonical remote observations matched. Manifest SHA256
0b4388cecec636a1918efc6e1749d6eb4ba1882f4dfb7ef7e3eebca741ac5e19
is1363LF bytes and matches committed/Cargo bytes. All357raw source blobs match
committed inventory. No tag synthesis, cache ref/config edits or proof retry.
Production proof receipt36,837B/SHA256
f9fbf9de8eaf62087a6e82d4337598bf65e5102233d18667395c252a806af0ae;
compact handoff d9112cd95f5459e64656c460ba355e2d5d793ce934b46c44236900322f1609e8.
Raw private source/receipt files are retained locally, not public downloads.
Root retains the single6,321,274logical-byte proof clone for later packaging use.

### Actual Cargo-to-SDK identities

Production cargo_identity ran once per target, ARMv7 first and AArch64 only after
its success. Both used existing process-local offline Cargo metadata and the
proved independent source, each with its own legitimate fresh tag observations.
Full fresh graphs equal the retained graphs semantically; no drift/retry occurred.

| Target | Root features | Packages/nodes | Actual metadata identity SHA256 |
| --- | --- | --- | --- |
| ARMv7 | installed-resident-output, development-resident-bootstrap, development-input-diagnostics |388|d0f434e59bf2ade06eb380a42333bcf94553d6864cf66870c2d3628f35739fca|
| AArch64 | none |390|6394c39d9f2754e1662b515c8f65ae0c84b762a220049140a5a6c3fde31e40c8|

Both results bind tagged-git SDKv0.2.0/a0c6480 and the manifest/tag object above.
SDK development-capture/mock/native-adapter graph features include dev edges;
metadata is not evidence of native authority or final binary linkage.
Cargo.toml SHA256d753a3f16a6f17beaa3acb1b57a874386f3e3ad940580fdc2a15639fe1007c6e;
lock5ae32abe822fd06668d034e09cab8559665dbb0014c6905a8e64a83974cbdaf9.
Actual handoff6,645B/SHA256
ff805387ba1072a6d156373d21f568700b6e53a42545888b3197d5df017e4837
pins13private phase/graph/identity inputs. Source, Docs and SDK remained clean;
SDK local configuration hash stayed unchanged. No compiler or build script ran.

## Current verification and next delivery action

Local Docs checks for this amendment pass:12unit tests,36current guidance
files/126preserved provenance blobs and114strict OpenSpec items. Exact final
commit and retained log hashes are recorded at handoff. No repeated source, model, package or tablet
qualification is necessary for this documentation correction. Root reviews this
precise final Docs diff and its successor hosted checks, then coordinates normal
Docs-first/source-second squash delivery in the existing PRs. Current Buddy main
60817c80265f84c55aa0a872b7c9a32497abfdc0 includes the disjoint Windows cfg repair;
Root must preserve it in the final merge tree, not transplant a reverse two-dot
diff. Source0e5f0b1 remains the exact previously checked source correction.

The normal maintained release workflow chooses and publishes any genuine next
Buddy release tag; this change does not invent one. Current producer is an
untagged linked worktree, and known stablev0.63.0 still pins SDKc87e5628. After
actual release observation, select its exact clean/full/standalone canonical Buddy
source and fresh release-source/Cargo admission before separately admitted
build/package/signature/reproducibility work. The old heldv0.56.0 packet is not
reused. Production signer/trust, runtime/native installation and lifecycle,
maintained APK release integration and full acceptance remain open in this parent.
Tasks1.3/1.3b/1.4/2.1/2.2/3.1–3.4 stay unchecked. No package/activation/deletion hold
is lifted; existing held outputs remain untouched.

Source basis: exact source/spec diffs, existing independent reviews/hosted checks,
actual bounded SDK/Cargo receipts and local postconditions. Current delivery
sequencing is a coordinated implementation decision, not new package evidence.
