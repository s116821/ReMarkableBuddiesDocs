# Manager consumer for isolated backup preparation

This work consumes [ordinary isolated root provisioning](isolated-root-provisioning.md)
through the existing privileged wired host. It does not create another publisher
or provider protocol. Root owns the Manager consumer; the Buddy producer remains
in its existing scope.

## First source increment

The host privately retains the complete successful inspect snapshot and the
original version-1 provisioning input. Preparation requires an existing isolated
choice. It never substitutes a LocalOnly/shared choice or invents a grant from
Manager sign-in. The exact operation UUID, conditional token, device, backup,
epoch and binding remain associated with the operation across output loss.

The private consumer accepts one bounded UTF-8 JSON line, checks the complete
producer envelope and the existing saved-mode snapshot grammar, and correlates
the result to the retained original. It preserves early errors without inventing
result custody. An absent isolated_root member is distinct from a null or
malformed member. It checks each outcome/status/incomplete combination and derives
current versus historical from the original token and immutable epoch choice.
A result-bearing report must retain the Store actor and persisted device and
report an explicit current mode. At the original epoch it must retain the full
original token, backup and grant. A later epoch requires a different token;
reusing the original backup also requires the original grant. A changed device,
unconfigured mode or contradictory token cannot be accepted as historical.
Malformed UTF-8/JSON is reduced to a fixed refusal without input excerpts, and
outcome values must be literal supported strings before enum lookup.

Only the reduced saved-mode view and result identifiers/outcome/currency may
leave this parser. Input tokens, grant digests, provider IDs, credentials,
operation UUIDs and raw output stay private. A verified root is preparation of
cloud storage, not evidence of a completed package, running publisher or native
page availability.

The focused tests combine explicitly synthetic contract frames with three
original Buddy command-harness report lines and their original request bytes.
Their hashes are checked before parsing current, historical and unqualified
outcomes. This validates the JavaScript consumer against Rust-emitted bytes; it
does not qualify a connected host action, real provider or tablet execution.

## Connected action

The following is the remaining consumer work, not a claim of implementation:

- Add the fixed command to the existing identity-verified wired maintenance
  transport, with the usual shared ownership, deadline and cancellation rules.
  Do not expose commands, paths, original tokens or credentials through IPC.
- Provide an explicit review and prepare action for an already selected isolated
  mode in the shared browser/Electron UI. Keep a lost response unresolved; a fresh
  inspect cannot stand in for the original provisioning result.
- Retain the original request for any explicit retry and use it byte-for-byte.
  Mode changes, account/grant replacement and connection or boot changes require
  refusal or separately reviewed reconciliation, never an automatic new root.
- Keep independent observations separate: saved mode, prepared provider root,
  latest verified package and current runtime status.
- Exercise the real host, transport fixtures, both UI distributions and current
  producer frames. Keep production qualification profiles unchanged.

The transport reuses `local_mode_choice_transport.py` and its fixed sync-mode
command prefix with the single additional selector `provision-isolated-backup`.
Only that selector accepts the original version-1 provisioning body and a total
budget up to 45 seconds, including identity checks. Its command phase is bounded
to 35 seconds to accommodate Buddy's existing 30-second provider window. The
observer has an independently configurable provisioning timeout, defaulting to
45 seconds; its existing ordinary timeout remains unchanged. Other selectors
retain their 12-second request and 8-second command bounds. Cancellation still
owns the child process, and lost or incomplete output is not an acknowledgment.
No transport retry, arbitrary command, path or endpoint is introduced.

Tablet credential installation, choosing isolated mode from Manager sign-in,
provider namespace visibility, backup browsing/download and replacement restore
remain explicit following integration. They use this same preparation action and
the already accepted archive/restore contracts. No desktop authorization ID is
treated as a tablet credential or provider-root binding.

## Increment checklist

- [x] Review the private validator and reconcile exact producer-emitted frames.
- [ ] Connect the fixed wired command with retained original ownership.
- [ ] Connect the shared browser/Electron review, prepare and recovery UI.
- [ ] Verify actual host/transport/UI behavior and coordinated source/Docs CI.
- [ ] Complete separately scoped provider and wired runtime qualification.
