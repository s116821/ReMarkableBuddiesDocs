# Protected notebook restore contract

This increment adds three explicit values to the existing `--restore-operation`
selector: `prepare-notebook`, `apply-notebook`, and `status-notebook`. Input uses
the existing `--restore-input -` protected stdin transport and configured owned
paths. The existing strict 16KiB JSON request/report bound applies. Both request
and report version are 2; legacy operations and their version1 behavior remain
separate. Do not infer an operation from archive format or change a returned
intent's version to route it elsewhere.

Prepare accepts `restore_version: 2`, a new nonnil `operation` UUID and `source`
archive path. It returns the existing preview/intent shape, including original
actor, mode/config/path fingerprints, archive metadata fingerprint, base and
target generation/history fingerprints, staged configuration fingerprint and
complete-media condition. Notebook history fingerprints additionally bind the
actor and effective feedback/selection feature flags. The archive must be a
complete ordinary format4 notebook archive from the same actor. Current state
must be a ready local notebook generation with no selected heads/retained history.

Apply and Status accept `source` and the complete original returned `intent`.
Keep this private intent unchanged. Apply rechecks original conditions, reserves
the original absent target, stages all current and source facts through the
existing notebook writer, rebuilds complete lineage, publishes CURRENT and
capabilities, then verifies desired history and staged configuration. Optional
archive configuration remains staged as `restored-config.json`; it is not applied.
Records keep their original identifiers and causal revisions. Device/page
references convey historical data, never new native or selection authority.

The existing report shape uses `report_version: 2` and
`runtime_activation: unverified`. Success requires `outcome: restored` after
actual desired-state readback. Prepublication writer failure can report
`not-activated` with retained staging. A failed CURRENT attempt or uncertain
completion/readback reports `unknown`. Preserve that original outcome even if a
later Status observes the desired generation. Status can report
`desired-generation-observed` or `unresolved`; it neither replays Apply nor
repairs capabilities, and does not require the source archive to remain present.
Missing/corrupt current readiness can instead refuse observation. Repeat Apply
never silently chooses another target or reuses existing staging.

The private Store instance holds its existing exclusive OS lease through report
write and flush. It does not acquire an additional ordinary mode handle, which
would violate notebook unique custody; persisted local mode identity is still
bound and checked. This is the existing cooperating-writer, trusted-local-parent,
quiescent-archive model. Source inspection reuses the bounded detached notebook
validator; subsequent union/staging retains existing notebook writer behavior.
No single cumulative I/O budget for the entire maintenance invocation or strict
Windows power-loss/directory-sync guarantee is introduced.

Cross-actor mapping, shared/selected activation, clean-device setup, Manager UI,
Drive synchronization, provider execution and native mutation remain outside this
delivery. The legacy ordinary restore contract continues to refuse notebook
layouts unless the explicit notebook route is selected.
