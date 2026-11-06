# Design

Baseline Buddy0747f861 / Docs32647106. Reuse restore_maintenance strict parsing,
16KiB frame, protected configuration/source overlap checks, existing Store OS
lease and prepare/apply/status reports. Add explicit prepare-notebook,
apply-notebook and status-notebook selectors; they accept version2 intents only.
Legacy selectors accept version1 only. Neither route sniffs/falls back by format.

Reuse NotebookBackup complete format4 validation, actual same actor and existing
notebook feature/capability/contract validation. Require a ready ordinary local
notebook generation, no selected heads/retained history, no live domain/publisher
handles, writer or export. New existing-only notebook maintenance admission reuses
ExistingCustody and index rebuild, never creates a Store, publishes capabilities
or repairs an incomplete current notebook merely to admit a command. Its exclusive
OS lease and private Store handle keep local operations serialized; unlike the
legacy route it does not create an extra mode lease that would contradict the
notebook writer's unique-custody precondition. Persisted mode identity still binds
the returned intent and is rechecked with current generation/configuration.

Factor the existing notebook restore writer behind a private locked method with
caller-selected new target and an activation-attempt flag. The old public library
route preserves its semantics; the conditional route reserves an absent target
exclusively. Prepare validates current/source complete closures and the additive
union's exact manifests/records, returning stable fingerprints plus expected
feature flags through domain-separated history hashes. Apply repeats admission
and compares original conditions before any target writes. Actual staged rebuild
must validate complete notebook lineage before CURRENT publication. Preserve
staging on failure, distinguish not-activated from unknown after a CURRENT attempt,
and verify the desired generation/history/staged-config/capability readback.
Status only observes original desired state; it never repeats Apply or repairs
capabilities. A crash in the activation/capabilities gap remains unsupported or
unknown until separately owned recovery; observed desired state does not rewrite
an original unknown historical outcome. Configuration is staged, never installed.

Reuse bounded notebook detached validation for source admission; trusted local
parents/quiescent archive and cooperating OS-lease writers remain the baseline.
No hostile-root/path-race/strict power-loss guarantee is invented. Windows
sync_dir retains its documented limitation. Exact retained source bytes and all
unrelated current transactions/media survive. The source archive and original
configuration are never mutated. Native references remain historical/unbound.

Tests use real temporary Stores and production notebook/archive APIs, then the
actual maintenance path. Cover success/reopen/status, legacy isolation, wrong
actor/format/feature/config/source/media, stale original conditions, busy custody,
staging/activation/readback faults and lost-ack observation without replay.
Linux/Windows evidence is separate. No live provider/native result is required
for the local source increment. Root owns independent final review/integration.
