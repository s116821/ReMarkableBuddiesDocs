# Reader persistence seam — bounded design accepted; implementation verification open

This additive plan implements tasks3.1–3.3 and4.4 in the active REM37 change.
It does not qualify SDK acquisition, page binding or native completion. The current
Rust18e1a741 capture-persistence checkpoint fixes the independently reproduced
derivative geometry defect and has bounded independent Sol acceptance.

## Acquisition states

DeviceBackend supplies an explicit acquisition result alongside the captured Frame.
One state carries a complete SDK-owned CapturedBatch, retaining its original identity,
qualification, parent and derivative order. Another state explicitly declares a
legacy acquisition with identity and qualification unavailable. An attempted SDK
capture that fails, returns unknown identity or lacks required facts is a refusal,
never an implicit fallback to the legacy state. Backends opt into legacy acquisition
explicitly; tests can supply clearly labelled SDK synthetic batches.

Legacy evidence uses a separate Buddy historical container with absent identity and
qualification. It cannot inhabit SourceObservation or SDK facts, generate a page UUID,
or establish a native binding. Persist the exact overview and each detail actually
submitted, preserving their original order. Retain an acquisition parent whenever
provided; if a legacy backend supplies none, record that absence explicitly. Do not
claim sibling derivation or original acquisition pixels from overview alone.

