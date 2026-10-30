# SDK visual setup handoff

Use the separately typed visual-only capture in SDK revision
`f03cc7227d6b32213d6d49ae8c61a1cef6d43711` to replace allocation scanning for a
new explicitly selected developer setup. The original helper and spent packets
remain historical. This changes no installed menu/navigation behavior.

## Selection and clocks

A native capture plan may explicitly select `visual_setup: 1`. Absence retains
the original six-record setup protocol; other values refuse. The observer and
controller artifacts, SDK pin and new wire-4 native profile/library are frozen
together before any fresh candidate is admitted. Native mutation remains disabled.

Keep the original overall 180-second observer bound, launch at most 60 seconds,
setup at most 120 seconds and source-capture at most 10 seconds. Both visual
requests get at most 10 seconds each, capped by that same original setup deadline.
No phase, request or reconnect renews setup or the independent recovery bound.

## Owned observer and images

Only the admitted supervisor parent can use the resident socket. The external
driver SHALL NOT connect to it. After both original input admissions end, the
observer explicitly reconnects once to the same verified child and performs one
CaptureVisual before publishing setup-ready. The request remains read-only and
does not acquire source/page/write authority. Runtime, candidate, service and
mailbox checks continue through request IO and publication.

For each before/after stage, exclusively create a private PNG and receipt, sync
both, validate their bytes under file pins, then publish a separate bound stage
record and completion marker. The receipt binds schema, stage, candidate/runtime
binding, fresh operation UUID, dimensions, DPR, procedure, PNG length and SHA256.
The PNG is at most 1 MiB and receives the SDK's full bounded validation. Partial,
preexisting, changed, corrupt or misbound images/receipts never signal completion.
Published image and phase pins remain current through setup and source capture.
After image read-back and phase JSON sync, recheck runtime/service/candidate
admission immediately before publishing the stage completion marker. Also reject
premature completion/admission records at that boundary. Setup-ready receives its
own closing admission check. Refusal retains partial files without a completion
marker; it never retries publication. Both parties recheck progress after pair
decoding and before acquiring fresh input.

Setup-ready implies that a before-image is available and both admissions ended;
it does not imply any particular screen. The developer driver retrieves and
inspects that image before selecting input. After successful setup input (or a
deliberate no-input selection), it invokes the fixed `setup-visual-after NONCE`
controller role. This verifies the original actor/runtime, candidate, stopped
services, ready/ended/before records and absent later phases, then publishes one
after-image request. It does not perform input or claim that an input succeeded.
The driver remains responsible for refusing after an unsuccessful/uncertain tap.

The observer consumes that request once, reconnects once to the same child with
fresh connection identities, and captures/publishes the after-image once. The
extra reconnect handles the SDK's 30-second idle retirement; it is not a retry
of a failed capture. The developer retrieves and inspects this image before
invoking setup-complete. Completion requires both valid images, distinct operation
IDs, the matching after request and the same original binding. A before-only
completion is insufficient in this explicitly selected mode, including no-input
setup; both images are required consistently.

The actor and observer validate the selected image pair before their existing
fresh-input handshake. Both acquire one new input observer and retain quiet input
through the source request. Source capture still explicitly reconnects once after
setup, then makes one CaptureSource using the original expected full-order facts.
Any visual/setup/source failure takes the existing owned shutdown and independent
stock-first recovery path. Earlier uncertain effects and source preservation
policy remain unchanged.

## Implementation and verification

Expose visual capture through the existing ResidentConnection as a read-only
operation, without a mutation journal entry or invented source observation.
Keep visual-stage orchestration in the development bootstrap feature. A typed
transport callback owns the Runtime so image requests and progress checks cannot
borrow or replace another runtime implicitly.

Owned controls must cover stage order, no ready before the before-image, no
completion before both images, wrong/duplicate operation and binding, partial or
changed files, cancellation/expiry and exactly two visuals plus one final source
capture with no Observe/effect replay. Preserve original v1/v2/v3 journal records
under the SDK upgrade and ordinary non-visual setup behavior. Exercise actual
Runtime/peer reconnect and original uncertainty retention. These are model/source
checks; the separately reviewed developer driver, exact ARM artifacts, fresh
candidate and actual inspected native images remain required for qualification.
