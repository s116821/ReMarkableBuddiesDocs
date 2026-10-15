## Why
The accepted actual async client preserves a10MiB response bound, including unknown lengths, but no actual-client integration test covers its inclusive boundary or early refusal. A local TLS fixture can close this gap without production changes.

## What Changes
Reuse the owned Linux TLS fixtures for three new controls: exact-bound valid answer, oversized declared length with no body, and oversized chunked response. Require exact static bound error classification, request/response/peer-close witnesses and owned cleanup. No production/Cargo/version/global-setting changes are planned.
