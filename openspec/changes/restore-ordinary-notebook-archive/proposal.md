# Protected ordinary notebook restore

## Why
The delivered same-actor format-4 NotebookBackup has export/inspection commands
and an existing library restore writer, but ordinary protected restore refuses
notebook generations. Expose a bounded explicit prepare/apply/status maintenance
path so users can restore their own archive without native or cloud authority.

## What changes
Add explicit notebook operations to the existing restore command family, using
version-2 intents and the existing report/ownership/config/path guards. Reuse the
existing notebook archive validator and generation/CURRENT writer. Conditional
publication binds actor, mode/config/source, base and intended target history.
Legacy selectors/version-1 intents retain existing refusal/behavior.

Same-actor additive local restore only. No new restore framework, cross-actor
mapping, shared/selected activation, Drive, Manager UI, native document/page
mutation, provider call or automatic uncertain replay is included.
