# Contract review status: UNFROZEN

This draft defines intended behavior, not wire/schema or implementation admission.
Main's proposed reader_enabled, writer_enabled and export_destination fields are
under review in one optional versioned object. The current gap was source-reviewed
by Main; full exact source pin/types are still required before freezing.

## Required freeze decisions

1. Exact object name and schema revision; member optionality; absent/null/type/
   unknown/future-version handling; missing and explicit default origin; clear one
   or last field; empty/version-only object; no-op byte preservation. Do not choose
   these independently in producer and consumer.
2. Fixed CLI selectors and mutually exclusive dispatch, bounded '-' stdin/EOF,
   exact framing/UTF8/duplicates/unknown keys, statuses and complete report matrix.
3. Raw/current/public fields; original intent, operation, path/base/change/target
   hash domains and canonical serialization; no private hashes/packets leaked.
4. All Reader/Writer/export entry gates, maintenance ordering and disabled-export
   historical reconciliation that cannot cause a new provider dispatch.
5. Frozen size/deadline/ready/original/capacity/cancel bounds and all no-change,
   conflict, not-dispatched, verified, unknown and desired-file observation rules.
6. Independent literal positive/negative/custody vectors with hashes and explicit
   actual-source vs synthetic attribution. No vector-generator self-oracle.

This increment intentionally offers no private free-text destination/account/URL
or new credential entry unless the reviewed real producer changes that scope.
The Mem/Disabled choice must not close all destination requirements by wording.
