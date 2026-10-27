# Why

The delivered Writer supports durable supplied-text drafts and joined export, but
generation still rejects document/guidance JSON above 40 KiB, retains an inline
Source record bounded to 48 KiB, and sends all selected text in one model payload.
The current history and payload limits are independent. Raising one limit would
neither process long notebooks nor preserve complete source evidence safely.

The next bounded increment processes a larger explicitly supplied normalized
document through ordered model chunks and one reduction, retaining its complete
canonical text/provenance in existing content-addressed storage. It advances the
large-notebook requirement without claiming handwriting extraction, physical
notebook completeness or native Writer interaction.

# What changes

- Add explicit budgeted notebook generation/refinement and joined-export commands
  under the existing Writer dispatcher; preserve all existing command behavior.
- Retain canonical normalized-document JSON as required immutable media, with a
  typed Source3 descriptor and non-visible Conversation3 plan/stage facts. Keep
  generic Store format 1, old Source1/2 bytes and native Conversation2 unchanged.
- Plan complete ordered selected coverage before cost: at most eight map calls
  and one reduction, with caller-declared call allowance and encoded-byte limits.
- Reuse ordinary Ledger receipts, actual Writer/export owners, provider settings
  and the delivered export uncertainty/selection guards. Replay does not resume
  paid stages or send an external effect.
- Extend maintained Writer host scenarios and actual loopback/Store coverage;
  prepare a new separately reviewed representative model-quality observation.

# Boundaries and delivery

The proposed schema allocation and each shared consumer's support/refusal matrix
require coordination with the native/source owner before implementation. Existing
storage generation3 feedback is independent of proposed payload schema3. The
[in-place adoption contract](compatibility-adoption.md) preserves current
generation identity and immutable data, requires a separately reserved unsupported
format/backup/contract revision and leaves contracts1/2 unchanged. Numerical
allocations and the complete revised precode remain acceptance gates. Existing
narrow cleanup and native receiving are not broadened into new features. The
change must add explicit safe refusal where necessary, rather than silently omit
new records. A generic blob API is not evidence that those consumers support them.

One future Source PR and this Docs PR form one implementation/review/sync/archive
delivery; no planning-only merge. The preceding Source9be88628 / Docs11090c3
delivery and its independent publication observer remain preserved. No new
model/account/tablet action is authorized merely by publishing this proposal.
