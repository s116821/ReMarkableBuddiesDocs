# Existing-page acquisition receipts

The current Ledger binding receipt describes insertion only: its target must be
absent from the original order and appear immediately after the source in the
observed order. REM-25 also requires qualified adoption of a relevant existing
current or immediate-next Buddy page. That case must retain the real unchanged
order rather than removing the target to manufacture insertion evidence.

## Representation and compatibility

Extend the existing BindingReceipt with a typed acquisition discriminator:
Inserted, ExistingCurrent, or ExistingAdjacent. An absent discriminator means
Inserted, and serialization omits that default. Preserve every existing field,
its order and original insertion semantics. Frozen pre-change serialized receipt
and bind-fingerprint input vectors must remain byte-for-byte identical; historical
operation acknowledgments must still replay before ordinary head checks. Do not
rewrite old stored envelopes or receipts.

Inserted bindings remain conversation envelope schema 1. ExistingCurrent and
ExistingAdjacent bindings use schema 2 with an explicit discriminator. Schema 2
already admits conversation envelopes; this extends only the Binding record's
accepted shape, alongside the existing independently validated Receipt/OutcomeFact
shapes. No storage envelope or Manager contract version changes. The Ledger must
reject schema-1 existing-page records, schema-2 insertion records, unknown
discriminators, null values and unrelated schema-2 record kinds. Older consumers
refuse the new binding shape instead of interpreting it as insertion. Root and
ordinary operation-receipt schemas remain unchanged.

## Validation and publication

All receipts retain nonnil conversation/operation/document/page IDs, exact intended
and observed target correspondence, source document correspondence, original
source identity/provenance, complete nonempty unique nonnil expected order and
the existing evidence/persistence fields. Stored fields remain historical facts;
the domain never manufactures native revisions, visits, qualification or leases.

Inserted preserves the existing one-page insertion invariant. ExistingCurrent
requires the target to equal the source/current page. ExistingAdjacent requires
the target to be the immediate next page after the original source in the complete
expected order. Both existing-page forms require observed_order == expected_order.
No duplicate, missing, nonadjacent or other-document target is accepted. A changed
order after inspection refuses publication; a returned cursor or timestamp is
not a replacement for the original placement facts.

Keep the same deterministic document/page binding key and Ledger::bind API.
Its atomic root/binding full-head CAS, create-or-identical restriction, consumed
operation fingerprint and historical retry behavior apply to all forms. Adoption
does not overwrite another conversation's claim or a tombstone, move an already
bound conversation, reconstruct missing heads, or run selection/insertion.
The existing resident journal remains the sole native-operation journal.

Historical and selected binding inspection must retain the exact discriminator
and the existing receipt validation. Selected projection and output preparation
must not accept a malformed new binding through a weaker decode path. Apply full
receipt validation to new schema-2 binding decoding while preserving the existing
schema-1 inspection behavior; validation at ordinary bind and binding queries
continues to cover both forms.

Actual product adoption still requires qualified identity/order, conversation
relevance, capture/recognition and current-device ownership outside the Ledger.
Header similarity, a missing binding or a stored receipt alone grants no native
reuse or writing permission. This increment supplies the missing domain
representation for that pipeline; it does not claim the pipeline is installed.
Existing schema-2 maintenance limitations remain conservative refusals rather
than silently dropping these records.

## Verification

Before changing receipt types, exercise the frozen v1 serialization/fingerprint
input against the old implementation. Afterward, verify the same bytes, legacy
schema and historical retry. Exercise real Store current/adjacent adoption,
reopen/export/restore, exact historical and selected candidate inspection,
changed discriminator under a consumed operation, conflicting page/conversation
claims, stale full heads, deletion followed by historical retry, and both forms
of existing-page order/target refusal. Check envelope schema/shape confusion and
unknown/null discriminator refusal. Invalid publication must leave Store
manifests unchanged. Preserve insertion tests and run the affected broader suites.

Source basis: current Ledger::bind/validate_binding_receipt and selected/historical
inspection code; the REM-25 recognition/reuse contract; the REM-37 existing binding
CAS and historical-acknowledgment requirements. This is the proposed integration
design, accepted by independent review before implementation. The implementation
and scoped verification are recorded in [existing-page-binding-result.md](existing-page-binding-result.md).
