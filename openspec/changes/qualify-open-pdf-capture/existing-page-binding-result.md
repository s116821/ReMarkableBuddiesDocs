# Existing-page binding integration

Buddy `7541c01d20cc03a87a0bceadbd7563f4035deb6b` implements
[the existing-page binding contract](existing-page-binding.md) in the existing
Ledger API. `ExistingCurrent` and `ExistingAdjacent` retain unchanged page order
and exact current/immediate-next correspondence. They use schema-2 Binding
envelopes with an explicit acquisition discriminator. Old insertion receipts
remain schema 1 and omit the default discriminator.

The frozen insertion JSON and bind-fingerprint input passed against the prior
implementation at `deb863b9a2b8cd94893d7b04eac635ecb5472706` before the type change.
They remain byte-for-byte identical afterward. Existing operation replay,
deterministic page keys, full-head CAS, conflicting claims and tombstone behavior
are unchanged. New schema-2 bindings pass full receipt validation in the common
decoder, including selected projection; malformed records cannot reach Reader
actions through a weaker projection path.

Independent design and implementation review accepted the change with no blocker.
On October 25, the final source passed these Windows checks:

- `cargo test --locked --test existing_page_binding --test conversation --test historical_association -j 1 -- --test-threads=2`: 33 tests.
- `cargo test --locked --lib workflow::selected_buddy -j 1 -- --test-threads=2`: 16 tests.
- `cargo clippy --locked --all-targets --all-features -j 1 -- -D warnings`.
- `cargo fmt --all -- --check` and `git diff --check`.

Coverage includes all three acquisition forms through real Store publication,
reopen/export/restore and historical retry after deletion; stale heads and
competing conversation/page claims; changed acquisition under a consumed
operation; invalid target/order/schema/null/unknown forms; unchanged manifests
after refused publication; exact historical candidates and selected-path refusal
before device calls. An initial test assertion required Debug on Envelope and
failed compilation; it was changed to equality without Debug, then the full
affected suite passed. No production type was changed to accommodate the test.

Both affected OpenSpec changes pass strict validation. The documentation manifest
check passes with 25 current guidance files and 126 preserved source blobs.
Hosted validation for the new Buddy commit remains pending at this checkpoint;
previous CI is not credited to it. Windows Store tests do not establish Linux
power-loss behavior or native tablet qualification.

This supplies historical representation for qualified adoption. The installed
Reader still needs current/adjacent recognition, native acquisition, binding,
capture/write/persistence and runtime recovery integration. Resident ReaderFacts
cannot be converted to synthetic PageObservation or invented visit/revision
fields to fill that gap. Existing schema-2 maintenance refusals remain intact.
No tablet action, production capability promotion, merge or archival occurred.

Source basis: current implementation and spec files, independent source review,
and directly observed test/compiler output. Native acceptance remains separate.
