# Ordinary public Stop with a durable typed job receipt

This precode applies to the isolated ordinary public qualification successor
only. Source bases are Manager 061ac32847b52d4310490cfd09f858804ed0ab05 and
Docs fb85d3c86124668753c297be810a2dcab4585f71. The reviewed diagnostic owner
and job receipt scripts come from seal 2e0a5d32. Existing ordinary and resident
production registries stay empty. The old systemctl sender and completed
diagnostic cannot supply this successor's qualification.

## Fixed submission and custody

In the isolated build, only the approved ordinary alias tuple and fixed
nonce-scoped owner stage may use this adapter. Resolve those from compiled
reviewed inputs. No renderer-supplied path, unit, method, profile tuple,
action token or command. Keep public Begin, Confirm, Inspect and their
result DTOs unchanged. Preserve the exact private sampling digest and
two-bracket recheck. The host's Confirm carries its already admitted
invocation UUID into the private child alongside the existing expected
profile/sample hash. Only Stop may carry that additional field. The
original review reference and its invocation ledger remain in the host.
No private field is copied into the public result.

Reuse the protected wired observer and fixed authenticated transport.
Bracket the same boot and the same admitted bus ID, unique manager owner
and Unix PID 1. The private child verifies the original sample and records
possible submission before writing the one fixed exec command. The exec
runs the hash-pinned existing device owner under its existing per-stage
lock and nonce. Its fixed action public-stop is the only Stop authority
for this experiment. The trial orchestration installs/starts and waits
for that action rather than sending its own diagnostic Stop. The existing
independent rollback timer is armed before installation and remains the
recovery owner. No host fallback or passive second Stop engine.

The device owner checks the active stage/lock, open guard, prepared alias
and executable custody, original expected boot/manager and exact trial
invocation/group. Reject an existing public binding, claim or job directory.
Use the original record_job and ListJobs parser with the additional
public-stop action. The one manager method is EnqueueUnitJob with
sss reader-buddy.service stop fail. Require exact response type, job
identity, unit, job type and accepted auxiliary policy from the existing
parser. No retry after the durable claim, regardless of outcome.

## Deadline

Keep the original UI/host/child ceilings of 14/13/12 seconds and the original
absolute host deadline. Sample same-boot device uptime before dispatch in
the bounded child. At sample receipt, calculate a conservative device
uptime cutoff using the sampled uptime plus the remaining host time minus
a reviewed 100 ms margin, rounding down. Use a bounded canonical uptime
parser. No send if the remaining allowance cannot accommodate the minimum
margin or if time is stale/unavailable. The owner independently checks
that exact cutoff against device uptime immediately before the typed
method, alongside its existing timer/rollback reserve. A late host result
cannot extend the cutoff or upgrade an original outcome. A receipt for an
already-sent action may finish durable publication after the cutoff solely
for independent recovery. It cannot yield public acceptance after expiry.
Preserve the original outer and remote recovery limits.

## Durable receipt and acknowledgment

Under the stage lock, write the canonical ASCII single-line binding
PublicStop1, nonce, public invocation UUID, sample SHA-256, connection
SHA-256, boot UUID and decimal device cutoff, separated by single spaces
and ending with LF. Limit to 384 bytes. Use protected root-owned stage
mode 0700 and a root-owned regular single-link file mode 0600. Validate
each field strictly and compare against the original admitted values.
Use exclusive creation of a private temporary file, flush it, atomically
rename to fixed stage/public-stop-binding only when absent, then flush
the parent. Persist the existing public-stop-claim marker before the
method call. A partial pre-send claim is never fresh authorization.

Use stage/public-stop-job/reply capped at 8192 and identity capped at 512.
Reuse the existing root-owned protection and parser. Extend the public
job identity with the SHA-256 of the exact durable binding line. Bind the
existing nonce, action, boot, manager bus and unique owner, trial invocation,
returned exact job ID and exact LF reply SHA-256 as before. Flush reply,
identity and directory, then use the original atomic public-stop-job-accepted
marker as the commit point. Verify the same manager and matching protected
receipt after publication before output. Acknowledge to the host only with
the exact bounded committed identity line. No new persistent database.

The host compares the echoed binding hash, exact observed boot/manager,
stage nonce, trial invocation and returned job identity/receipt framing
against the admitted request. Only a complete zero-status and zero-stderr
reply inside the original deadline and the original host owner may reduce
to request-accepted. Missing, mismatched, partial or late output, receipt
persistence uncertainty, cancellation or lost acknowledgment stays unknown
after possible submission. No automatic upgrade or duplicate call. The
public raw/result shape remains unchanged. Keep the exact receipt as
private qualification/recovery evidence.

## Recovery and controls

Extend the existing require_settlement list, bound invocation selection
and retirement check to public-stop. Revalidate the immutable binding
and accepted receipt in settle_job, require same manager and boot, exact
job absence in complete ListJobs and actual trial invocation/cgroup
retirement before restoring the original name. Queue absence supplies no
JobRemoved result. Unbound or uncertain effects preserve escrow and
withhold owner release. Existing independent restoration and opacity
checks remain required.

Exercise an exact commit-before-ack positive path, wrong owner/boot/
invocation/sample/nonce or elapsed cutoff before method, occupied claim/
binding/job directory, unexpected manager reply, auxiliary jobs, flush or
rename failure at every durable boundary, disconnect or expiry before and
after the method, late/duplicate acknowledgments, and original unknown
retained while recovery sees a committed exact receipt. Missing receipt
must withhold restoration even if the queue is empty. Same-manager job
presence and process/cgroup presence must each independently withhold
settlement. Preserve legacy direct/resident raw/digest vectors, zero
production dispatch in both factories, and fixed-command/no-caller-path
tests. No actual installation or Stop is selected by this amendment.
