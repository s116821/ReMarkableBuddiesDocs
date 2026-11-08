## Decision

Index ResidentCapture provider images in the existing resolver, preserving frozen
ContextView evidence and original turn-source order. Complete descriptor admission
before object reads: twelve unique attachments, sixteen MiB attached PNG bytes and
256 associations remain the existing limits. Reserve a single per-request resident
proof allowance before I/O: at most twelve referenced captures and 64 MiB total
declared original-plus-derivative bytes across them, counting repeats. Each original
must satisfy the existing resident pixel/dimension bounds; total original pixel
work is bounded by twelve times that existing limit. No allowance resets per capture.

Call Ledger::resident_images_from_evidence with frozen evidence and exact object
loads. It validates original/derivative media and historical correspondence, then
rederives overview/strips and compares exact bytes. Only returned provider images
are cached/attached; original PNG is provenance only. Reuse validated returned
bytes rather than reread a current head or mutable object for attachment.
Digest deduplication preserves every source/ordinal association, including shared
resident derivatives and other source kinds. Missing/corrupt/false-recipe or
resource-exhausted evidence refuses before model dispatch, never degrades to text.

## Verification and Ownership

Use actual ordinary Reader, Writer Generate/Refine and notebook reduction receivers
and maintained scenarios. Seed explicitly synthetic ResidentHistoricalUnqualified
history, not a current native lease. Preserve raw receiver histories, derivative
hashes/association order, reducer digest and retained drafts. Exercise missing parent,
changed derivative, false recipe and cumulative bounds before any model call.

Extend the existing qualification runner with an explicit resident fixture/case,
retaining its seven-call, ninety-second-per-call and 720-second overall limits,
protected configuration admission and stop-on-failure transport. Offline runs use
no credentials. Live execution requires independent review of the exact inputs.

The correction covers ordinary receiving and scoped simulator behavior. It grants
no acquisition or native authority and qualifies neither native output, Submit,
currentness, handwriting quality nor aggregate integration.
