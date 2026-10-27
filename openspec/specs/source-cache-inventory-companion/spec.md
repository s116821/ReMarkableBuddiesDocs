# Source-cache inventory companion

## Purpose

Provide explicit, bounded, read-only source-cache metadata in both Manager companions. The exact [consumer wire and lifecycle contract](../../changes/archive/2026-10-26-inspect-source-cache-companion/contract.md) defines complete validation, ownership, observation quiescence and snapshot limits.

## Requirements

### Requirement: Shared explicit bounded cache candidate inspection
Both companions SHALL expose the optional fixed identity-bound read-only source-cache inventory under contract.md, validate the complete producer report before safe reduction and preserve exact empty/refusal/bounds/metadata/no-authority semantics without payload access, cleanup or installed-version inference. Source basis: canonical source-cache-inventory and archived exact producer/manual/current source.

#### Scenario: Explicit admitted metadata or empty inventory
- **WHEN** an observed wired user deliberately requests the supported inventory
- **THEN** only the parameterless Linux producer is invoked with no stdin and a consistent0..16 sorted candidate list/apparent total or inspected-empty result is shown with unread/unvalidated/freshness/runtime/no-cleanup limits.

#### Scenario: Unsupported, malformed, changed or bounded refusal
- **WHEN** capability/report/identity/shape/flags/order/integer/sum/framing/bounds admission fails or producer refuses
- **THEN** fixed bounded unavailable/unsupported/busy/conflict/null results replace current candidates without diagnostic echo, partial/zero fallback, alternate command, repair, cleanup token or inferred freshness.

### Requirement: Nine-owner custody and retained-original preservation
The consumer SHALL use the real ninth shared owner in both factories and preserve all eight existing wires/private lifetimes/original uncertainties, with Busy before host hooks/cancel/I/O and explicit renderer private/view clearing under contract.md. Source basis: current eight-owner MaintenanceIO factories, accepted private lifecycle and producer custody.

#### Scenario: Peer ownership and admitted inspection
- **WHEN** another owner is Busy or inventory/one of eight peers starts admitted work
- **THEN** Busy grants no host side effect, admitted idle grants/private actual DOM/raw clear before relevant awaits, reciprocal stale inventory is invalidated and every old unknown/unresolved original remains independent without renewal/settlement/retry.

#### Scenario: Stopped, late or expired bounded read
- **WHEN** a user stops waiting, identity/observation changes or a result/deadline completes after supersession
- **THEN** local Stop sends no global/remote cancel or token release, the host remains bounded by its original deadline and no old result/timer/finally refills a stopped/new view or cancels/releases a newer peer.

### Requirement: Guarded shared interfaces and attributed delivery
The consumer SHALL retain strict HTTP/main-frame IPC/identity/stream/privacy admission, explicit snapshot-only UI and independently reviewed Windows/Linux source/retained qualification through its complete own paired lifecycle. Source basis: existing guarded host adapters, central contribution workflow and unchanged historical producer evidence.

#### Scenario: Untrusted surface or automatic-action attempt
- **WHEN** caller arity/frame/origin/session/body/raw-action input is invalid or no explicit inspection was requested
- **THEN** the capability refuses without broadening existing allowlists, displaying raw/owner diagnostics, polling/persisting or automatically selecting/preparing/cleaning a candidate.

#### Scenario: Exact qualified paired delivery
- **WHEN** this consumer is proposed for delivery
- **THEN** original producer/failure provenance remains separate from new72-direction/24-boundary/shared UI controls, current both-OS source/retained/byte and independent reviews precede own canonical/manual sync/archive and final normal paired delivery, with actual publication and broad REM42/MVP separately observed.
