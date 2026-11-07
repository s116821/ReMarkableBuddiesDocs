# Fixed service stop and independent lifecycle evidence

## Verified source and scope

Current reconciliation contract: package-record-contract.md binds delivered
Buddy91dcc601 PACKAGE/Profile6/Lease3, including its original rm-sync baseline,
fixed vendor artifacts, zero original/current companion watchdog and loaded
policy checks. The paired successor replaces Manager c013eb2's earlier
LEGACY/Profile1/Lease2 candidate. The following original source packet
is historical evidence, not qualification of either current candidate. Existing
results are retained under their original revisions. Both production registries
remain empty pending implementation and exact tuple qualification.

The original Manager1f258ce baseline had fixed service observation and no service mutation.
Main sourceb008027 and separately pending APK3f0a10a were verified through all18
payload hashes/bytes and17original Git blobs. source-assessment.md records precise
route/Drop/recovery limits; profile-admission.md defines the complete two-profile
predicate and private DTO. Committed source is not deployed qualification.
Existing Store/mode/configuration/native guards remain independent. The current
native candidate's narrower RM2 reports do not qualify released-source/RM1 safety.

## Systemd semantics

Primary systemd docs distinguish job completion, process exit and application
cleanup. Without ExecStop, systemd sends the configured termination signal; its
stop policy may later escalate. Killing the SSH client does not establish that a
queued remote job stopped or that native resources were restored. Do not assume a
universal TimeoutStopSec or target systemd version. Read effective properties and
admit only an explicitly supported loaded unit/lifecycle profile.

References: https://www.freedesktop.org/software/systemd/man/255/systemctl.html,
https://www.freedesktop.org/software/systemd/man/248/systemd.kill.html and
https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html.
These versions explain risks; they do not establish installed firmware behavior.

## Admission decision

The accepted intent is UNIT-SCOPED: request that fixed reader-buddy.service stop.
Revalidate current connection/boot and the original observed profile/invocation,
refusing observed drift. Do not claim atomic original-PID targeting, create a
bespoke lifecycle lock, or require a new compare-and-stop protocol. No stock or
native mutation authority follows from this intent.

Exactly ordinary-manual and resident-installed candidate profiles are recognized.
The closed predicates, observations, artifact/path/argv policies, mode-agnostic
scope, release enablement gates and explicit refusals are in profile-admission.md.
The manual Type=simple/Restart=on-failure unit and PACKAGE/notify resident
installation are distinct. The development alias, LEGACY resident contracts and
bare /usr/bin APK remain unsupported by Stop. Missing/occupied/partial native metadata cannot
become a readiness grant. There is no invented tablet flag/receipt or native lock.

No profile is enabled by this assessment. Owner qualification must bind the exact
source/build/unit/effective-policy/platform tuple and cover every runtime mode
that tuple admits, including active work. A source shape match is not that gate.
This does not block implementing the now-closed sampler, refusals, protocol,
transport/queue and UI fixtures after independent precode acceptance. The whole
paired change remains active until its actual qualification and delivery gates.

## Parent metadata collection

Use one bounded fixed command for each existing ordered parent chain instead of
opening a channel for every ancestor. The immediate no-symlink/stat pairs and
strict metadata parser remain unchanged. Validate the complete returned chain
before leaf metadata/content/hash access, and repeat it independently after the
protected read. Do not cache parent metadata or replace the second sample.

This deliberately changes the rejected-operation trace: an unsafe ancestor's
owner/type/mode may be rejected after deeper ancestor metadata was collected.
Those reads reveal metadata only; no leaf content or hash is allowed before all
parents pass. A symlink or failed stat still aborts the shell chain immediately.
Retain exact record count/order/framing, the 4096-byte stdout cap, stderr/EOF
checks and the same absolute deadline. Fewer synthetic commands are source-cost
evidence, not a measured target runtime or production profile qualification.

## Host and UI

Use a distinct serviceStop capability and existing MaintenanceIO across both real
factories. Derive peers from the admitted final source (storage initialization
adds a nineteenth predecessor). Review and Confirm acquire ownership before
invalidation/I/O; Busy has no cancellation or invalidation side effects. Ordinary
observation polling quiesces before review/confirmation. Ready expires after120s
and is invalidated by peer/session/invocation/unit drift. Confirm revalidates the
original private review and never silently upgrades admission. The operation remains unit-scoped and never promises original-PID CAS.

After possible stop submission, lost/nonzero/incomplete/timeout/cancelled output
is unknown. Even a later inactive observation cannot settle original delivery,
prove a graceful stop or grant another stop. At most8possible submissions and32
invocation/fence entries per original, no eviction or renewal. Unknown blocks
another stop for that connection across reboot within host lifetime. History is
in-memory only. Cancel targets the original host reference+invocation; it stops
local waiting, never sends systemctl cancel/start/recovery or a delayed global
kill. A stale cancellation/finally cannot affect a newer host owner.

Use the existing fixed-command pattern: /bin/systemctl --system --no-pager
--no-ask-password --no-block --job-mode=fail stop -- reader-buddy.service. This
is a candidate command supported by current native source usage for another
fixed unit, not target-version qualification. Success means request accepted by
PID1, not completed shutdown. A conflicting pending job refuses rather than being
replaced. No cancellation/restart/recovery command is sent.

Current service observation and historical command outcome are separate. Report
at most current OS state and whether the original fixed stop request was accepted
under the admitted contract. Neither field means native restoration/flush success.
No automatic config save/restart/restore continuation follows. Existing maintenance
must independently observe current inactive state and acquire its own guards.

## Useful work and real qualification

After current source/policy acceptance, independent work can implement strict
protocol/action matrix, fixed transport, shared ownership/lifetime/controller,
closed UI reduction and local process/SSH/systemctl-fixture cases without a tablet
or provider. These can exercise unavailable profiles, queued/lost requests,
changed invocation, unsafe unit policy and late output. Final actual host/browser/
Electron/package/platform checks remain required. Native stop safety and unit
package compatibility are owner-supplied dependencies, not waived by those tests.

## Typed hook integration
Reuse the reviewed pure decoder and the existing injected bounded runner. Keep
textual parsing strict for the other41 properties; use the separate typed hooks
DTO defined in contract.md for the two command-array properties. One group spans
the existing repeated captures and is reset on failure. No new executable,
transport framework, public protocol or production tuple is introduced.

## Common stat producer
An actual read-only target diagnostic returned BusyBox1.36.1's rejection of
`--printf`. Use `-c` with literal internal newlines and its automatic terminal
newline; both upstream GNU and BusyBox support this format without changing the
metadata schema. BusyBox1.36.1 source retains nanoseconds in `%y`/`%z` and reports
missing files with `can't stat`, distinct from the existing GNU `cannot statx`
spelling. Admit only those exact missing-final-component envelopes, not a loose
substring or locale translation. Keep every timestamp and parent check strict.
The previous refused attempt remains failed; this correction needs new target
evidence and does not retrospectively repair it.
