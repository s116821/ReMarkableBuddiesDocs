# Durable request context evidence

## Why

The delivered historical receiving API selects local source passages and returns
an immutable request frame, but that selection disappears with its caller. The
ordinary ledger needs an inspectable record of the context selected for a request
across restart, including explicit no-document, zero-match and unavailable-media
facts. This is evidence of selection, not proof that a model consumed the frame.

The receiving delivery is complete. This change adds a separate opt-in preparation
and publication path over its existing assembly machinery and the existing Store;
it does not turn the read-only API into an implicit writer.

## What changes

- Add a bounded historical request-evidence record to the ordinary ledger, with
  the exact encoded receiving frame, source/key/passage facts, caller-reported
  admission limits/count and exact historical record references.
- Add a sealed ordinary preparation that captures a Store read set before local
  retrieval/counter callbacks, then a separate atomic publication that rejects a
  changed Store generation or relevant heads. Reuse ordinary root/receipt and
  crash-recovery semantics.
- Provide historical readback without another query, preserve evidence through
  ordinary export/import and logical conversation deletion, and refuse invalid
  or unavailable record references without inventing a replacement.
- Document and test the new data-only API with real temporary Store and Index
  fixtures, including restart, retry/conflict, omission and concurrent changes.

## Scope and exclusions

Use ReMarkableBuddies and this central Docs repository as one paired delivery.
No parallel source/history registry, capture-batch membership change, automatic
source inheritance, Writer implementation copy, model/research/router dispatch,
selected/native admission, tablet contact, service operation or new settings is
included. The retained Writer supplied-text record has a distinct purpose and
remains untouched. The existing receiving contract, SDK pin, CI structure and
previous completed deliveries remain preserved.

## Capabilities

- Add `source-request-evidence`: ordinary preparation, atomic durable evidence
  publication and honest historical readback.

## Impact

Buddy changes are limited to the ordinary conversation data adapter, shared
receiving assembly, a small private Store snapshot/publication extension and
necessary typed-record validation/compatibility. Existing selected projections
must explicitly refuse the new ordinary record; no effect route is enabled.
Central canonical sync and archival follow implementation, verification and
independent review in the same coordinated delivery.