SDK amendment [1072e12bcfff8fabf3c64ca7bb7b1c8396e8967b](https://github.com/s116821/ReMarkableOpenSDK/commit/1072e12bcfff8fabf3c64ca7bb7b1c8396e8967b)
now permits this explicitly selected Buddy-only unbound legacy history. It preserves
refusal for failed SDK capture, absent native qualification and all output guard and
receipt requirements. Detailed consumer implementation remains subject to exact review.

Proposed Buddy legacy payload: schema1, evidence ID, conversation/turn IDs,
origin LegacyUnqualified, identity None, qualification None, acquisition-parent
descriptor Option, and an ordered list of actual provider-image descriptors
(Media, decoded dimensions, overview/detail role and provider ordinal). Require
explicit null for absent fields and refuse unknown fields/versions. Do not add
affine, crop or viewport provenance when the backend did not provide verified
descriptors. A supplied parent is retained as acquisition pixels without claiming
an SDK-qualified owner or derivation. Preserve the distinction from SDK Capture
records in context and retained-history APIs. Conversation UUIDs identify Buddy
records only and are never replacement document/page UUIDs.

Preparation bounds:1–15 provider images plus at most one acquisition parent,
32MiB encoded per image and64MiB encoded total, checked before staging; existing
8192-axis/32MiB full-image decoding limits still apply. Fail rather than truncate.
Apply ordinary root CAS, operation fingerprint/retry, integrity and retention rules.
These are consumer persistence bounds, not native compatibility or aggregate
process-memory guarantees.

## Preparation and provider use

Orchestrator retains the shared Ledger created from startup's existing Arc<Store>.
Capture once through Workflow's guarded device seam. Freeze the returned original
image bytes, validate and commit a Prepared user turn plus linked evidence/media
under full root heads before adding any images to the provider. Storage failure
returns before provider execution, navigation or typing. Legacy runs allocate an
explicitly unbound conversation; matching images or headers never adopt old pages.
SDK-qualified page lookup remains a separate required capability.

Retrieve that prepared batch through the ledger for proposal and verification.
Both requests submit identical original bytes in identical order; base64 transport
does not reencode images. Preserve current prompts and progress callbacks. Any
future provider-specific image processing must produce a recorded derivative before
submission. Retrying an acknowledged preparation reuses its original operation,
turn and stored bytes; restart does not automatically dispatch interrupted attempts.

## Outcomes and authority

Prepared turns are excluded from visible context. A request becomes Interpreted only
after independent transcription verification. The answer remains Generated until
the device seam supplies a separately qualified output receipt containing exact
verified text and current native facts. render_answer returning Ok is insufficient:
it also returns Ok for absent or invalid successors. Provider/device errors and
cancellation retain explicit terminal facts; uncertain effects become
ReconcileRequired and are never automatically repeated. Existing process-local
undo ownership and request retirement guards remain intact.

Historical unbound context remains useful for inspection without page-revisit or
native-binding guarantees. SDK-dependent operations refuse unavailable or synthetic
qualification. This plan does not retrofit legacy verification into SDK receipts.

The current backend can report NoOutput for absent/invalid successors or
SubmittedUnverified for a render that succeeds without a qualified SDK receipt.
Neither state becomes Completed. Commit the generated assistant draft before
navigation/output; once input may have occurred, missing verification leaves
ReconcileRequired. Record a no-output refusal as Failed with an explicit reason,
preserving the interpreted user turn. Proven no-effect failures may record
Failed/Canceled; ambiguous device errors retain uncertainty. Storage failure before
rendering prevents rendering. Failure after possible input leaves the precommitted
draft for explicit inspection and restart reconciliation, never automatic replay.

## Concrete consumer choices for review

Add a distinct `Record::LegacyCapture` in the Source namespace, linked from the
Prepared user's sources. Keep `Record::Capture` exclusively SDK historical facts.
Expose legacy evidence separately in context, inspection and retained-media APIs;
never construct ImageUse/SourceObservation from it. Descriptor role/ordinal and
encoded-byte digest determine provider ordering and retry fingerprints. Integrity
checks fully decode PNG/JPEG under existing bounds without reencoding them.

The backend explicitly selects acquisition kind before Workflow starts capture.
The trait default is unsupported; RealDevice and simulator declare legacy selection
explicitly, while SDK fixtures opt into the SDK branch. Workflow freezes overview
and detail bytes once within the existing request guard before ledger preparation.
Base64 details are decoded once to their exact original encoded bytes. Any error in
SDK acquisition or in legacy capture/details refuses before provider dispatch.
No branch attempts a second acquisition as error recovery.

Until qualified source/binding lookup exists, each legacy iteration creates a new
explicitly unbound conversation. It does not infer continuity from headers, OCR,
image equality or process-local history. Stored unbound history can be inspected
by its Buddy conversation ID after restart; automatic same-page resume remains an
open qualification gate. This bounded integration is not complete REM37 acceptance.
No historical turns are silently injected into a provider request; future resume
must use the existing explicit context budget/selection contract.

Add an explicit Reader output result: NoOutput(reason) or SubmittedUnverified.
Commit the assistant Generated draft before entering render_answer. Navigation
attempts are effects: record ReconcileRequired before entering rendering, then
retain it after a submitted output or ambiguous error. NoOutput is restricted to confirmed unchanged source or a verified return without
answer input; an unconfirmed return stays uncertain. A proven no-output result
can be separately recorded as a reconciled Failed revision; it cannot masquerade
as Completed. This requires an explicit fact-only reconciliation operation with
root/turn CAS, retained history and idempotent fingerprint, rather than widening
ordinary advance to replay effects. No runtime restart automatically reconciles
or dispatches these attempts. The renderer preserves existing request/undo guards.

If preparation or assistant-draft publication fails, propagate the storage error
and make zero subsequent provider/output calls. If terminal recording itself fails,
return a combined error and leave the previously durable Prepared/Generated or
ReconcileRequired facts intact. The caller cannot invent an acknowledged terminal
state; restart inspection reports the interrupted state for explicit reconciliation.

## Verification and remaining design work

Use the actual Orchestrator and recording LLMEngine with a real temporary Store.
Assert proposal/verification bytes equal ledger retrieval; test a backend whose
later detail query changes to prove no second acquisition, and storage failures
with zero provider calls/navigation/typing. Verify original source state remains
unchanged. Cover provider failure, transcription disagreement, no successor,
invalid successor, cancellation, output uncertainty and restart without effect replay.

Independent Sol review accepted exact design c84265fcf38014df99a7fd3adfd128e4ea9b9d91 before implementation. The reviewed choices settle the unbound evidence schema, bounded
legacy acquisition descriptors, conversation selection/resume seam, output-result
type and responsibility for terminal recording when storage itself fails. SDK owns
acquisition and native receipt meaning; Buddy owns ledger/container and orchestration.
Native smoke, release builds and canonical sync/archive remain separate open gates.

Source basis: current Reader/Workflow/DeviceBackend code, accepted REM37 tasks and
SDK boundaries, independent review finding, and coordinator's current semantic
direction. The bounded design has exact independent acceptance; code, native qualification and complete issue delivery require their own evidence.

## Selected development-capture increment (2026-10-08)

Main selected a separate SDK-owned development acquisition after the actual
[v11 capture](https://github.com/s116821/ReMarkableOpenSDK/pull/1#issuecomment-6060257011)
produced a visually inspected first-page PNG. This receipt lacks the session,
visit, revision, input, render and affine facts required by CapturedBatch. Its
observed_order is false. Do not fabricate those facts, relabel the acquisition
Synthetic, or route it through Legacy (whose current branch permits legacy output).

The selected opt-in SDK DevelopmentCapture owns the exact PNG and original strict
v2/v11 completion bytes, with expected attempt/fixture inputs distinct from reported
identity. Its parser checks bounded byte/receipt correspondence, not freshness or
live ownership. Main's existing collector retains the live candidate/root/payload
checks. The type grants no SourceObservation, CapturedBatch, CaptureFacts, live
guard, effect capability or Reader preparation.

Buddy adds an explicit DevelopmentUnqualified acquisition and separate historical
evidence container. Freeze and atomically persist the original receipt, acquisition
PNG and actual ordered provider images with the Prepared turn before provider
dispatch. Reopen/readback retains exact bytes and development provenance; expected
fixture order never becomes observed page order. Proposal and verification retrieve
the same durable provider bytes. Missing/corrupt evidence refuses dispatch.

This branch is always non-output. A persisted Generated answer records
NativeOutputUnavailable without navigation, typing, selected preparation or effect
settlement. Trigger/setup/status/history and branch-dependent selected render_answer
remain unavailable. Existing SDK synthetic and explicit legacy paths retain their
semantics. Focused actual-Orchestrator persistence/provider-byte/zero-output checks
and a fresh controlled RM2 capture-to-persistence run verify this increment;
production bootstrap, qualification, settlement and full task2.10 remain open.

Source basis: the linked actual capture receipt and visual inspection; current SDK
and Buddy API inspection; Main's selected narrow integration. This section records
the selected increment, not completed implementation or qualification.

## Partial verification (2026-10-08)

SDK development-capture revision d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1
and Buddy revision b085d4d78b56646cb2ee8bb73b81845bafeeb53f implement the
selected read-only transport and persistence branch. Main independently ran the
actual Orchestrator with a real retained Store and a recording provider against
the previously collected de375 v11 completion and PNG. The original receipt and
RGB8 PNG, 768x1024 overview and three overlapping detail images persisted before
both provider passes and reopened byte-for-byte. The one-shot transport refused
reuse; Generated ended with NativeOutputUnavailable and zero device effects.
This is a historical-byte integration check, not fresh native ownership or a
live provider/model result. The original PNG stays unchanged; RGB-to-RGBA working
conversion applies only to the derived prompt images.

The fresh 41ce4495aa674325bea22466c2eae0ba attempt used the same SDK native
producer and Buddy capture consumer e41c978d30d736853f9a0cb7b58070d6dffe5b1e.
One released contact and one capture publication reached PNG creation, then
refused in the queued completion callback. No completion file was published,
so the fresh capture-to-Reader harness was not run. Main preserved and visually
inspected the PNG and refusal metadata, restored stock, removed only the exact
owned stage/helper, and independently verified all fixture/provider hashes,
service policies and absence of spent stages. The failing predicate remains
unknown; a five-second deadline crossing is an inference, not a measured cause.
The attempt is spent and must not be replayed.

Buddy's exact revision passed CI Test; strict Build & Lint still fails on unused
production admission/selected-backend scaffolding. Independent review and fresh
capture-to-persistence verification remain open, as do production qualification,
bootstrap, effects, settlement and the remaining task2.10 lifecycle gates.

Source basis: exact pinned source review, Main's retained historical integration
receipt, current 41ce operator/publication receipts and preserved bytes, independent
restoration/cleanup/final-baseline outputs, and
[Buddy CI](https://github.com/s116821/ReMarkableBuddies/actions/runs/37783000265).

The next spent attempt, df2494e3ec5c4d9b9416435fe99f30f1, used native SDK
a4cfd898c0954881f80284e0f65a135a7d73a916 and capture consumer
36d7b65c844b668bea3735a7aff331b6520c0582 with a default-off completion
diagnostic selected. The first existing ownership check refused: accepted21009,
baseline24303, postRead24360, failure25450, effectiveDeadline26009 milliseconds.
Because the monotonic failure time is sampled after that check, its559ms remaining
budget rules out the accepted+5000 deadline for this attempt. It does not identify
the older41ce cause. The failed ownership subpredicate was not reported; sticky
invalidation or an ownership endpoint change remain hypotheses.

The PNG was again written, but no completion record was published and the fresh
Reader harness was not run. Main preserved20 stage files and7 helper evidence
files with matching hashes, visually inspected the PNG, and removed only the exact
owned stage/helper after verified restoration. Final independent baseline passed
at stock PID11221/start238122636 with fixture14/provider10 hashes unchanged,
service policies restored and all spent stages absent. The successful v11 wire,
SDK parser, original five-second budget and Readerb085 remain unchanged. A narrow
versioned refusal diagnostic can report cached predicate/subreason without adding
native getter calls or relaxing acceptance; fresh integration remains open.

Source basis: current pinned source and decoded final callback, preserved PNG and
raw receipt, independent cleanup and final-baseline outputs. Deadline exclusion
uses the existing monotonic clock; the ownership failure cause remains unknown.

Independent consumer review of Buddyb085 reproduced a P2 at the Workflow boundary:
the development constructor retained an effectful selected facade, and dispatch_reader
could navigate using an already-published matching context. The historical
Orchestrator tests' zero-effect observations do not establish refusal for that entry
point. A narrow immutable-mode dispatch repair and the reviewer's failing regression
plus ordinary selected-mode control are required before asserting the development
Workflow always refuses effects. The isolated native capture lane may continue.
Source basis: [independent review and reproducer](https://github.com/s116821/ReMarkableBuddies/pull/30#pullrequestreview-5457231891).

The narrow repair is pushed at Buddy f6999d5c85bdf6479eae41c493213d72e98e5b29.
A private persistent development-mode flag refuses dispatch before reaching the
selected facade or context. Main independently verified the two source inputs and
ran the original regression, ordinary selected navigation control, and two existing
development persistence tests: four passed, with the collected-byte harness ignored.
[Independent repair-only recheck](https://github.com/s116821/ReMarkableBuddies/pull/30#discussion_r4220056084)
closed the P2 with the same original reproducer and control. Fresh capture-to-Reader,
strict lint, native qualification and the remaining lifecycle gates remain open.

The spent 6418c955ca6047d2aefbcb13f2a7f40c capture attempt used SDK
463c5f1fce7def67b3c8c419182be037946afcf0 and capture consumer
279e5bfc608a21bebf61b7eb15be69b4a6c4b7f4. Its versioned failure diagnostic
reports invalidated-before with no active-owner subreason: the sticky invalidation
flag was set before the final queued ownership check, after the prior PNG check
had passed. Failure was at 25,800 ms, before the 26,373 ms deadline. The invalidating
signal remains unknown. No completion record was published; the Reader harness was
not run. Main preserved and visually inspected the PNG and exact metadata, completed
owned cleanup, then independently verified stock PID 13579/start 238225937,
unchanged fixture/provider hashes, service policies and absence of all spent stages.
Source basis: exact saved callback and source ordering, preserved bytes and visual
inspection, independent cleanup/final baseline, and the linked repair-only recheck.

The next spent attempt, 301a86a1a18d48d885c5ddcec0af549c, successfully published
the unchanged 37-field v2/v11 completion through native SDK
3996a6555b6a37f7ede4a6e09c227f1515a01587 and capture consumer
6dd93c85169ca9e100a6dd70759fe0b743ca5424. One released contact and one capture
publication completed in 4,229 ms, with 771 ms remaining in the original five-second
budget. Main retrieved, hash-checked and visually inspected the 1404x1872 PNG.
Its SHA-256 is 7c9d84d2187491755549cbc8960dfaa087e1e9f3c80203411b58cf90c1f43b86;
the exact completion hash is
e96b9169205ecf6c5976c5f2b7975205a74fbe3e2b1a7211045d12725d647289.
The failure-only first-invalidation diagnostic did not fire. The prior sticky
invalidation cause remains unknown; this successful retry does not establish a fix.

Before helper cleanup, Main ran the repaired Reader f699 actual Orchestrator with
a fresh retained Store against these exact collected bytes and independently
selected attempt/root/fixture bindings. The harness passed: the original completion
and PNG plus four derived prompt images persisted before both recording-provider
passes, matched provider bytes exactly, and reopened unchanged. An independent
pixel oracle checked the overview and all three crops. Generated ended with
NativeOutputUnavailable, with zero backend entries, no Pending publication and
no settlement. This closes the fresh collected-byte-to-Reader persistence check.
It remains a historical import through SDK d01b4bdf, not a live model result or
an acquisition qualification claim. Native/render/UI/atomic/order authority all
remain false; no facts request or positive visual decision was published.

Stock restoration and owned cleanup completed. Main independently verified stock
PID 15947/start 238343560, all 14 fixture hashes, all 10 provider hashes, service
policies and absence of every spent stage. Six helper evidence files were preserved
with matching hashes before exact helper cleanup. Reader strict lint still reports
24 unused production items; production bootstrap, qualified acquisition, effects,
settlement, native render and the remaining task2.10 lifecycle gates remain open.

Source basis: Main's exact capture/collector records, retained f699 integration
receipt and pixel assertions, visual inspection, independent final baseline and
[exact f699 CI](https://github.com/s116821/ReMarkableBuddies/actions/runs/37790700992).
The [saved PNG](https://drive.google.com/file/d/1j9jn_FmKczOtMwQ-F_OwJ6XWrU4DS9_l/view)
is a presentation copy; local source bytes are hash-verified. Drive upload and
metadata are verified separately, without asserting a remote byte checksum.

The subsequent source-facts attempt 0404ebf9b5794196a85bfba7ee6859ba used SDK
71d9dbfa33ba828540fa0a9f22ec4db8aca862d6 and consumer
3e51532061c42cfed8640e894a97f08c6a2da90a. This separate read-only mode was
intended to observe native six-page forward/reverse mappings, without pixels,
facts admission or Reader effects. Both source reviews and the exact packet
build/prepare-only/preflight passed. Main rebound a historical inline payload
checksum to the reviewed artifact before arming; acceptance predicates stayed
unchanged. The helper staged successfully before launch.

The attempt failed at the readiness phase, with no verified released-contact,
publication or source-facts result. Host collection recorded armed=true,
restored=false and cleanup_verified=false; the host exited without its timeout.
The previous-boot journal records restoration starting at 15:26:34 UTC, followed
by the instrumented application's shutdown and SIGSEGV at 15:26:37. Its existing
OnFailure dependencies were triggered. The reboot interrupted the restoration
service, and the transient stage/evidence disappeared. The crash cause and the
original host-readiness exception remain unresolved. No retry is authorized by
this failed result; the nonce is spent.

Main independently verified the post-reboot state: boot
02b2347b-03aa-4a85-8dd7-d731aabf6f3e, stock PID 291/start 561, unchanged RM2
firmware 3.28.0.172, all 14 fixture hashes and all 10 provider hashes, active
stock services, original policies and absence of spent/current stages and helper
roots. This establishes the current safe stock state. It does not turn the failed
operator restoration or missing source-facts evidence into success. The prior
301a Reader persistence result remains valid within its stated limits; native
source qualification and production Reader dispatch remain open.

Source basis: retained host/operator/readiness records, previous-boot journal,
and independent post-reboot hash/service checks. The crash and reboot are
observed facts; a specific code defect causing them has not been established.
