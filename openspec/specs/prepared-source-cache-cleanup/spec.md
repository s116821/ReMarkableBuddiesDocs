# Prepared source-cache cleanup

## Purpose

Provide bounded original-bound cleanup of one owned derived source-cache slot, with explicit Linux capability and no durable-history or runtime authority.

## Requirements

### Requirement: Nonmutating bounded one-slot cleanup preview
The source-cache maintenance CLI SHALL inspect and prepare exactly one canonical
owned normalized-source slot using validated existing ordinary Store and cache
namespace header/lease custody without constructing/recovering Store, enumerating
or reading durable payloads, creating, repairing, chmodding or cleaning files. It
SHALL reject unknown/unsafe/staging entries and expose no source content or
freshness authority. Credential contents, original documents and unrelated owned
categories SHALL remain outside this operation.

#### Scenario: Preview a present slot or refuse an unsafe namespace
- **WHEN** a caller selects one canonical UUID in a supported existing namespace, or ownership/path/lock/bounds checks fail
- **THEN** preview returns bounded fixed metadata and a private exact-original intent only when admitted, or an explicit nonmutating refusal; no cleanup permission follows from generic size inspection.

### Requirement: Exact-original conditional cleanup and honest reconciliation
Apply SHALL bind the original Config, roots, actor, ordinary generation, ownership,
namespace and selected file identity/bytes, remove at most the unchanged selected
UUID.json, sync its directory and retain existing custody through output. It SHALL
report post-mutation uncertainty without retry/rollback. Status SHALL be read-only
and distinguish original, absent and changed state without claiming who deleted it.

#### Scenario: Apply exact intent or observe change and uncertainty
- **WHEN** an original intent is applied or reconciled after a changed file, deletion, sync failure or lost output
- **THEN** only an unchanged admitted original can be removed; changed inputs refuse, observed absence is not historical-success proof, and uncertain mutation/output never triggers automatic retry or deletion of a replacement.

### Requirement: Explicit platform capability
This producer SHALL support Linux only and SHALL return unsupported on non-Linux
before stdin, Config, filesystem or lock admission. Existing legacy cache APIs
SHALL remain unchanged. Windows fixture success SHALL NOT imply deletion or
directory durability; future browser and Electron adapters may use the same Linux
producer without requiring native local-host maintenance support.

#### Scenario: Unsupported host platform
- **WHEN** any new source-cache operation runs on Windows or another non-Linux target
- **THEN** it returns unsupported without reading held stdin or touching Config/roots/locks, and never reports applied using a no-op synchronization primitive.

### Requirement: Strict independent one-shot public contract
The additive version1 CLI SHALL require strict bounded whole-object stdin with
literal dash, fixed bounded nonsecret reports and early routing before runtime or
provider startup. Existing cache APIs and wire contracts SHALL remain unchanged.
Manager integration and installed/native/provider qualification SHALL remain explicit
separate work.

#### Scenario: Malformed input and public manual use
- **WHEN** malformed, oversized, nonliteral-selector or incompatible-mode input is supplied, or a contributor uses the documented public CLI
- **THEN** invalid input refuses before protected startup, and a valid local synthetic operation needs no private tools, provider or tablet access and claims no companion/runtime activation.
