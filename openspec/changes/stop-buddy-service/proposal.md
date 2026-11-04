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

New capability: manager-service-stop. No change to the existing storage setup,
saved-file, Local-only, release source, package installer or selected-outbox wires.

## Exclusions

No start/restart/reload/enable/disable, installation/purge, arbitrary unit/PID/path,
force-kill command, recovery command, provider operation, native page mutation,
Buddy admin API, WLAN tablet transport, automatic maintenance chain or invented
shutdown receipt. The service's own stop/escalation policy must be admitted, not
silently overridden. No claim that a completed stop alone proves graceful native
restoration or permits another operation without its independent checks.

## Assessment and enablement

Verified current main ordinary/resident and separately pending APK source establish
the /opt manual, canonical resident and /usr package distinctions. The exact
closed two-profile admission table, property DTO and unavailable config/runtime
facts are in profile-admission.md. Unit-scoped user intent is accepted; no atomic
original-PID stop or new lifecycle lock is proposed. Both profiles remain disabled
until owner-qualified binary/unit/policy/platform and active/native stop evidence
cover their admitted runtime modes. No new readiness file or flag supplies that
qualification.

The accepted precode is imported into this sole central change before code.
Protocol, refusal, transport, queue and UI fixture implementation can proceed
without tablet or provider execution. Keep the whole change active until
actual enablement/qualification and paired delivery; no planning-only merge/archive.
