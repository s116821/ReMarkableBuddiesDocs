# Manager workflows

Manager groups controls around the task you want to complete. The browser and
desktop editions use the same navigation and show the capabilities available on
their host. Opening a page does not apply settings or run a tablet operation.

| Destination | What belongs here |
| --- | --- |
| Tablet | USB connection, observed tablet state, Buddy and Manager updates |
| Settings | Reader and Writer preferences, model connection and API key, research, personalization, memory settings, preference files |
| Data | Conversations, subject memory, handwriting corrections, storage and contextual cleanup |
| Backup & sync | Google account, saved data mode, export and restore |
| Troubleshooting | Diagnostic settings, saved configuration report and technical runtime details |

Choose a task before opening its editor. Supported actions keep their existing
read, preview and confirmation steps. A saved preference is not proof that a
running Buddy process has loaded it. An uncertain write remains uncertain until
its original status can be established; changing pages never retries it.

Google sign-in uses your own Google account and Drive. Account sign-in, tablet
configuration and a verified backup are separate states. Manager must not report
backup as enabled merely because browser consent succeeded. Normal application
onboarding should not ask users to register their own Google Cloud application;
application registration is a maintainer responsibility.

Some maintenance operations require a document, profile or record identifier
because the underlying supported operation cannot list it yet. Such tools must
explain the identifier they need, preserve original documents, and offer a
deliberate preview before deletion. Older archive formats belong to a selected
export or restore workflow, rather than separate top-level products.

## Contributor presentation rules

Add a capability to its existing task context. Do not append a new dashboard card
for each producer command, storage version or qualification increment. Keep
technical evidence in troubleshooting or selected-item details. Do not hide a
large unstructured dashboard behind one generic Advanced expander.

Preserve operation authority, input privacy, bounded cancellation and unresolved
results when changing presentation. Navigation must not make an unfinished
operation inaccessible or turn an empty recreated input into valid saved intent.
Retained status belongs beside the action it describes, with a discoverable cue
when attention is needed elsewhere.

See the [workflow contract](../openspec/specs/manager-workflows/spec.md),
[Manager architecture and checks](manager-foundation.md), and
[public roadmap](roadmap.md). Feature availability continues to follow the
individual implemented contracts; this guide does not qualify unfinished tablet,
provider or installation behavior.
