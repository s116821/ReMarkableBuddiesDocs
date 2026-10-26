# Installed resident request integration

Implementation: Buddy `b585517a2b7d814576f8b8c9a9acedb72b781439`, with SDK
`df4383e0af4bccd2e4e1a6b14615e8f281dc5cb3`. This is an installed-session
component, not completion of automatic native Buddy-page creation.

## Implemented behavior

`Session::request` and explicit `Session::reconnect` replace the raw connection
accessor. The common dispatcher invokes the existing Store-backed observation,
insertion, selection and original-target reconciliation operations. Typed input
progress distinguishes quiet/canceled input from observer errors. Cancellation,
caller deadline, connection retirement, unresolved work and request refusal
retire only the socket; integrity failures poison the service health owner.
Dropping the whole session remains fatal. No effect is automatically retried.

Progress retains installed pins, lease, service incarnations, stock exclusion,
group membership, original child and consumed admission checks. Input is sampled
again after authority checks. A final admission check after successful outcome
publication refuses stale delivery while preserving the actual historical reply.
Earlier uncertain effects remain sticky across retirement and reconnect.

Service reads distinguish the original caller deadline from their internal
three-second timeout. An unreaped owned command is fatal in either case. Typed
causes survive the actual anyhow/IO/SDK transport error wrappers; classification
does not parse diagnostic strings or infer cause from a subsequently expired clock.

## Review and verification

Independent source review accepted the implementation after fixes for lost typed
callback causes, input changes during authority checks and cancellation/deadline
during journal publication. Regression cases exercise those paths, real owned
socket/child retirement and reconnection, dispatched insertion and selection
uncertainty, malformed peer identity, changed artifacts, service command cleanup,
and the actual health-owner datagram behavior. These are host fixtures.

Formatting, whitespace and Python fixture syntax checks passed before publication.
The matching Docs changes pass all 88 strict OpenSpec validations and the
manifest/guidance/source check (25 guidance files, 126 preserved source blobs).
The exact Buddy [pipeline 40257213471](https://github.com/s116821/ReMarkableBuddies/actions/runs/40257213471)
has compiled and passed strict lint; all-feature tests are running. Execution
success is not yet claimed. The prior reconnect-only revision `c546e77` has passed
Checks in [40255895994](https://github.com/s116821/ReMarkableBuddies/actions/runs/40255895994),
with packaging still running; that does not validate this revision. SDK `df4383e`
has passed its full [40253152513 pipeline](https://github.com/s116821/ReMarkableOpenSDK/actions/runs/40253152513).

Local Rust builds remain unavailable after the preserved disk-full failure.
Automatic approval review rejected removal of the selected build cache; no
cleanup or alternate deletion was performed. Hosted CI supplies execution evidence.

## Remaining integration

The first-gesture Workflow does not yet own this Session or reacquire its source
and input after activation. Historical ReaderFacts are not a current capture,
binding or Writer lease. Approved installation/profile/bootstrap resources,
Manager lifecycle, reusable native ownership and actual Reader/Writer/tablet
acceptance remain required. No tablet action occurred for this increment. Native
capability remains disabled; the overall change remains unarchived.
