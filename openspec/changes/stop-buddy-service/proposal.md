# Deliberate fixed Buddy service stop

## Why

Both companions inspect the fixed Buddy service, while saved-setting and owned-data
maintenance requires users to manage service state separately. A deliberate stop
can make that workflow clearer. OS inactivity alone cannot establish native stock
Reader restoration, safe resource release, original-operation settlement or data
flush. Those lifecycle boundaries must be verified before enabling mutation.

## What changes

Add a separate shared Review stopping Buddy / Stop Buddy / Check service state
flow over verified wired SSH and the existing fixed reader-buddy.service. The
host validates a supported loaded unit/runtime lifecycle profile, samples its
current invocation for drift checks and presents unit-scoped consequences before one explicit stop. Only
recognized, independently accepted stop semantics may permit mutation. Unknown,
changed, unsupported or unqualified native ownership refuses before dispatch.
A later OS read is current state only; Stop waiting never rolls back or cancels a
systemd job already requested. Retain uncertainty without automatic replay.

## Capabilities

New capability: manager-service-stop. That Stop capability leaves existing storage
setup, saved-file, Local-only, release source, package installer and selected-outbox
wires unchanged. The separately bounded package-transition addition below has its
own capability and explicit operation intent; it does not expand serviceStop.

## Exclusions

No start/restart/reload/enable/disable, installation/purge, arbitrary unit/PID/path,
force-kill command, recovery command, provider operation, native page mutation,
Buddy admin API, WLAN tablet transport, automatic maintenance chain or invented
shutdown receipt. The service's own stop/escalation policy must be admitted, not
silently overridden. No claim that a completed stop alone proves graceful native
restoration or permits another operation without its independent checks.

## Assessment and enablement

Delivered Buddy91dcc601 and retained package evidence distinguish the /opt manual
unit from PACKAGE/Profile6/Lease3 with the original rm-sync baseline. The earlier
LEGACY/Profile1/Lease2 consumer proposal and bare /usr/bin APK are not qualified
Stop profiles. package-record-contract.md defines the proposed closed records,
fixed paths, companion/vendor observations and digest delta implemented in the
paired successor after Manager c013eb2. Both companion watchdog observations
must be zero. profile-admission.md retains unavailable config/runtime
facts and separate enablement gates. Unit-scoped user intent is accepted; no atomic
original-PID stop or new lifecycle lock is proposed. Both profiles remain disabled
until owner-qualified binary/unit/policy/platform and active/native stop evidence
cover their admitted runtime modes. No new readiness file or flag supplies that
qualification.

The accepted precode is imported into this sole central change before code.
Protocol, refusal, transport, queue and UI fixture implementation can proceed
without tablet or provider execution. Keep the whole change active until
actual enablement/qualification and paired delivery; no planning-only merge/archive.

## Proposed shared resident-package wiring addition

Status: precode for independent review before implementation. Manager PR57 has
existing host-private package transition/recovery/disable/removal/replacement
helpers, but no public shared-host/renderer route. Add only the closed
`manager-resident-package-transition` capability described in
`package-transition-wiring.md`, backed by those helpers and the existing common
MaintenanceIO/verified wired transport. This is an amendment to the same active
change and coordinated Manager delivery, not a new installer or planning-only PR.

The serviceStop exclusions above continue to govern that capability. The new
capability alone can request a reviewed fixed disable/remove/replace transition;
it does not expose start, arbitrary commands/paths, package creation, trust repair,
new downloads or a generic workflow engine. All production Stop and package
qualification gates remain empty; no operation becomes eligible from source tests
or the separately completed public test-fixture observation.
