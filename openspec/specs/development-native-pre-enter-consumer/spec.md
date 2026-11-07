# Development pre-Enter consumer

## Purpose

Describe the opt-in Buddy consumer for the SDK historical pre-Enter diagnostic.
This capability provides source/build integration only; native input, composer
authority and device recovery remain separately qualified.

## Requirements

### Requirement: Build-only closed historical consumer

Buddy SHALL expose the typed pre-Enter request and connection method only under
explicit compile-time buddy_development_native_pre_enter, without runtime
selection. Cfg registration alone SHALL NOT enable it. Ordinary Cargo all-features
CI SHALL retain its normal/dev SDK pins and lock without referencing unavailable
SDK variants. Source: Buddy bafa5cc9 Cargo/build/CI and SDK240df867 paired wire.

#### Scenario: Ordinary all-features build
- **WHEN** ordinary CI builds all Cargo features against its existing SDK pin without custom cfg
- **THEN** the new arm/method SHALL be absent and ordinary feature coverage SHALL remain unchanged

#### Scenario: Selected developer build
- **WHEN** custom cfg and exact reviewed SDK override/features are explicitly selected
- **THEN** only the closed historical consumer SHALL become available, without enabling another mutation selection, runtime setting or product CLI option

### Requirement: Official diagnostic build exclusion

A diagnostic build SHALL refuse if ANY existing release/candidate tag or SHA
input is present, including empty, partial, malformed or mixed values, or actual
HEAD has an exact official semantic tag under existing policy. This SHALL hold
for externally supplied cfg and for tagged HEAD without identity environment.
Required developer Git identity SHALL fail closed when unavailable. Build-script
cache tracking SHALL cover selection and identity inputs. No diagnostic artifact
SHALL acquire official identity or enter release/APK archives. Ordinary metadata
behavior without cfg SHALL remain unchanged. Source: Buddy build.rs identity
channels and this design's official-build rejection.

#### Scenario: Supplied cfg with official identity channel
- **WHEN** any candidate/release identity channel is present with diagnostic cfg, even empty or unpaired
- **THEN** the build SHALL fail with a fixed value-free error before producing a diagnostic Buddy artifact

#### Scenario: Exact tag without identity environment
- **WHEN** actual HEAD is exactly officially semantically tagged and diagnostic cfg is supplied without official identity variables
- **THEN** the build SHALL refuse instead of treating it as a permitted tagged development or official build

### Requirement: Isolated developer source and lock

The diagnostic SHALL use Cargo's command-local Git-source path patch to the clean
exact reviewed SDK, explicit features, separately resolved/frozen developer lock
and isolated target/output. Later metadata/check/build SHALL repeat the same
patch/features with --locked. Actual resolved metadata SHALL bind the single SDK
manifest/tree, feature graph, locks, toolchain/flags/argv and native variant.
Dirty, replaced, unused, duplicate, wrong or changed inputs SHALL refuse. No
home/shared Cargo config, ordinary lock/pin, maintained version or tag SHALL
change. Existing source/APK validation SHALL keep refusing incompatible path or
compiler inputs; no release-proof exception SHALL be added. Source: central
package-build-inputs, Buddy cargo_identity/cargo_configuration and Cargo patch.

#### Scenario: Reviewed developer override
- **WHEN** the exact clean SDK path, generated developer lock and feature graph are frozen
- **THEN** subsequent commands SHALL use unchanged recorded inputs under --locked with separate unqualified development provenance

#### Scenario: Changed override or source
- **WHEN** patch/source/features/lock differ, another SDK is reachable or SDK is dirty/replaced
- **THEN** admission SHALL refuse without implicit lock update, alternate pin or ordinary-release bypass

#### Scenario: Return to ordinary build
- **WHEN** an ordinary build omits diagnostic cfg/patch and uses its independently retained original lock
- **THEN** normal identity/checks SHALL remain authoritative; removing a patch alone SHALL NOT be claimed to revert a changed developer lock

### Requirement: Existing request owner and original deadline

The consumer SHALL use the existing closed request_read_only and SDK
execute_with_progress with the ORIGINAL absolute deadline, existing progress,
pre/post admission, companion/child/owner checks, after_api retention and failure
mapping. It SHALL NOT add an arbitrary command/effect closure, new transport or
registry, mutation journal, fresh relative budget, automatic reconnect/retry or
rearm. Endpoint/RequestLease SHALL remain SDK-owned. Source: Buddy read_only.rs
and resident_client.rs, SDK transport.

#### Scenario: Correlated completion
- **WHEN** the request returns within its original deadline and final admission/retention succeeds
- **THEN** the consumer MAY return only its correlated historical diagnostic result

#### Scenario: Lost deadline or ownership
- **WHEN** expiry, progress, admission, connection or retention fails before successful completion
- **THEN** original failure/uncertainty SHALL remain without extended deadline, false success, lost earlier effect evidence or replay/rearm

### Requirement: Exact bounded raw UTF-16

The range SHALL retain count <=4096 and checked offset+count <INT32_MAX. SDK
operation/sequence/full-digest/reply-type/unit-count correlation SHALL remain.
Original u16 units SHALL be preserved without lossy decoding, normalization,
NUL stripping or surrogate replacement. Copied empty, refused, Unsupported and
Capacity SHALL stay distinct; other/protocol/transport failures SHALL NOT become
empty text. Any bounded fixture text/hex evidence SHALL remain private, outside
generic/public logs. Source: SDK Command/Reply and Session::complete.

#### Scenario: Raw or empty copy
- **WHEN** an admitted copy has exactly the requested count, including zero or NUL/separator/isolated-surrogate units
- **THEN** those exact units SHALL be retained and successful empty SHALL differ from refusal

#### Scenario: Refusal or mismatch
- **WHEN** SDK refuses/Unsupported/Capacity or rejects wrong type/count/identity
- **THEN** the distinction or failure SHALL survive without substituted text, downgrade or replay

### Requirement: Native arming and designated input remain separately admitted

The consumer SHALL NOT manufacture arming from Ready or request send. An eventual
observer SHALL require Native's real bounded marker with original pending
request/runtime/deadline/clock-domain checks before input. The designated single
Enter SHALL be distinguished from an unrelated Reader-currentness lease without
relaxing health/owner/deadline/recovery checks. Physical folio input SHALL remain
human-dependent unless a separately authorized, actually available mechanism is
verified; synthesized/OSK input SHALL NOT silently substitute. Source: SDKc85c4669
variant/marker contract, retained by its existing owner.

#### Scenario: Invalid arming evidence
- **WHEN** the marker is missing, partial, stale, late, mismatched or unverifiable in its original clock domain
- **THEN** no input step SHALL occur and the original outcome SHALL remain without retry/rearm

#### Scenario: Designated future Enter
- **WHEN** a separately selected fixture admits one Enter with all applicable boundaries retained
- **THEN** only that designated event MAY be observed without granting unrelated edits or inventing physical input capability

### Requirement: Historical limits and coordinated delivery

The copied result SHALL NOT establish semantic Submit, current draft/edit
revision, focus/conditional-clear lease or durable save. Source/offline checks
SHALL stay distinct from native copy/edit and independent restoration evidence.
Central Docs and affected Buddy implementation SHALL be verified, canonically
synced and archived as one delivery only when selected obligations are complete.
Precode/build success SHALL NOT authorize tablet/provider activity. Source:
central development-testing, platform-runtime and OpenSpec delivery workflow.

#### Scenario: Local verification only
- **WHEN** source/build controls pass without native qualification
- **THEN** only that exact evidence SHALL be claimed, with input/native/recovery gates explicit and no product composer authority
