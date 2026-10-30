## Why
REM-4 requires external research by default. The saved policy and research context
stage exist, but no concrete Provider acquires web evidence. The current OpenAI
engine posts Chat Completions without search options and returns only message text.
A declared evidence callback is not a delivered search backend.

## What Changes
- Add an explicitly selected OpenAI web-research Provider, separate from answering,
  using the existing request/context/result seam and maintained HTTP dependencies.
- Require actual hosted search-call witnesses and source-URL correlation, strict
  bounded provider-asserted evidence and owned cancellable request cleanup.
- Exercise real HTTP transport locally and bounded actual hosted acquisition before
  claiming provider support; preserve exact context, opt-out priority and old APIs.

## Scope
Main owns backend/acquisition and paired Docs. Existing runtime/gesture/native and
Manager drafts retain their owners. No automatic runtime selection, new saved
settings/credentials/schema, SDK/dependency/workflow migration or tablet work.
