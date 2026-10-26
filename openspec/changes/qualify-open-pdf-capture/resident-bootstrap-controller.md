# Independent controller for the bootstrap observer

The observer runs a copied Reader as its own child. The prior research actor
instead shadows the stock unit and invokes recovery from an EXIT trap in that
actor's group. Reusing that execution engine would change the launch being
qualified and would not supply independent recovery after actor-group termination.
Reuse its frozen packet, source manifest, intent and evidence conventions only.

Use a separate, development-only PID1 actor and ordered recovery service. Freeze
their complete unit policies, payload hashes, fresh nonce and document manifest
before selection. Do not create an installed production profile from sampled
state. No service changes or tablet execution follow from this design alone.
Use a bounded Type=exec actor: its main process runs in active/running, which
the baseline captures. A Type=oneshot actor remains activating/start and cannot
use this admission contract without separately modeled behavior.

## Original service evidence

Extract a read-only `service::baseline::ServiceBaseline` around the existing
GroupBaseline implementation. Capture an explicit validated unit's running
MainPID between identical bounded PID1 snapshots, verifying actual process
incarnation, namespaces and membership. Preserve the original policy and
systemd invocation/start timestamp separately from process start ticks.

`current()` must recheck that original snapshot and actual group/process before
and after the observation. `stopped()` must bracket the original group lookup
with bounded PID1 samples and preserve the existing installed stock-stop rules:
unchanged retained identity, or completely cleared inactive identity with
qualified original-group deletion. Reject population, changed policy or partial
clearing. Return typed retained/cleared identity plus EmptyOriginal/OriginalAbsent;
never return restoration authority. A legitimate stop transition may return
pending under the original deadline. Parameterize the unit identity and reuse
this same predicate for installed stock activation.

Provide a bounded encoded observation record for the independently ordered
helper. Decode through the strict service-property parser, validate the group
record and original running-state relationship, and reject unknown/duplicate
fields, incomplete records and excessive input. The controller must separately
protect and bind the record's exact bytes; a decoded observation is not a lease.

## Execution sequence still to implement and qualify

Before stopping either existing service, verify fresh source preservation,
original service/process/artifact identities, the actual observer input guard,
and the independent loaded recovery path. Publish the actor and both original
service baselines durably before any stop intent. The PID1 actor must have an
absolute lifetime and control-group termination independent of SSH or its main
thread. Recovery must execute in a different service after actor termination.

Stop competing Buddy and stock at most once each with explicit pending intent
and non-replacing PID1 jobs. Prove both original groups terminal before starting
the fixed observer. Run it once, with no mutation, input injection or automatic
retry. Recovery must prove the original actor/child group terminal before stock
restoration, retain uncertainty, and verify the resulting stock process and
source preservation. Account explicitly for shutdown interruption and partial
admission before permitting legacy Buddy restoration. Preserve every record,
log and payload until independently verified collection and exact cleanup.

Validate the read-only baseline with retained/cleared transitions, policy and
identity changes, populated/replaced groups, malformed records, racing snapshots
and deadline expiry. Then exercise controller failure and recovery with isolated
fake units before any real handoff. Existing kernel observations do not prove
privileged migration exclusion or arbitrary firmware behavior. Independent
review of the exact controller and fresh candidate remains required.

## Read-only baseline implementation

Buddy `13ce5b26020c4e3ca8d58211400db0682178a3b5` implements the baseline and
delegates installed activation's stock-stop predicate to its shared typed
implementation. Existing outer installed-profile checks remain in place;
the common predicate additionally requires equality with the original sampled
policy. It issues no service commands and provides no synthetic installed lease.

Four new host regressions cover bounded strict record round-trip and malformed
relationships, refusal to treat fixture files as kernel cgroups, typed terminal
observations, policy/identity changes on either side, partial clearing, populated
groups, racing transitions and expiry. Existing installed stock-stop controls
exercise the same extracted predicate. These tests model service snapshots;
they do not qualify live PID1 ownership, migration exclusion or recovery.

Independent source review accepted the implementation and identified the actor
service-type constraint recorded above. Formatting and whitespace checks pass.
Exact-revision hosted compilation/tests remain pending; local Rust builds remain
unavailable with insufficient disk space. The executable controller, isolated
failure cases and native bootstrap selection are still unfinished.
