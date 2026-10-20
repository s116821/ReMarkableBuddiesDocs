# Event admission and result identity

Preserve one core workflow, its existing normal PR/main stage budget and all
normal job/check names. The maintained title Action still runs first for every
PR event. Opened/synchronize/reopened events and edited events with a real title
change run the normal code pipeline after valid title; this preserves recovery
when an initially invalid title prevented downstream checks.

For edited without changes.title, the Checks predicate additionally refuses
application execution. Its omitted job receives an explicit metadata-only name,
not `Checks`. The skipped reusable application caller likewise receives an
explicit metadata-only name rather than its normal caller name. A false caller
must not instantiate its normal Build/Integration child checks. No successful
placeholder or new skipped normal application context may mask an existing
failed/canceled check. Normal/source/title-edit names and guards stay exact.
Do not change source-run concurrency or cancel useful runs as admission logic.

This design uses workflow expressions and existing Actions, not an API rerun
coordinator, additional normal PR jobs, write-token escalation or branch-setting
changes. Dynamic names apply only to omitted metadata jobs and must be reviewed
as an explicit context change. If actual GitHub behavior still creates normal
application contexts, reject the candidate and revise before delivery.

# Evidence and controls

Buddy69faff5 runs39372692100/39372727494 share the exact source; the latter
followed a body edit. Existing workflow source includes pull_request.edited.
The canceled duplicate's native job API shows title succeeded, Checks canceled
and only the reusable caller skipped; its child Build/Integration jobs were not
instantiated. This corroborates caller isolation but is not final candidate proof.
The pinned title Action48f25628 fetches the current PR through REST, explicitly
avoiding stale event titles on reruns. No custom semantic parser is introduced.

Focused controls evaluate the real YAML expressions for source, body-only edits,
title corrections, prior code failures, cancellation and main. Verify unchanged
normal names/job budgets and dependency gates. On the owned draft candidate,
retain a witnessed failed application check, change body only, and inspect native
check-run IDs/names/conclusions to prove the failure remains authoritative. Also
prove invalid title then correction on unchanged source starts real Checks after
title passes. Preserve expected failures; do not relabel reruns or waive gates.

The hosted negative may use one explicitly temporary failing shell step at the
start of this owned candidate's Checks job, before costly suites. An invalid
title must first block it; correcting only the title must run it and produce a
real failed Checks result. A subsequent body-only edit must leave that exact
failed check ID/conclusion intact. Remove only this owned control step in a new
source commit, then require the ordinary final source pipeline to pass. Preserve
the intermediate commits and actual failures, and prove the final diff contains
no control step or application-source edits. Do not manufacture check results,
edit a feature candidate or replay completed broad suites for this experiment.

Existing Buddy layout/catalog deliveries continue independently. No source,
provider, native, signing or artifact-generation test is repeated for this plan.
