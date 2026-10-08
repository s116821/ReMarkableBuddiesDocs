## Why

REM-41 requires verified signed local APKs and one Vellum package owner before installation can become eligible. Existing release-source preview cannot authenticate packages. Pinned upstream investigation found wrapper observation may mutate virtual packages, index parsing does not authenticate signatures, and wrapper version helpers discard packaging revisions. Qualify the actual apk tool before defining a shipping consumer contract.

## What Changes

- Add an offline host qualification harness in Manager that invokes separately supplied, pinned upstream apk-tools, without copying its GPL implementation.
- Use upstream tooling and ephemeral test keys to generate signed synthetic APK/index fixtures. Exercise signature/integrity refusal, full revision comparison, installed metadata and file ownership observation.
- Prove read operations leave isolated fixture roots unchanged. Do not invoke Vellum CLI, bootstrap or installation commands.
- Document exact tool/source/build identities, licensing boundary, observed failures and missing production producer dependencies.

## Capabilities

### New Capabilities
- `manager-vellum-verification`: bounded offline actual-tool qualification independent of product installation eligibility.

### Modified Capabilities
None. Browser/Electron preview and existing release pipelines remain unchanged.

## Impact

Manager test/tooling and public guidance only; central Docs owns this lifecycle. No shipping host transport, Buddy package producer, source handoff, official trust key or device qualification is established. REM-41/42/35 and unfinished REM-46 gates remain open. Linked Docs/Manager delivery, independent review and required CI remain necessary.
