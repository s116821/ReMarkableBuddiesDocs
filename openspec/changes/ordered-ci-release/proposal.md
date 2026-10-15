## Why

REM-56 records the October 15 human instruction in Things to Fix version111:
checks must gate builds, builds must gate integration tests using their artifacts,
and one final release job may tag/publish only after every predecessor succeeds.
Current main release workflows independently race CI. The unfinished REM-46
candidate instead tags and creates a draft before building, which is now obsolete.

## What Changes

- Compose maintained upstream filtering, semantic versioning, tagging and release
  publication in one ordered Buddy workflow and one independent Manager workflow.
- Freeze a read-only candidate version/source before builds, test the actual
  resulting artifacts, and publish those exact bytes only in the final main job.
- Retire the bespoke production filtering/version/coordinator engines, preserve
  their historical evidence, and keep build/package/identity verification helpers.
- Order ordinary Docs checks without introducing a Docs release. SDK release
  requirements remain SDK-owned and are coordinated separately with SCRAPPY.

## Scope

Buddy and Manager release workflows, upstream tool configuration/provenance,
necessary build identity/packaging and artifact-consumer tests; central release
and Manager requirements. No tablet/account operation, production release/tag,
repository-setting change, SDK source edit or whole REM-35/46/50 completion.
