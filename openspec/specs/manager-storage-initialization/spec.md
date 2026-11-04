# Manager storage initialization

## Purpose

Define deliberate preparation of configured Buddy-owned storage in both Manager companions, including bounded dispatch, honest uncertainty and shared operation ownership.

## Requirements

### Requirement: Deliberate configured owned-storage preparation
Both Manager companions SHALL offer a distinct policy-reviewed, explicitly confirmed preparation using only the existing fixed no-input Initialize command on the same verified wired target. Review SHALL describe normal owned storage creation/recovery, possible owned staging cleanup and current configured-root prerequisites, without claiming an empty Store, read-only behavior, path/configuration reservation or repair counts. No mode choice, service stop, provider/native activation, configuration editing, arbitrary path or restore SHALL follow. Existing saved-mode/Local-only capabilities SHALL retain their narrower contracts.

#### Scenario: Clean tablet with configured Buddy paths
- **WHEN** a supported connected target has a valid existing configuration and the user deliberately confirms the unexpired preparation policy
- **THEN** the host dispatches Initialize once and admits only its validated complete success, without asserting that a new Store was created or Local-only/runtime/cloud is ready.

#### Scenario: Existing or refused owned structure
- **WHEN** initialization uses existing owned state or returns Busy/unsupported/unavailable/corrupt output
- **THEN** normal producer recovery/refusal rules remain authoritative, existing mode is not changed by this capability, and no fallback or service stop occurs.

### Requirement: One dispatch with honest retained uncertainty
Each host-issued policy reference SHALL allow at most one possible Initialize dispatch. Pre-dispatch expiry, session change, cancellation or Busy SHALL not dispatch or disturb another owner. Any incomplete, lost, malformed, nonzero, cancelled or non-ok result after possible dispatch SHALL retain an unknown original rather than assert no changes. A separate fixed inspect SHALL observe current metadata only, never settle that history or trigger initialize/retry. Finite eight-record and thirty-two-invocation limits SHALL refuse without eviction or renewal; a same-target unknown SHALL block a new preparation in this capability within host lifetime.

#### Scenario: Successful setup followed by output failure
- **WHEN** storage may have been created/recovered but the successful report is absent or untrusted
- **THEN** both companions retain unconfirmed setup and later matching current storage cannot relabel it successful or grant another automatic Initialize.

#### Scenario: Duplicate or stale confirmation
- **WHEN** confirmation repeats, queues after consumption, expires or belongs to an old target/boot/epoch
- **THEN** no second writer is invoked and late output cannot restore authority or erase the original outcome.

### Requirement: Closed private admission and shared ownership
Both real host factories SHALL validate strict bounded requests/results, fixed Initialize/inspect reports and private snapshot/token/binding structure before reducing to only current saved-mode kind. Public data SHALL expose no private identities, tokens, raw output, paths, configuration, payloads or arbitrary diagnostics. Shared maintenance ownership, remaining deadlines, response epochs, renderer generations and targeted cancellation SHALL preserve all peers and Local-only uncertainty; a stale timer/finally/cancel SHALL never affect a newer owner. No direct Buddy API or product WLAN transport SHALL be introduced.

#### Scenario: Competing operation or delayed setup result
- **WHEN** a maintenance owner is active or a setup result arrives after Stop/refresh/disconnect/page lifecycle invalidation
- **THEN** Busy performs no competing I/O/invalidation/cancel, stale data is not delivered, and only the original invocation can be cancelled or released.

#### Scenario: Private or malformed raw metadata
- **WHEN** an initialize/inspect report carries valid private authority or violates operation/framing/UTF8/duplicate/closed-shape/status/bounds rules
- **THEN** the host validates privately and exposes at most a safe saved-kind observation, refusing malformed output without widening the old parser or displaying protected fields.
