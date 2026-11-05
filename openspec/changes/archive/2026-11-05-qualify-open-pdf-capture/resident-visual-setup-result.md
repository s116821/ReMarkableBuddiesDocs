# Resident SDK visual setup integration

Buddy source
`ec2897bec86c981bf3f6ff8f38081ac2a4aea9c4`
(tree `b2d195d49afad6a3e864c0b150356502884f1d81`) implements the
[selected contract](resident-visual-setup.md) using SDK
`f03cc7227d6b32213d6d49ae8c61a1cef6d43711`. SDK CI
[40786319432](https://github.com/s116821/ReMarkableOpenSDK/actions/runs/40786319432)
passed at that SDK commit.

The explicit development mode obtains two separate visual-only images through
the owned Runtime, with one same-child reconnect per request. Before/after PNGs,
strict receipts and phase bindings are pinned; runtime/service/candidate admission
closes after file IO and immediately before completion markers. Ready also rejects
premature later phases. Both participants validate the image pair and recheck
progress before acquiring fresh input. Source capture retains its separate
ReaderFacts checks, deadline and final reconnect.

The controller adds a fixed after-image request role. Existing historical-ready
recovery remains independent of later image success: an after-image failure does
not erase the retained proof that both original input admissions ended. Visual
capture neither creates mutation history nor reconciles an earlier uncertain
effect. Original protocol-v1/v2/v3 journal bytes and digests remain preserved.

## Source and owned-process evidence

Final frozen source passed in the owned Linux root container:

- Full all-feature library suite: 776 passed, 26 explicitly ignored.
- All setup controls, including protected-root cases: 11 passed, none ignored.
- Strict all-target/all-feature Clippy, formatting and whitespace checks.
- Independent source review accepted the final publication and ordering controls.

The preceding resident-wide run passed 199 tests including the protected-root
runtime/supervisor controls. Final ordinary tests cover the actual Runtime/peer
command sequence `CaptureVisual, CaptureVisual, CaptureSource`, four distinct
handshakes with one retained child identity, full pixel comparison, refusal before
dispatch, corrupt/truncated responses and retained uncertain mutation history.
No Observe or effect request is inserted into that capture sequence.

Final setup controls inject admission loss after image IO and after ready JSON
sync, plus one-shot premature completion before the before/ready/after markers.
They require the intended phase-order error, correct retained markers and no fresh
input admission. They also cover partial/changed/misbound artifacts, duplicate
operations, after-capture refusal and unchanged setup clocks.

Earlier diagnostic failures remain retained: two stale current-revision assertions
expected v3 rather than v4, and one host startup attempt returned text-file-busy.
The assertions were corrected and original v3 mutation fixtures added; the startup
case passed in both subsequent runs. A review found an early-completion test could
fail on its second injection rather than ordering; the final one-shot test requires
the intended rejection. Earlier runs do not substitute for the final controls.

## Remaining qualification

The developer driver still needs a separately reviewed update to retrieve and
inspect these SDK image receipts, request the after-image and require its inspection
before completion, including deliberately selected no-input setup. Fresh compiled
Buddy artifacts, a clean recovery fixture and a new candidate remain necessary.
The observer's new profile/library pins refer to the reviewed SDK wire-v4 build;
that build has not been transferred or run on the tablet by this increment.

No tablet execution, input or service changes occurred. Actual native visual/source
capture, creation/reuse, installed Reader/Writer/blank-start, writing/reopen,
preservation, lifecycle and final simulator acceptance remain open. All coordinated
PRs stay draft; the change remains unarchived.
