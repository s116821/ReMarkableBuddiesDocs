## 1. Implementation and source verification
- [x] Implement the bounded Store-owned normalized-source cache and exact-key rebuild/load/targeted-forget API using shared primitives.
- [x] Verify reopen/query, stale/corrupt/refusal, replacement/capacity, ownership/locking and scoped cleanup with original Windows and hosted Linux fixtures.
- [x] Verify quality, source/spec agreement, independent source review and the exact-head hosted source checks; keep integration/native limits explicit.
- [x] Sync and archive only the completed cache scope.

Final Docs lifecycle review, paired squash delivery, any necessary integration
with the independent EPUB increment and postmerge verification remain tracked
in source PR64/DocsPR60. This library does not close broader REM-4 or establish
Reader receiving, durable citation evidence, cloud sync or native qualification.
