# Source-cache metadata inventory

## Purpose

Discover bounded owned cache candidate IDs and apparent lengths without reading payloads, granting cleanup authority or implying source/runtime freshness.

## Requirements

### Requirement: Bounded nonmutating source-cache metadata inventory
The Linux inventory CLI SHALL use private existing-only header/Store-and-namespace
lease custody to list at most16 canonical slot IDs and apparent lengths, without
initializing/recovering Store, reading entry/durable payloads, cleaning staging,
accessing credentials/original documents or mutating storage. Unknown/unsafe or
changed input SHALL refuse without a partial success list and custody SHALL last
through consuming output/failure.

#### Scenario: Stable bounded namespace or unsafe/concurrent observation
- **WHEN** the fixed existing namespace is empty/populated within bounds, or ownership/lease/path/bounds/identity changes prevent admission
- **THEN** metadata returns a deterministic bounded list and total only when consistent, or an explicit nonmutating unavailable/unsupported/busy/conflict report.

### Requirement: Honest metadata-only authority
The versioned report SHALL explicitly distinguish unread/unvalidated payloads and
unverified source freshness from current metadata and SHALL confer no cleanup,
reclaimability, source-history, native or runtime authority. Selective cleanup
SHALL still require its separate fresh selected-slot preparation and confirmation.

#### Scenario: Corrupt entry or later selected cleanup
- **WHEN** a canonically named slot has empty/corrupt content or a user later selects an inventory candidate
- **THEN** inventory may describe only its metadata, and a later cleanup independently validates/reprepares the selected slot without adopting inventory as permission or freshness proof.

### Requirement: Separate public parameterless wire and platform boundary
The additive parameterless CLI SHALL expose a closed bounded report without
stdin/arbitrary path/filter input or protected startup, return early unsupported
on non-Linux and preserve all existing closed reports/operations. Both future
companion host adapters SHALL be able to invoke the same Linux producer without
claiming implemented Manager or local Windows support.

#### Scenario: Unsupported platform or incompatible invocation
- **WHEN** inventory is invoked on non-Linux or with conflicting execution/override flags
- **THEN** it refuses before Config/filesystem/runtime admission without consuming input, changing another wire or starting an alternative operation.
