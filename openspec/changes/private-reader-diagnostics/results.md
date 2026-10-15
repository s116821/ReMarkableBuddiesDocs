# Private Reader diagnostics: local evidence

## Revisions and implementation

Full precode fdb4b3c was published before implementation. Source11f6aac7125fa736b715911388428a9db3afbad1 changes four files over accepted Reader cancellation6fea00fcf77b18960f278789b0dae50fab8b67b8: provider diagnostics, Reader orchestration, render-text diagnostics and the maintained actual-CLI HTTP fixture/regression. No Cargo/SDK/configuration/prompt/request/output changes. The prior reviewed personalization and cancellation branch heads remain intact.

Provider response JSON and arbitrary model/usage metadata are no longer formatted into routine logs. Only recognized unsigned prompt/completion/total usage counters remain. Reader analysis, interpreted question, independent reading and render text log stage/byte counts rather than their contents. Exact returned and persisted text is unchanged; intentional evidence files remain content-bearing.

## Actual Windows evidence

Rust1.98.1, locked/offline/all-features, one Cargo job. Dummy credentials and an owned loopback HTTP server; no external provider/model call:

- Original expected-correct default-log privacy check failed17.72s on unchanged production logging. The actual default app logger emitted the synthetic question, answer, provider-model and string/object usage markers through response JSON and Reader status logs. Output assertions had passed and both owned requests completed; the failure was the privacy assertion. Raw original `private-reader-diagnostics-red-r1.log` is retained.
- After the three production log-only changes, the focused CLI regression passed7.54s, zero ignored/seven old tests filtered. The canary checks are unchanged; the positive numeric-usage assertion was tightened to the exact named counter. Both requests completed, actual report assertions passed and the rendered answer retained the exact question/answer. No marker appeared in stdout/stderr; recognized total_tokens23 remained diagnostic. Raw `private-reader-diagnostics-green-r1.log` is retained.
- Existing affected response-parser check passed once0.00s; invalid/missing content continues to return sanitized errors without panic or response echo. Raw parser log retained.
- Final all-target/all-feature strict Clippy passed19.11s; formatting/diff checks passed. Raw lint log retained. Unchanged cancellation/TLS/response-bound matrices were not repeated locally.

No image/output renderer was changed, so the regression checks exact report text and diagnostics rather than introducing a new visual fixture. This is synthetic provider data through actual HTTP/CLI, not live semantics, handwriting recognition or native typography proof. It is not an exhaustive third-party/error-log audit. Required hosted checks, independent source/spec review, current feedback and own canonical synchronization/archive remain open at this snapshot.
