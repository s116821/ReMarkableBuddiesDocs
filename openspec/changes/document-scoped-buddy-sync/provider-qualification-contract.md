# Proposed disposable provider qualification contract

Status: reviewable execution contract only. No account, OAuth registration, file,
namespace, device or service has been created or changed. This is part of the
unfinished REM-52 delivery, not live-provider acceptance.

## Resource decisions required before execution

The coordinator must identify an explicitly authorized suitable Google account
and OAuth application, protected local credentials, named operator and exact
permitted client registrations. Prefer an existing explicitly authorized binding
when isolated disposable app-data resources, exact registration/visibility and
cleanup satisfy this contract. A new account or project is not mandatory; resource
creation, if needed, requires its own explicit execution scope. Use only
drive.appdata for this candidate. An existing Drive connector or its
Personal/ChatGPT folder does not establish access to this application's hidden
data or permission to exercise contention there. Do not infer authorization from
personal-cloud backup, tablet SSH setup or source fixture results.

Choose one test run UUID and group UUID, agree fixed pre-generated appDataFolder
IDs before either contender starts, and record every generated/created resource
ID in a private cleanup ledger. No personal records, native document/page/ink,
credentials, live databases or tablet identifiers enter synthetic payloads.
The initial ceiling is 32 created files and 2 MiB uploaded synthetic data per run;
stop before exceeding it. These are proposed run bounds, not provider limits.

## Frozen execution inputs

Pin the accepted Buddy adapter/source and paired Docs revisions, maintainer-owned
harness revision, OAuth application/account binding, descriptor bytes/digests,
original group/scope/slot IDs and two independently authenticated client contexts.
The test harness must call the existing prepare_slot, create_or_read_slot and
observe_prepared_slot paths; it must not emulate Google or add an alternate sync
engine. Do not activate the application worker, restore a Store, select domain
winners or touch a tablet. Local-only and unsupported shared paths stay available
or fail closed exactly as before.

## Required observations

1. Verify pre-generated IDs work for ordinary metadata-only files in the actual
   appDataFolder. Capture exact-ID retry/conflict and complete pointer reads.
2. Release two independent contenders at a barrier for the SAME fixed ID, with
   distinct immutable descriptors and the same agreed base/scope. Require exactly
   one retained pointer; both observations must agree on it. Record response
   outcomes separately from later confirmed observations; a timeout is not freedom.
3. Interrupt acknowledgement after an attempted create. Recover by observation of
   the original ID, retaining original descriptor and request identity. Never
   allocate a successor or republish a stale candidate after losing.
4. Test one account/application across supported browser, Electron and tablet
   registrations, token refresh and independent sessions. Qualify actual hidden
   data and private property visibility; equal account IDs or matching project
   labels alone are not evidence. Test changed account/application refusal before
   object requests using the existing prepared-context checks.
5. Test missing, corrupt or mismatched descriptor/pointer and an unrelated scope.
   Retained incomplete/corrupt data must refuse without selecting/applying it.
   Keep malformed-object injection confined to owned resource IDs.

Repeat contention with a predeclared bounded sample count (proposed ten fresh
slots); passing samples support the tested binding only, not universal atomicity.
A failure rejects that candidate/binding. Do not broaden scope, replace private
properties with public ones, switch to personal Drive folders, or substitute a
last-writer-wins protocol without a separately reviewed design.

## Harness implementation contract

Use the opt-in `drive_slot_qualification` Buddy example on a protected Unix
host. Ordinary Cargo and CI targets may compile it. They do not run its live
commands. With no command, it prints usage without reading any run or grant.
Keep the selected Worker and production qualification decisions out of the
harness.

The private, explicitly approved plan identifies the run, group, source and
Docs pins, expiry, request and rendezvous bounds, and the actual role-to-grant
mapping. Browser, Electron and tablet roles may share an existing OAuth
registration. Record sharing explicitly, use independently issued grants,
and require each origin's exact pointer, properties and bytes to be visible to
each reader. An absent or failed mapping leaves that row unqualified. A host
run using a registration's real grant does not establish platform runtime
behavior. Observe refresh through the existing expiry-triggered path, record
whether it was triggered naturally or deliberately, and use protected files
for dedicated run-only grants. Refresh can rotate those credentials.

