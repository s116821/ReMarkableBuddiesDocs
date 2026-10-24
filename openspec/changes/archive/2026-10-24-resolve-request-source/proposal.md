# Resolve declared source inheritance

## Why

Ordinary receiving currently requires callers to reconstruct an explicit original
turn/source reference. Durable request evidence now preserves those choices, but
neither stored selections nor page bindings identify active user intent. Several
operations for the same request can legitimately select different sources.

## What changes

- Add a read-only ordinary adapter that validates an explicit source choice or
  carries forward the choice from a caller-named prior evidence operation.
- Preserve explicit no-document and deliberate source changes. Missing inheritance
  anchors remain unresolved rather than choosing a timestamp winner.
- Require an independently supplied complete index key for original-document
  choices; leave actual retrieval freshness admission to the existing receiver.
- Add real Store/Index regressions and a public API guide, preserving existing
  receiving/evidence schemas and all held Reader/Writer integrations.

## Capabilities

- Add `source-request-resolution`: declared historical source resolution.

## Impact and limits

One coordinated Docs and Rust delivery. No new durable record, source registry,
capture membership, Store format, selected/native admission, active-intent claim,
model/research dispatch, tablet contact or service operation. This is an ordinary
data building block; automatic runtime inheritance remains separate work.
