# Buddy-page recognition and reuse before insertion

## Authority and ownership

The October11 human clarification requires Buddy-page identification to remain in the product workflow. REM-25 owns automatic page creation/acquisition/reuse; REM-37 owns durable identities and binding storage; REM-38 owns one Buddy page per conversation. Raw SDK insertion capability does not implement duplicate prevention. This clarification is a planned product requirement, not evidence that the existing production renderer implements it.

Reuse the existing planned REM-37 deterministic document/page-to-conversation binding in the Store, not a second registry. Reviewed source: durable-conversation-context/design.md section3 and conversation-context/spec.md Qualified page binding with full-head CAS at Docs1049375fc8d9e92342ef430e99696408e00a2202. That lane is separately delivered; its current-worktree design is not a claim of merged production behavior. Runtime lookup uses verified native IDs; legacy header-only pages require explicit REM-25 acquisition/adoption. Restored/imported associations do not themselves authorize current-device native actions.

## Required product decision

Before automatic insertion, resolve whether the current page is already the relevant Buddy page. If it is, reuse it without insertion or an unnecessary successor inspection. Otherwise retain the ORIGINAL source document/page identity and current exact order, then resolve its immediate successor. If that successor is already the relevant Buddy page, reuse it instead of creating another.

A known Store binding may avoid an unnecessary visual inspection when its document/page/conversation association is current, unambiguous and reconciled against fresh native identity/order and current-device qualification. Reject conflicting/tombstoned/reassigned claims, missing pages, changed placement and stale qualification as reuse authority. A saved page index is not stable identity. This is a small existing domain binding, not a ban on associations or a new registry subsystem.

Unknown or stale associations fall back to Buddy-page recognition. An ordinary guarded swipe and fresh check are acceptable when successor pixels must be inspected. Missing binding is UNKNOWN, never proof of a non-Buddy page. Missing header cache, capture/recognition failure, unfamiliar content or unresolved relevance also cannot justify a duplicate insertion. Legacy recognition may identify a candidate requiring qualified adoption; it does not silently create a trusted Store claim. An arbitrary blank screenshot alone is not proof of Buddy ownership or absence. No automatic effect follows an uncertain classification; preserve current content and report the unresolved decision.

Only after the relevant current/successor reuse cases are ruled out by qualified identity and recognition may the product create a new Buddy page. Insertion is anchored after the ORIGINAL source and before its existing confirmed non-Buddy successor, regardless of which page is displayed after inspection. Revalidate document/session/source identity and exact order immediately before publication; preserve source, neighbor and all user ink. At a verified end of document, insert after the original source. A moved/deleted source or changed neighbor/order invalidates the planned placement rather than shifting it to the inspected page. Intended target, exact expected order, durable native result, actual displayed page and subsequent binding remain separately qualified; callback alone does not authorize rendering or a trusted claim.

## Current implementation and qualification limits

The inspected production render_answer in src/workflow/orchestrator.rs always navigates to the successor before classifying it. Existing classifier in src/workflow/mod.rs recognizes a matching cached top150-pixel header as ExistingQA, masked white pixels as Blank, and otherwise Invalid; a nonblank page without a readable cache is Invalid. It can append to a recognized successor and initialize an eligible blank successor, but does not demonstrate current-page reuse, a verified document/page binding resolver or automatic insertion between an original source and a non-Buddy successor. Those are explicit product gaps. Legacy manual blank-successor fallback remains separately limited by the REM-25 roadmap and is not permission to repurpose an arbitrary blank neighbor in the automatic path.

The development native insertion harness and owned relative-gesture qualification are lower-level capabilities. They must not be labeled completion of this product precondition. In the current eight-page fixture, preserved9005 target4c8a847e-0eb8-4cf3-a747-77952d56445a is a known candidate from exact source/creation evidence, but lacks a qualified product conversation binding and rendered Buddy header. Registry absence does not establish that it is a non-Buddy neighbor. Product acquisition/reuse/adoption must resolve that candidate before selecting a new product insertion. A separately authorized primitive insertion experiment, if selected, remains explicitly capability-only and cannot substitute for duplicate-prevention acceptance.

