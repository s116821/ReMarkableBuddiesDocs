# Proposed disposable provider qualification contract

Status: reviewable execution contract only. No account, OAuth registration, file,
namespace, device or service has been created or changed. This is part of the
unfinished REM-52 delivery, not live-provider acceptance.

## Resource decisions required before execution

The coordinator must identify an explicitly authorized disposable Google account
and dedicated test OAuth application/project, protected local credentials, named
operator, and exact permitted client registrations. Use only drive.appdata scope
for this candidate. An existing Drive connector or its Personal/ChatGPT folder
does not establish access to this application's hidden data or permission to
exercise contention there. Prefer a dedicated test account/application; do not
infer authorization from the personal-cloud backup or tablet SSH setup.

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
