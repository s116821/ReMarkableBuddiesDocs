# September26 retirement verification

This report covers the revised REM-9 retirement/salvage delivery, not the superseded marker matrix or integrated1.0. Full description and all18 timestamped REM-9 comments reread September26; current resume/retirement authority overrides historical pause, marker and component-local instructions. Full history remains in baseline/design/superseded tasks. Linked delivery: Rust PR27 and Docs PR3, both squash; Docs as-built merge immediately precedes Rust implementation merge after exact-pair review.

## Scope and source mapping

| Contract | Implementation / verification |
| --- | --- |
| No source feedback; preserve old recovery record | workflow/mod.rs and orchestrator.rs remove normal indicator lifecycle; backend.rs disables status entrypoints, retains startup read-only refusal; zero-stroke simulator expectations and recovery/guard tests |
| Retained request ownership | device/request_guard.rs, backend.rs NativeRequest and xochitl_integration.rs observer transfer; simulator/device.rs capture pins before work, retained keyboard pin and sticky cancellation; boundary owner-change/external-input regressions |
| Single conditional trigger dismissal/recovery | trigger_dismiss.rs, capture_recovery.rs, native_history.rs; shared production policy tests cover one-tap fresh retry, owner/native/input change, typed/untyped failure and deadlines |
| Exact capture conversion | screenshot.rs conversion/pixel tests and native capture; no Paper Pro hardware claim |
| Verified navigation | workflow/navigation.rs and xochitl_integration.rs ordered native target plus bracketed fresh pixels/chrome, input/deadline checks; readiness/negative tests and actual next/previous cases |
| Exact output/typed failures | workflow/orchestrator.rs and mod.rs, simulator scenario/error/history regressions; proposal/verification unchanged, non-ink diagnostics distinct from future visible error turns |
| Contributor/no-menu/wait guidance | Rust AGENTS.md and docs, central development-testing delta; full remaining wait audit retained in design/wait-inventory |

Final sync audit additionally corrected Shared workflow execution/Page and fault model/Corner hold trigger, whose older canonical wording still described X marks or an unconditional tap. Their new deltas describe already reviewed runtime behavior; no new behavior was introduced by this correction.

## Checks and review

Production source `f63a7f25fdae587ddbaf3efef4dffe09b5e59a73` passed independent review after request/navigation handoff findings were fixed. Diagnostic-only `e5d5b77dca37379e306130749805417d52a14343` adds guarded append-probe captures, not runtime changes; independently accepted, not run as a substitute for live Q&A. Exact e5 CI36277452777 passed all-feature Linux tests, strict lint and both cross-target builds. Local f63 optimized ARM Linux library tests146/146 passed; both release architecture builds passed. Host policy/simulator coverage includes43scenarios,12history and7localHTTP regressions; modeled elapsed time is not native latency.

## Native batch: RM2 firmware3.28.0.172, portrait

Only coordinator operated the authorized idle unpaired tablet. Installed binary was never replaced; helpers were staged separately. Every screenshot below was retrieved and visually inspected, with independent reviewer inspection of the success and restoration.

- Trigger: one known-panel outside tap positively delivered6events/2frames; accepted dismissal811.456ms. Source native SHA256 before/after `f256d30c35cef3de2a27e97b2e6f732e2e0dd9b6c024ba1108c710678a602a6e`. No allocation fault recurred: policy tests establish bounded retry behavior, not native fault reproduction.
- Cancellation: the first external tap arrived after a10s mock reply, so it is NOT cancellation evidence. The second30s local HTTP fixture received external input while pending, latched refusal, made no navigation/text, preserved source bytes, returned error, then systemd restarted once. The worker join delayed error return until30s response: safe refusal is verified, responsive cancellation is not. A first temporary unit's watchdog restart is not guard-driven restart evidence.
- Live refusal: first real proposal/independent transcription agreed; large-serif disposable heading differed from small-sans global cache. InvalidSuccessor caused one verified return; source and notes bytes unchanged. Not successful output. A missing timeout utility failed the runner before any model call and was replaced by a PID watchdog; not a paid retry.
- Controlled live success: backed up global cache, seeded exact visible disposable heading using unchanged classifier, verified ExistingQA, returned to source and ran one bounded Q&A on exact f63. Exit0, exact337char new block1511→1848, prior text exact prefix. Raw record comparison: only RootText(type7)/PageInfo(type10) changed; all26 other complete length-framed records including unread payloads identical. Source bytes unchanged. New question/answer/delimiters visible; no source status ink. Cache setup is an explicit test precondition, not a production header fix.

