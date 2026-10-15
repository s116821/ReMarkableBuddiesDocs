# Design

## Current source and requirements

Current REM24 description and all38 comments have been covered: prior36 were read for ordinary-mode work, and the two new Manager stdin clarifications were read before this proposal. Their profile-free Query consumer and existing Manager precode are the exact dependency. Old issue5% reserve is superseded by current1% coordination. Main owns Rust/CLI; SCRAPPY owns Manager.

## Decisions

1. Reserve the exact `-` input argument for stdin only on operation query. Existing regular-file mode retains files::safe_path and bounded files::json. Its absolute-path restriction already makes old readers reject the dash before Store; no /dev/stdin or staging fallback is permitted.
2. Reuse the existing Query type/validator and common configuration/profile/preflight/Store/execute path. Query fields remain document, text, now_ms, current_claims, max_matches, max_context_bytes; no profile discovery or domain schema is added. Preserve report_version1/status/incomplete/data and guarded Report::write_to, including selected currentness and no second report after partial output failure.
3. Stdin is at most MAX_RECORD1048576 bytes. Read at most MAX_RECORD+1; invalid UTF8/JSON, trailing non-whitespace JSON, invalid domain fields, I/O failure or oversize returns sanitized InvalidInput before Store admission/effects. Existing configuration/profile failures may return Unavailable before input consumption, as in file mode.
4. Only query accepts stdin. Inspect/mutations/setup with the marker return Unsupported without consuming input, loading configuration or opening Store. Their regular-file behavior remains unchanged.
5. Caller sends one complete UTF8 JSON document then EOF and owns its existing process/channel deadline and cancellation. The backend adds a byte bound, not a wall-clock promise. Incomplete input on EOF refuses; failure after valid input/query dispatch is not proof of no Store recovery or an undone operation. Existing stdout I/O failure/currentness semantics remain authoritative.
6. Manager's planned document:null/current_claims:[]/8matches/8192context request uses the existing configured profile. Generic report bound remains MAX_RESPONSE (MAX_METADATA+65536); Manager's smaller128KiB transport cap must refuse oversize/unknown output honestly rather than truncate or present it as empty. Old readers reject the dash with InvalidInput; the consumer must treat a known well-formed unsupported-input result as unsupported/unavailable, not empty search success.

## Verification

Use existing isolated subject-memory CLI/selected fixtures. Exercise actual piped stdin with EOF, regular-file parity, relevant provenance, malformed/oversized/invalid UTF8 before Store creation, unsupported stdin operations without reading, and selected currentness through the shared output path. Reuse existing Query and provider tests; do not create a speculative provider matrix or claim native/cloud/model evidence. Publish source/spec examples before freezing Manager implementation; complete own verification/review/CI/canonical/archive only.
