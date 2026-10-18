# Provider cancellation on actual main

## Why
Current Buddy main5f89060 still joins its blocking provider worker after progress rejects a pending request. Port the already accepted provider cancellation implementation2a510e825822d3683176fe5607efa6cf6f804e69 independently, preserving original stacked PR43/Docs35 and their RED/GREEN evidence. This is not a new cancellation framework or whole REM-40.

## Scope
Only src/llm/openai.rs, tests/provider_cancellation.rs and the required Cargo dependency/lock successor. Preserve main's numeric-only usage logging/response privacy, timeout/default model/request body, existing SDK absence/pins and all unrelated paths. No Reader/domain/Store/schema/native/config/prompt change. Keep genuine current-main failure before repair.