| Successful live span | Seconds |
| --- | ---: |
| Whole iteration | 38.724433 |
| Proposal HTTP | 4.666864 |
| Independent transcription HTTP | 1.904248 |
| Navigation completion including preparation/gesture | 5.283421 |
|337-character keyboard output | 13.844231 |
| Post-output exact native persistence | 10.395769 |

Nested spans must not be summed twice. One variable-length answer is not a matched benchmark, a percentile or first-visible-pixel measurement. The source/body/answer capture checks completed; the resulting scrolled notes viewport subsequently classified Invalid with its header offscreen.

## Restoration and remaining gates

Original document46e07fc5-a3b5-4a0d-a71c-804a999fd2c7, notesf39ae285-3e0c-43dd-b27c-866dff7a24cd and visit1:75 restored and visually inspected. Original notesSHA `c284dfd1c82694d243c6314185507e1b51b8408d3e5a30be66cfebb682176008`, cacheSHA `6faae9628f71287149719e8afb2995a667628ce783b9a3e37ae8b48a1102a323`, installedbinarySHA `caa5dd3e51e5443d665c727c4ff5730af475ec6d4d7175ef5eb3f78fab57f03b` all matched. Original reader-buddy activePID22839/NRestarts0; both temporary units inactive, no active recovery journal or account registration. Firmware/account unchanged.

REM-25/37/38 own durable binding and cross-document/scrolled-page identity. REM-38/43/35 own native exact-text/history and unknown PageInfo semantics; this append proves preservation for one fixture, not universal native schema safety or tested undo/redo. REM-40/35 own scoped HTTP cancellation/join latency. Header500ms and other explicit legacy/physical waits remain documented exceptions, not completion signals. REM-35 alone owns integrated functional/performance acceptance and1.0. Paper Pro, reboot, human gestures and personal-account sync remain untested here. Old marker matrix stays superseded, not passed.

Local evidence roots: outputs/rem9-retirement/current-f63a7f2-conditional-dismiss, f63-live-qa, f63-live-qa-seeded, f63-original-restored; cancellation logs and restoration-state.txt. They are maintainer-local evidence, not private-tool contribution prerequisites. Minimal durable images and exact pair/check links are published in PR comments; bulky snapshots, raw logs and credentials are not committed.

## Completed lifecycle checkpoint

Independent exact-pair review accepted Docs `e67f6e0516e51be0b60a8bc81bcbf89be7a7f190` / Rust `1a28dba9b17309edd7d35ff05428fd88b33465c0`: all seven canonical diffs, complete requirements/comment coverage, native evidence and preservation/restoration accepted for the revised scope. Final Rust CI36278549115 passed tests/build/lint/release policy/title; current Docs CI passed OpenSpec and both OS tooling checks. Both Bugbot runs explicitly hit a usage cap, so independent review is the recorded fallback, not a clean bot verdict. Published evidence: Rust comment5850750653 (native/images),5850763213 (pair/checks) and Docs5850763376. Two pinned images rendered in a public browser view; Summary-only bodies restored after the bot's generated addition.

Canonical sync completed before archive. `openspec archive responsive-reader --skip-specs --yes` moved only this completed retirement change; the final lifecycle checkbox was left open until that move and post-archive validation finished, then marked complete. CLI removal/large-delta lint warnings do not represent missing runtime requirements: removed legacy requirements intentionally contain reason/migration statements. Strict active validation14/14 passed before archive, post-archive canonical13/13 passed, public Docs12tests and17guidance/126blob checks passed. Superseded unchecked historical marker tasks remain explicitly historical. Final archive-only revision receives narrow review/CI before the already coordinated squash merges; this does not claim an unperformed merge or1.0 release. New REM46 upstream-action release simplification separately blocksREM35 and is not part of this runtime delivery.