Build the example from the clean Buddy revision selected for the run with
`cargo build --locked --example drive_slot_qualification --features
drive-slot-qualification`. Use its `--help` for the argument shape. In a
dedicated mode-0700 directory, prepare a private `plan.json` with version 1,
non-nil distinct `run` and `group` UUIDs, full `buddy_revision` and
`docs_revision`, `expires_unix`, `request_seconds` set to 10, a
`rendezvous_millis` bound between 1 and 10000, and six ordered `grants`.
The order is Browser, Electron, tablet, same-registration contender, wrong
account and wrong client. Each entry has `binding_sha256` (SHA-256 of the
adapter's compact JSON tuple of client ID, account permission ID and group)
and an explicit `stimulate_refresh` boolean. Store the dedicated 0600 grant
files as `browser.json`, `electron.json`, `tablet.json`, `contender.json`,
`wrong-account.json` and `wrong-client.json`. The last two grants are local
refusal controls and do not make provider requests.

The approved plan byte hash gates `allocate`. The returned frozen hash
gates `run` and later exact-ID observation. Use `report` for sanitized local
evidence and its current journal hash. A separately approved `cleanup` also
requires that journal hash and an explicit deadline. Allocation and run use
the same plan deadline. Later observation and cleanup have separate deadlines
with at most an hour remaining at invocation. The example checks its embedded
clean Buddy source revision against the pin before any live operation.

Separate ID allocation and plan freezing from sends. The frozen ledger
binds exact IDs and deterministic synthetic bytes. Require the frozen digest
for dispatch. Persist one-shot consumption and each send's reservation before
dispatch. Stop on expiry, failed checks or missing grants. A subsequent
invocation can report the ledger or observe its exact IDs. It cannot replay
the run. The sole planned retry is a same-ID replay by the verified winner.
Use a cancel-aware rendezvous with a finite timeout immediately before the
two contender POSTs. Record each POST result independently of the subsequent
pointer reads. Record a separate deliberate lost acknowledgement between
POST and the adapter's same-call read, then recover by exact-ID observation
in a fresh client.
After both contenders return, open a fresh client from the selected Browser
grant for a third exact-ID and byte comparison. This is a fresh transport
session using the same registration and grant, with no claim of an additional
OAuth grant.

Allocate 27 IDs, including two deliberately absent IDs. At most 25 files may
be created. Ten fresh race slots share two immutable same-base descriptors
for transport qualification. This does not exercise ten domain operations
or validate aggregate ancestry. One separate lost-ack slot reuses a
descriptor. Three registration matrix slots have three descriptors. Three
occupied negative slots share one extra corrupt-body descriptor and an
allocated-but-absent descriptor. One unrelated slot has its own descriptor.
Cap each descriptor at 4 KiB, each metadata POST at 8 KiB and each multipart
POST at 16 KiB. At most 29 metadata POSTs and seven multipart POSTs yield a
344 KiB planned maximum. Charge actual encoded bodies and every uncertain
send before dispatch. Keep the 32-file and 2 MiB outer ceilings.

The negative fixtures use only the frozen IDs and closed shapes for a
missing property, missing descriptor and corrupt descriptor bytes. Observe
them using the ordinary agreed-slot reader. Start separate, approved cleanup
after the contenders have stopped. Reverify the frozen ledger digest, fresh
originating binding, literal private properties and exact current descriptor
bytes before a per-ID delete. Keep
uncertain or mismatched entries. Do not search the app-data space or delete
anything automatically. Public reports show roles, outcomes and digest
comparisons without private IDs, credential data or raw provider responses.

## Evidence and cleanup

Keep HTTP bodies/tokens/account IDs/private resource ledger out of public logs.
Publish source/harness hashes, redacted client-binding labels, requests/outcomes,
barrier and fault descriptions, exact pointer/descriptor digest comparisons,
sample count, failures and limits. Wall clocks are diagnostics, not ancestry.

Cleanup is a separate explicitly authorized operation limited to exact ledger IDs
created by this run, verified against owned run/group/digest identity first.
No broad search-and-delete, account/app removal or whole appDataFolder deletion.
If ownership cannot be confirmed, retain the object and report cleanup incomplete.
Final evidence must distinguish local modeled acceptance, observed provider
behavior and remaining domain/native/first-release gates.

## Source basis and boundaries

Google documents generated IDs for drive and appDataFolder in [files.generateIds](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/generateIds).
Its [creation guide](https://developers.google.com/workspace/drive/api/guides/create-file)
describes conflict responses on retries of a successfully created pre-generated
ID. This is supporting documentation, not proof of the complete proposed protocol.
[Application data documentation](https://developers.google.com/workspace/drive/api/guides/appdata)
describes application-specific hidden data, required appdata scope and sharing/
trash restrictions. [Private property guidance](https://developers.google.com/workspace/drive/api/guides/properties)
requires OAuth client authentication and documents property limits. Actual
cross-registration visibility and contention remain unqualified.

Current project requirements and accepted generic adapter/inventory contracts
supply the test semantics; resource choices, sample count and run ceilings above
are proposals for coordinator review. This contract does not authorize execution
or close SDK REM-50's separate protected GitHub release qualification.