Root preserves9005 for those reuse/adoption cases. A later fresh same-running primitive insertion/navigation test may use an independently verified ordinary source/ordinary neighbor pair or a separately prepared disposable copy of the already-authorized technical-paper material, whichever is simpler. That selection requires its own exact identity/order/backup/source/artifact contract and advance device notice; no fixture is selected by this document. Never delete or roll back the existing candidate to manufacture insertion eligibility. Native primitive investigation need not wait for the entire conversation domain, but remains distinct from product duplicate-prevention and binding/adoption qualification.

## Acceptance cases and persistence

Verify current relevant Buddy reuse with zero creation; immediate relevant successor reuse with zero creation; valid association lookup reconciled against current order; unknown/stale association recognition fallback; legacy unbound candidate adoption without duplicate creation; missing binding or uncertain recognition granting no insertion; and confirmed non-Buddy successor insertion between ORIGINAL source and that neighbor even after a visual inspection. Changed order/source/session must refuse before publication. Tests distinguish synthetic decision fixtures from actual tablet qualification and preserve both original pages and saved ink.

Record this clarification in the central Docs change and current Mem handoff. Root reports Linear reauthentication is blocked; no issue comment has been posted. Canonical as-built reader-answer-pages remains the implemented baseline until the separately checked product integration satisfies these gates. The terminal-release source fix continues against its exact c2c6dc5 owning freeze; this product clarification does not retroactively alter old gesture or insertion trials.

Source basis: current human clarification relayed by Root, current inspected repository code/specs/roadmap, and the explicitly reviewed REM-37 planned binding design. Registry reconciliation as an inspection-saving option is assessed design, not implemented evidence.

## Native recognition without fixture PNGs

Exercise an explicit RM2 portrait recognition mode with no expected PNG
digest. Binding inspection still comes first. For a page with no claim,
require a bounded, identity-stable saved RMv6 scene with validated zero-text
PageInfo and the observed supported ink/metadata blocks. Corroborate that
scene with a fresh identity-bound native capture whose stock heading area
is clear. A saved text root, unknown scene, occluded heading area, missing
file, or conflicting association cannot authorize insertion. This first
qualification covers plain notebook pages with the observed viewport.
For an original PDF page, require a matching native ordered page table and
an in-range, unique redirect to the original PDF. Require the corresponding
PDF file and a fresh capture of the exact native page. Read the saved RMv6
annotation scene if present. A known zero-text annotation scene or no
annotation file is admissible only after the original redirect is established.
Typed or unknown annotations, duplicate redirects, and changed saved assets
refuse. Other viewports and legacy adoption require separate evidence.

The installed path also recognizes a handwritten stock PDF note page in the
same portrait best-fit layout. Require an unredirected, untemplated record in
the exact live order, at least one valid original-page redirect, stable backing
PDF bytes, and a stable supported no-text scene for the note. The fresh capture
must show visible body marks and a clear heading area. Blank, typed, and
unfamiliar inserted notes remain unresolved.

## Explicit installed adoption of an adjacent answer page

An operator can queue one `adopt-legacy-page` request through the installed
binary's local `--writer-note` command. The approval identifies an operation,
the live activation, document, original source, immediate target and SHA-256 of
the saved target scene. Pass JSON on stdin with `command` set to
`adopt-legacy-page` and an `approval` object containing `operation`,
`activation`, `document`, `source`, `target`, and `scene_sha256`.
The private slot expires after 120 seconds. Queueing
does not navigate, bind or write. The ordinary Reader request still has to
reach the exact adjacent target through guarded navigation and fresh capture.

Require a missing binding, matching native document/order, the exact approved
scene bytes and the known answer heading in the decoded native text. Consume
the operation durably before publishing the Ledger binding. Recheck scene
identity and then use the existing observation and render guards. A duplicate
operation within the activation, changed proof, or competing binding grants no
adoption. This route covers explicitly selected adjacent RMv6 answer pages.
