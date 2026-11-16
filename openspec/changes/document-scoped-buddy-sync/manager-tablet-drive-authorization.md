# Google Drive authorization for a tablet

Normal setup starts in Manager, uses Google's system-browser consent, and returns
to Manager for protected USB provisioning. Users authorize their own Drive
account. Application registration is maintained once for the distribution;
ordinary users do not create Google Cloud projects or manage token files.
The existing advanced developer registration remains useful for qualification.

## Host authorization increment

Reuse `DriveAuth` and its maintained Google OAuth client, PKCE, one-time state,
fixed endpoints, response bounds and callback listener. Add a private tablet
purpose to that same flow, alongside the existing Manager-host purpose. Do not
add a second OAuth implementation, renderer command, credential store, or
automatic provider call.

The tablet purpose requires a saved, previously verified host account. Capture
the original registration/grant digests and authentication generation before
opening consent. The newly exchanged token must pass the existing token-info
audience/expiry and Drive account checks, have exactly the `drive.appdata` scope,
match the original host account, and contain a nonempty refresh token distinct
from the host refresh token. Recheck the original protected records before
acceptance; a different account, registration or grant invalidates this flow.

The host's saved grant is unchanged. Keep the tablet grant only in private host
memory for at most five minutes and no longer than its verified access expiry.
Only a reduced status, account label and random opaque reference may be shown.
Pending authorization is not installed credentials, a prepared backup root or
a successful backup. Starting another authentication operation, disconnect,
revocation, cancellation, expiry, disposal or changed protected custody retires
the pending grant. A late callback cannot restore it. This memory lifecycle does
not promise cryptographic erasure from JavaScript's managed heap.

A host-only one-use take checks the exact reference, current generation and
protected digests, then consumes the grant synchronously. It accepts a canonical
nonzero collection UUID chosen by the later verified tablet workflow and emits
Buddy's existing V1 credential shape. Convert verified expiry milliseconds to
integer UNIX seconds once. The returned secret is private input for that future
writer, never a browser response, IPC result, log, command argument or public
status. A missing, stale, expired or already-consumed reference yields no secret.

This first source increment has no public bridge and cannot perform USB writes.
The complete workflow must bind the prepared authorization to the selected
connection, boot, Store actor, mode epoch and collection before confirmation,
and recheck those facts before writing. Do not infer target authorization from
this private helper or its synthetic tests.

## Remaining connected delivery

Use the existing fixed wired maintenance boundary and Buddy's guarded private
file writer. Creation requires absence; replacement/removal requires the
expected credential revision and serialization with refresh or a quiescent
owner. Verify atomic commit, private permissions and original readback. An
uncertain write retains its original operation for reconciliation, not replay.
Keep collection/account/client binding and explicit local-only versus isolated
or shared mode choices intact. Buddy owns subsequent refresh and backup after
Manager exits; host sign-in alone never enables that publisher.

Both companions must provide the same concise flow under Backup & sync. Local
disconnect and provider revocation remain different actions. Revocation may
invalidate other grants for the app and must explain that consequence. An
approved public desktop registration and actual provider/installed USB
qualification remain required before claiming this workflow delivered.

The existing [provider qualification contract](provider-qualification-contract.md)
keeps its independently issued Browser, Electron, tablet and contender grants,
wrong-account/client controls and bounded original ledger. A same-account
multi-grant test does not establish cross-user isolation.

## Verification

Use the actual locked Google library against owned loopback fixtures. Cover
distinct and duplicate refresh grants, missing credentials, wrong account,
audience and scope, protected-record drift during exchange and before take,
cancel/expiry/supersession/late callback, one-use consumption, exact V1 encoding
and unchanged host-grant bytes. Retain the existing refresh-rotation tests.
Source tests do not create real Google grants or qualify a tablet.

Sources: [Google desktop OAuth](https://developers.google.com/identity/protocols/oauth2/native-app)
and [Drive application data](https://developers.google.com/workspace/drive/api/guides/appdata),
plus the existing Manager authentication and Buddy V1 credential contracts.
