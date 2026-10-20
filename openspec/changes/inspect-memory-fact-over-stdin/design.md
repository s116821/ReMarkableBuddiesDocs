# Inspect stdin implementation boundary

## Source and coordination
The full memory and Manager issue chronology was read for previous delivery;
current descriptions and all new comments were reconciled, including the Manager's
single-fact request, concrete compatibility questions and coordinator acceptance.
Archive68/65 is separately delivered at029354f/8c0ae5d; its publication continues
independently. Its code, requirements and tests are not rewritten here.

Current memory::maintenance::run_stdin returns Unsupported for every non-query
operation before config/input/Store access. Its bounded parser always constructs
Input::Query. Existing file Inspect already validates Key/profile, uses ordinary
or exact selected memory admission, returns all matching current heads, and keeps
the existing Report::write_to and selected Inspection guard. Reuse those paths,
not a query-as-detail implementation or a new domain API.

## Narrow change
Admit exactly Query and Inspect before run_with_input; retain early Unsupported
for Put, Forget and all setup/registration operations, including unreadable stdin
and absent configuration. Pass Operation to the existing bounded stdin decoder.
The Query branch keeps its current decoder/validator. Inspect parses a private
strict wire Key, converts to the unchanged memory::Key and calls the existing
profile/domain validator. No operation UUID, expected heads or write token is
accepted. No new config/Store initialization or fallback is introduced.

The private wire uses {profile,scope,fact}; scope is Global{} or
Document{document} with an internal kind tag, rather than the existing unit Global
variant. Direct typed JSON decoding rejects duplicate and unknown fields at both
levels. Preserve ordinary file decoding exactly: a fresh existing-file admission
probe confirmed unknown outer Key fields refuse but extra fields in the existing
unit Global scope are ignored. This compatibility difference is explicit; do not
claim the old file decoder was fully strict or change it under this transport work.

Use the existing inclusive1MiB byte/EOF limit, config/profile validation order,
preflight and execute/report paths. Report-v1, generic8454144-byte encoded cap,
all-current-head raw-envelope semantics, currentness seals and prefix-write refusal
are unchanged. The exact DTO is in contract.md, which is also the consumer precode
reference. Consumer code remains separately owned and must validate all heads and
derived requested record identity, including null-payload tombstones.

## Meaningful verification
Actual file/stdin parity for one local and selected key: value, complete-empty,
tombstone and competing current heads, preserving IDs/provenance and all heads.
Verify absent key is not a store/refusal/global-empty substitute. Preserve raw
unsupported heads rather than silently filtering them; consumers reject unsupported
envelope/domain payloads independently. Exercise inclusive bound, EOF/truncation,
read failure, duplicate top/nested keys, extra nested global/document fields,
unknown scopes, nil/foreign profile/fact/document and no Store creation on refusal.

Retain a MustNotRead control for all mutation/setup selectors, existing query
semantics and the old file decoder compatibility. Use existing actual Store and
selected writer fixtures to prove current stdout handoff and no second report on
prefix failure, without rerunning unrelated old matrices manually. Supply a small
attributed actual producer report corpus for the real consumer parser. Run affected
CLI/maintenance tests, no-default/lint, ordinary full CI and independent reviews;
sync/archive only this completed change, followed by actual-main publication.
