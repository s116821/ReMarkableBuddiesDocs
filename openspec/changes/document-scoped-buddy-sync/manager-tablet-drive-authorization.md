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
nonzero collection UUID chosen by the verified tablet workflow and emits
Buddy's existing V1 credential shape. Convert verified expiry milliseconds to
integer UNIX seconds once. The returned secret is private input for the
writer, never a browser response, IPC result, log, command argument or public
status. A missing, stale, expired or already-consumed reference yields no secret.

This private authorization helper cannot perform USB writes. The connected
workflow below binds the prepared authorization to the selected
connection, boot, Store actor, mode epoch and collection before confirmation,
and rechecks those facts before writing. Do not infer target authorization from
this private helper or its synthetic tests.

## Connected setup contract

### Shared host setup owner

The shared host owns one setup reference for the selected wired connection and
boot. Begin reads the existing mode token, then inspects the private credential
slot using that token. Only configured local-only or isolated-backup Stores are
eligible. A new credential uses a host-generated collection UUID; reconnecting
preserves the installed collection and account/client binding. The renderer
cannot supply credentials, a collection, paths, mode tokens or operation IDs.

Connect opens the existing tablet-purpose consent flow after that inspection.
Once consent succeeds, the owner consumes the private grant once and prepares
the exact bounded writer input. The user sees the selected tablet, account label
and whether this is a connection or reconnection. Remove prepares only the exact
inspected slot. Neither action changes the backup mode or provisions a root.
Confirm re-inspects the original slot and mode before sending the one-use write.
A changed target, original file, registration, account or expired authorization
requires a new preview. No secret is returned through either host bridge.

Use the existing shared maintenance admission and local-mode USB transport.
Release admission while the user completes browser consent. Active wired work
has the existing 13-second host / 12-second transport limits. The prepared
preview lasts at most two minutes and no longer than the access token. Another
maintenance owner, navigation, cancellation or host disposal invalidates an
unused preview; a late result cannot restore it or release another owner.
Navigation also invalidates a pending Begin before its first reply. A dispatched
Confirm or original Check remains application-owned while its view is hidden.
Explicit cancellation during possible dispatch preserves the unknown-outcome
warning and access to retained originals; a late reply or inventory refresh
cannot silently clear that warning.

Before possible dispatch, retain the original operation, inspected metadata and
desired digest through the existing protected DriveStore using compare-and-swap.
After dispatch erase the
prepared secret input. An ambiguous response is never retried: Check sends only
the original readback request. A matching desired file proves its observed
state, not which process wrote it. Original-state observation also does not
permit replay. Keep at most eight unresolved operations and refuse another write
for an unresolved target. These bounded records contain no tokens and survive a
Manager restart; Check uses their original request. Remove a record only after
verified resolution and a successful protected compare-and-swap. A changed
tablet boot or original custody remains unresolved rather than authorizing a
replacement. Closing Manager never retries the write.

The same file retains at most eight reduced connection/device/collection/binding
records. Verified installation or removal updates that binding atomically with
resolution of the original. An isolated backup whose credential file is absent
must recover its exact collection from this checked metadata before consent;
missing or mismatched provenance requires recovery and never guesses a UUID.
Unresolved originals reserve their binding slots. Capacity is checked before
consent and again in the protected pre-dispatch CAS, including concurrent hosts.

Both companions present this through the existing Backup & sync task. Installing
credentials is reported separately from enabling backups and from a successful
backup. Tablet credential removal is distinct from disconnecting the Manager's
cloud account or revoking the app's Google grants.
The browser shows the host-owned Google consent link. Electron opens that same
owned URL in the system browser and does not show a nonfunctional in-app link.

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
