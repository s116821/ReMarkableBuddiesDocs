# Design

## Requirements audit

The existing public roadmap and Manager contracts require tablet connection and
updates, backend/model/key configuration, Reader/Writer preferences, research,
personalization, memory and handwriting management, safe owned-data maintenance,
and optional backup/sync. They do not require a top-level panel for each host
operation. Retain these outcomes and replace their presentation.

| Destination | User task |
| --- | --- |
| Tablet | Connect by USB, understand device/service state, find updates |
| Settings | Configure Reader/Writer, model connection, research, personalization and memory; transfer preferences when needed |
| Data | Inspect conversations, memory, handwriting and storage; select an item before maintenance |
| Backup & sync | Manage Google sign-in and data mode; choose export or restore with supported format handling |
| Troubleshooting | Inspect saved configuration, diagnostic settings, technical identity and unresolved results |

The Google account is the user's own account. Host sign-in is distinct from
tablet configuration and successful backup. Existing capability checks remain
authoritative; clearer presentation must not manufacture feature availability.

## Interaction boundaries

Navigation is local presentation state, not a device command. It must not silently
apply, retry or claim to cancel operations. Keep pending/unknown results reachable
after navigation. Private drafts must retain the existing controller lifetime and
clearing guarantees. Direct controls may simplify set/clear/keep terminology but
must preserve absent, explicit-empty, saved and effective-value distinctions.

Credentials and their protected file references share a model-connection context
without merging their separate write authorities. Technical references, raw
configuration reports and legacy archive support are secondary details. When
enumeration is unsupported, explain the required identifier rather than inventing
names or discovery. Destructive actions retain a preview and explicit confirmation.

## Validation and delivery

Exercise real rendered navigation, keyboard access, responsive layout and the
affected contextual workflows through synthetic browser/Electron fixtures. Keep
existing host/controller tests; change their navigation setup instead of leaving
all panels visibly present for old selectors. Inspect screenshots of the landing
page and representative settings/data/backup screens. No live Google or tablet
test is necessary for this renderer change.

Deliver a bounded change from current main, independently reviewed and checked,
with paired Docs. Reconcile open feature branches afterward so their additional
controls use the same navigation and cannot restore the long dashboard.
