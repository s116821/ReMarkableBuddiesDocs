# Design

## Source basis

The current REM-53 description and all thirteen accessible chronological comments were read. Actual main::logging enables Debug for remarkable_reader_buddy by default. Existing provider and Reader source explicitly formats full response JSON, independent reading, question, answer and rendered text into routine logs. This is a concrete current caller issue, not an inference that every response contains a preference.

## Decisions

1. Keep useful stage/length/count diagnostics, but never pass raw response, transcription, question, answer or rendered text to those normal log calls. Preserve existing default log configuration.
2. Read only known usage counters as unsigned integers. Unknown, string, object or invalid usage values become absent counters, not formatted JSON. Actual response parsing/output behavior remains unchanged.
3. Use the maintained live-simulator CLI harness with an owned loopback HTTP server, dummy credentials and declared replies. Clear the child's RUST_LOG so the regression exercises the real default logging policy. Put distinct synthetic canaries in question, answer and provider metadata; require no canary in stdout/stderr and exact user content in report/output.
4. Retain a failing run against unchanged production logging before the fix. Run only the new focused regression and affected existing parser check locally, then required strict lint/hosted checks. Do not repeat unrelated cancellation/TLS/size matrices.

## Limits

The regression is actual CLI/HTTP and synthetic provider data, not live semantic or native evidence. It is not an exhaustive audit of every third-party or error log. Intentional source/conversation evidence, output reports and explicit debug screenshot files remain content-bearing by design. The bounded change does not qualify runtime reload/Writer/native behavior or close all REM-53.
