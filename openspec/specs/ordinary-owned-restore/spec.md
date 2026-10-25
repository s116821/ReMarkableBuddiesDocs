# Ordinary owned-archive restore producer

## Purpose
Restore a compatible ordinary archive additively into an existing ordinary unconfigured/local-only Store through the existing guarded generation writer. Original history/source conditions, exact desired readback and phase-specific uncertainty remain distinct from runtime activation or historical publisher identity. The detailed [contract](../../changes/archive/2026-10-20-restore-ordinary-owned-archive/contract.md) fixes shapes, limits and fingerprint recipes. Selected restore, clean/replacement-device setup and companion UI remain separately unfinished.

## Requirements

### Requirement: Deliberate bounded ordinary restore preparation
The producer SHALL prepare only an additive format1 restore into an existing ordinary unconfigured/local-only owned Store, under contract.md bounds and pure strict admission. Preparation SHALL preserve source/target files and bind the original config/path, actor/mode, complete target generation/history and source archive identity to a fixed new desired generation/closure. Selected/shared/isolated/clean-device/provider/native authority SHALL remain refused or outside this increment.

#### Scenario: Compatible archive and existing target
- **WHEN** one explicit bounded valid ordinary archive and existing ordinary local target are prepared
- **THEN** a truthful additive impact and private original conditional intent are returned without mutation or configuration/credential activation.

#### Scenario: Unsupported or corrupt admission
- **WHEN** selected/shared/isolated/Busy/uninitialized/corrupt/future state, unsafe paths, missing promised media or bounds fail
- **THEN** the bounded invocation refuses without initialization, repair, service stop, fallback or invented restore readiness.

### Requirement: One guarded existing restore publication
Apply SHALL extend the SAME additive staging/rebuild/atomic CURRENT writer. Original actor/mode/config/source and generation/history conditions SHALL be compared under its publication mutex, retained through exact desired readback and consuming output. Existing caller behavior, old generation/source and all preexisting target history SHALL remain preserved; configuration/credentials/native files SHALL NOT be activated or replaced.

#### Scenario: Original state changes before publication
- **WHEN** a same-generation commit, generation replacement, changed source metadata/content, changed binding or existing target directory contradicts original intent
- **THEN** the command refuses or reports not-activated/unknown according to the actual CURRENT publication phase, without silently refreshing conditions, reusing staging or replacing unrelated data.

#### Scenario: Exact activation or uncertain writer outcome
- **WHEN** complete desired readback succeeds or an error occurs before/after the actual CURRENT publication attempt
- **THEN** the result is respectively verified disk restore/runtime-unverified, not-activated with possible retained staging, or unknown, retaining original evidence/old data without automatic retry, rollback, cleanup or replacement output.

### Requirement: Consistent read-only desired-generation observation
Status SHALL observe original binding and full intended active generation/manifest/object/configuration closure under consistent existing-store custody. It SHALL report only desired-generation-observed or unresolved, without mutation, source archive reread, historical publisher proof, runtime readiness or settlement from a later refused invocation.

#### Scenario: Original apply response is missing
- **WHEN** a possibly dispatched original intent is explicitly checked
- **THEN** exact desired active state can be observed without replaying apply, while UUID equality alone, nonmatching data or a later refusal cannot acknowledge historical publication or infer rollback.

#### Scenario: Report prefix fails
- **WHEN** complete output or a prefix write fails
- **THEN** Store/current-mode custody lasts through the consuming write/failure, then releases without a second report or automatic restore.
