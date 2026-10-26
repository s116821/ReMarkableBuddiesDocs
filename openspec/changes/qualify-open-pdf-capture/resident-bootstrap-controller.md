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

The diagnostic controller is an explicit example behind a development-only Cargo
feature, not an installed dispatch mode. Its fixed nonce selects the staging
directory and owned unit names; a bounded candidate record selects native or
isolated fixture mode. Fixture mode may address only the two nonce-owned fake
units and an owned source directory. Native mode fixes stock/Buddy units and
the reviewed observer paths. Native fault injection is forbidden. Unit text is
rendered deterministically and loaded policy is checked, including independent
runtime/stop bounds and shutdown ordering. Existing service policy defaults are
not changed to make this diagnostic pass.

The candidate binds exact original service baselines, executable and controller
hashes, a fresh complete bounded source manifest and external backup identity.
After validation, write one complete ownership record before consuming either
stop intent. A missing ownership record with any stop intent is an error.
Successful publication is durable; records and per-invocation recovery intents
are exclusive and never overwritten. Recovery failures remain recorded and may
be independently inspected. A durable per-service start intent survives helper
interruption: a later invocation may verify an already-running service but must
never repeat that uncertain start. Exercise interruption after publishing the
intent and after submitting the start request in isolated fixture mode.

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
source preservation. Restore stock before running recovery source diagnostics;
their expiry or failure must withhold Buddy without preventing stock restoration.
Recheck input after authority sampling immediately before each stop, observer
launch and Buddy start. Account explicitly for shutdown interruption and partial
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
Exact-revision hosted Checks passed in run 40261613767; the application build is
still pending. Local Rust builds remain unavailable with insufficient disk space.

## Controller source implementation

Buddy `884a07c799885f10b77beb60a462ac07f0f5aec7` implements the development-only
controller and independent recovery example with fixed native/fixture targets,
durable ownership and stop/start intent, original-group checks, artifact pins,
bounded input admission and stock-first recovery. Its separate PR diagnostic
artifact includes the controller and observer checksums and actual build-source
SHA. Installed release packages do not select the feature or contain these tools.

Independent source review identified and verified fixes for uncertain start
replay across helper invocations, late input checks and source diagnostics
consuming stock restoration's deadline. Six host tests include recovery ordering
and refusal after diagnostic expiry or uncertain stock restoration. Formatting,
whitespace and the focused artifact-workflow fixture pass locally. These Rust
tests have not yet executed for this revision; hosted compilation, full checks
and ARM artifact generation remain pending.

Isolated PID1 cases must still exercise normal completion, actor SIGKILL with
a child, runtime expiry, partial stop, recovery exit, interruption after durable
start intent and after queued start, repeated-helper refusal, source mismatch
and shutdown. No fixture fault execution, native takeover, service change or
document mutation is claimed by this source implementation. Native candidate
selection remains dependent on those results and fresh independent review.
