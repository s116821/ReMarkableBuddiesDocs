# Change: Preserve personalization documents on ordinary notebooks

## Why
The existing personalization editor backend serializes an entire typed Config and admits only legacy format1. It therefore refuses a ready ordinary notebook and can materialize omitted unrelated configuration declarations. The delivered optional preference and receiving behavior remain valid; this finite change fixes its configuration publication boundary without changing the editor protocol or prompt.

## What Changes
- Reuse the existing strict Config/raw-document validator and conditional byte-document publisher, replacing only the personalization JSON member.
- Add a narrowly named existing-only personalization admission: legacy1 remains admitted, legacy2/3 remain refused, and ready ordinary notebook4 uses the separately reviewed notebook preference gate.
- Keep all v1 selectors/input/report/public Report methods, private explicit readback, bounds and uncertainty semantics; preserve the original lease-through-readback boundary.

## Impact
Rust personalization maintenance, one private maintenance entry, focused actual-file/CLI controls and public guide; central personalization-config-contract delta. No Manager, SDK, prompt/provider, runtime restart, sync/import, new writer or configuration/storage schema changes. Implementation depends on coordinated delivery of Buddy130/Docs142 and independent precode review.
