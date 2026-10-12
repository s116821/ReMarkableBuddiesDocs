# Selected Buddy binding integration result

October 12, 2026. The bounded local Store/Reader inspection increment is verified;
REM-37 and the MVP remain unfinished. Native transfer/activation stays held.

## Source and checked inputs

- Rust: `7b207ec8a42548c12960699854107236eb2bbd7f`, six scoped files over
  `3fb580ca38d14c9f1a525a64a242c6e57e5c30df`.
- Precode central contract: `7cadff4c2a176356f118e274da1f69c1c9a1abe6`,
  independently reviewed before source changes. The additional existing-domain
  MAX_ITEMS order bound was documented before its implementation and separately
  reviewed.
- Exact committed source uses SDK
  `d01b4bdfbc4dc11673f84ff82bbc62c8dc77bbb1` and its committed Cargo.lock.
  A normal Git archive build input verified those Cargo files and all six changed
  sources plus the protected native counterparts against committed Git blobs
  after standard Windows Git CRLF conversion. It is not a new Git checkout,
  worker, native packet or release artifact.
- Local source archive SHA256:
  `701918e1c9986edfbc466c221a6305c032764c7684194d4bd249345614546c11`.
  Expected development Git-metadata warnings remain explicit.
- The existing working checkout separately retains SDK Cargo WIP
  `5c0bc303bb9b22e8e01bce9b2bd2a7fe47c8010e`. Its eight dirty tracked files and
  one untracked tool were hashed before and after edits/tests/commit and remain
  byte-for-byte unchanged. None was staged, committed or used to claim a clean
  committed-source result.

## Implemented behavior

`SelectedAdmission.inspect_buddy_binding` uses the existing token-checked gate,
selected causal projection and deterministic Ledger binding key. It requires
exact live current Root/Binding heads, their conversation link, valid historical
receipt semantics, consistent document ownership and complete relevant chronology.
The receipt validator is factored from existing `Ledger.bind` without changing
its fingerprint/replay/operation/CAS order or general decoder behavior.

Selected absence, deletion, an unbound/bound-elsewhere root or another conversation
claim remains unresolved or refused. Neither retained records, all-history heads
nor a valid ancestor can replace a missing/deleted/foreign current association.
No record-key absence coverage is inferred.

The actual Workflow selected facade consumes this Store query using complete
matching supplied SDK observations, explicit Synthetic origin, lossless UUID
bytes, unique nonempty current membership and an existing-domain order bound.
Private immutable results retain the exact SDK observation, selected token,
root/binding revisions and original receipt. They are historical candidates,
not reusable targets, live NativeCommitted receipts or Reader effect contexts.

## Observed verification

Final committed-source Windows x86_64 checks used Rust/Cargo 1.98.1:

| Check | Actual result |
| --- | --- |
| `cargo test --locked --all-features --no-fail-fast` | PASS; 273 library tests passed, one existing test ignored; all binary/integration suites and compile-fail doctest passed |
| Fourteen new focused controls | PASS within the exact committed-source full suite; separately PASS in the preserved WIP checkout |
| `cargo check --locked --lib` | PASS on exact committed SDK pin, with 24 existing unfinished-bootstrap warnings |
| Formatting of the six owned source files; scoped diff check | PASS |
| `cargo clippy --locked --all-targets --all-features -- -D warnings` | FAIL on the same 24 existing unfinished-bootstrap dead-code errors; no waiver or suppression |
| Central Docs unit suite / manifest and guidance checker | 12 tests PASS; checker PASS |
| Strict central OpenSpec validation | 16 items PASS |

Tests invoke the actual Workflow facade with a real Store and recording mock
DeviceBackend. They verify exact receipt/revision/token/observation after Store
reopen; selected winners against retained/all-history competitors; omitted heads;
current tombstones and a foreign current head above a matching ancestor; unbound
and bound-elsewhere roots; ten malformed imported receipt variants; incomplete
chronology, ambiguous ownership and broken links; changed/foreign tokens; opaque
SDK instance/input/session/visit/order drift; request failure; and oversized order.
Known candidates make no successor lookup or device action. A returned candidate
cannot dispatch without the separate actual Reader context.

Each actual inspection asserts zero calls on the wrapped mock backend, unchanged
selection and hashes of every durable Store file except the Windows-exclusive
`store.lock`, whose inventory/length is checked. The Store fork control is separate:
initial publication refuses before a selected transaction can exist and may leave
only immutable unreferenced objects. The SDK invalid-order/membership controls
are also upstream refusals before a public opaque observation can be issued;
they are not misreported as Reader execution with fabricated observations.

The existing independent Sol reviewer accepted source/test/spec agreement and
the separate order-bound amendment without blocking findings. That read-only
review is internal project chat evidence; no public review transcript is claimed.
The reviewer did not edit or rerun the broad suite; execution results above are
Main's current tool outputs.

## Remaining gates

This is a production-source read-only consumer exercised locally, not an installed
end-to-end Reader/bootstrap or a native adapter. SDK observations remain synthetic;
supplied equality is no freshness oracle. Restored receipt origin/order/timestamps
do not qualify the current device. No provider, capture, render, navigation,
adoption, insertion or publication follows from inspection.

Qualified native binding/revisit, SourceAdmission/SettlementVerification adapters,
installed bootstrap, actual insertion/display/recovery and the broader SDK/Reader/
Writer integration remain open. Strict lint and current target/release/native
checks are not passed by this increment. Broad tasks stay unchecked; no canonical
sync, archive, merge, release or Done claim follows.

Source basis: current repository/source, actual committed-input local tool outputs,
fresh REM-37 description and all 37 accessible timestamped comments (no newer
requirement since October 9), and independent read-only review. Historical device
reports are not reused as proof for this code.
