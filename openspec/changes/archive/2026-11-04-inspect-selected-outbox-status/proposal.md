# Inspect local selected outbox status

## Why

The existing selected-attempt inventory validates original local journal
custody, but callers outside the Buddy process have no bounded versioned
report for that inventory. Expose counts of locally recorded pending and
withdrawn attempts as a narrow part of file/OS-readable sync management.

## What changes

- Add a fixed exclusive no-input Buddy inspection selector for existing
  supported Store layouts.
- Return only complete validated pending/withdrawn counts, or a sanitized
  Busy, unavailable, corrupt or unsupported result.
- Preserve journal bytes, output custody and the distinction between local
  records and current transmission, cloud, retry or native authority.

## Capabilities

### Modified Capabilities

- `document-scoped-buddy-sync` adds a bounded local outbox status producer.

## Impact

Buddy maintenance and central contracts only. No Manager transport/UI, new
Store format, selected publication or retry, provider calls, credential
contents, tablet execution, or restore. The parent document-scoped sync
change and its nine end-to-end requirements stay open.
