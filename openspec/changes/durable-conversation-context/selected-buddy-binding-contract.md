# Selected Buddy binding and Reader inspection

Status: bounded local integration contract, pending independent review and code
verification. Native transfer/activation, qualified reuse, insertion, adoption,
installed Reader bootstrap and the full REM-37 lifecycle remain unfinished.

## Existing authority and ownership

Use the existing Store, `Ledger.binding_id(document, page)` UUIDv5 key and
`SelectedAdmission.with_current(accepted_token, ...)` gate. Do not add an identity
registry, select from all-history heads, or change binding CAS/journal ownership.
Main owns this integration in the existing REM-37 checkout. Eight dirty native
and Cargo files plus existing untracked tools are protected byte-for-byte; the
bounded edit excludes them. No native operation follows from these local checks.

Source basis: current REM-37 Rust `3fb580ca38d14c9f1a525a64a242c6e57e5c30df`,
existing selected admission/projection, Ledger binding and Workflow facade;
SDK committed pin `d01b4bd` and separately protected Cargo WIP `5c0bc303` expose
the same public PageObservation/PageKey and UUID byte access used here. Current
REM-25 decision models at `dbf86273` motivate the integration but are not imported
or asserted to be wired into the installed Reader.

## Selected projection

The query accepts an existing selection token, conversation ID, native document
ID and page ID. Validate nonnil identities and the selected causal closure using
the existing projection, domain ownership and complete relevant chronology.
Read exact CURRENT conversation Root and deterministic Binding heads. A
candidate requires a live Root that names that Binding, a live Binding for the
same conversation, and matching receipt conversation/document/page and existing
deterministic key. Factor and reuse Ledger.bind's existing historical receipt
validation: intended/observed target equality, nonempty fingerprints/revision/
origin, valid source, unique nonnil original order containing the source but not
the target, and exact insertion order. Imported malformed receipts refuse even
when their immutable object hashes are valid. This does not qualify their origin.
Ancestors may validate historical closure but cannot stand in
for either current head. Inconsistent or ambiguous selected ownership refuses.

The immutable result retains the original selection token, root revision,
binding revision and exact stored BindingReceipt as historical provenance. It
does not refresh the receipt, reconstruct a NativeCommitted capability, or turn
an origin string into current-device qualification. The receipt's source page
and insertion order remain historical and are not compared as a live order
oracle; legitimate later visits or page additions require their own current
device checks.

Missing Root or Binding in the selected closure is explicitly unresolved.
`SelectedRecords` supplies included object references, not record-key absence
coverage. Neither retained losers nor ordinary Store heads fill those holes.
Tombstones, unbound/bound-elsewhere roots, foreign claims and broken links remain
unresolved or errors, with no conversion into an unclaimed/non-Buddy page.
Malformed closure, forks, stale or foreign selection tokens and incomplete
chronology fail before returning a candidate.

## Actual Reader consumer

Add read-only inspection through the existing Workflow selected facade. It
explicitly requires Synthetic origin on both original and supplied fresh SDK
PageObservations, refusing any future unsupported origin. It compares them fully, including
opaque SDK scope/visit/input/order facts through public equality, and validates
current-page membership and unique nonempty order. Convert public SDK UUID bytes
losslessly to the existing domain UUID type. Query the facade's existing
SelectedAdmission, binding the historical candidate to that exact observation.
An unbound Workflow or failed request refuses; it cannot reach legacy fallback.

Candidate fields remain private with read-only getters; the observation and
requested conversation stay bound to the selected evidence. The supplied
observation comparison is a consistency check, not a freshness
oracle: SDK observations at the inspected pins are synthetic. No new observer,
native issuer, mutable device input, navigation, capture, rendering, provider,
publication, adoption or insertion occurs in this API. A successful candidate
is historical association evidence only, distinct from a reusable/native target.
The returned token must be checked again on a later read; retaining the result
does not hold admission or grant an effect permit. Existing controlled Reader
context and synchronous effect admission remain the sole submission boundary.

## Acceptance and verification

Invoke the actual Workflow consumer using a real Store and SelectedAdmission,
with a recording mock DeviceBackend behind the existing facade. Check exact
candidate root/binding revisions, token, receipt and observation; preserve Store
selection and assert zero device calls on success and refusal. Reopen the Store
and reconstruct admission to verify durable lookup without historical fallback.

Exercise retained/all-history competing bindings, selected omission, current
tombstones over valid ancestors, foreign claims, unbound/bound-elsewhere roots,
current link mismatch, causal fork, broken/incomplete chronology, ambiguous
document ownership, malformed imported historical receipts, stale/replaced/foreign selection, foreign SDK instance or
visit/input/order drift, and invalid current membership. Known current candidates
must not inspect a successor or emit any navigation. These are scripted local
integration checks, not native display/recovery or installed end-to-end proof.

Run focused Rust tests and ordinary non-mock library check with unchanged Cargo
inputs; use the existing normal compiler environment. Check formatting only for
owned source files and verify every protected hash after edits and tests.
Independently review source/test/spec agreement and validate central OpenSpec.
Record any existing environment or protected-WIP build failure honestly; do not
hide WIP or change dependencies to manufacture a clean result.
