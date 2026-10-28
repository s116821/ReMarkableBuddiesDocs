# Explicit native capture setup

The existing version-1 single-Observe experiment remains unchanged. A version-2
native candidate may additionally select a capture plan: expected document UUID,
page UUID and complete ordered page UUID list (one through seventeen entries).
These are independently selected fixture intent, not observed Reader authority.
The existing reviewed profile/library hashes remain compiled into the observer.
Both examples now require `--features development-resident-bootstrap`; the
separate diagnostic CI build supplies it. Normal release packages do not.

The actor and observer each end their launch input admission explicitly. They
exchange durable records bound to the candidate digest, nonce, observer process
and complete resident runtime incarnation. Setup-ready is published only after
both admissions ended. Only then may a separately reviewed developer setup driver
open the disposable source. Product code performs no menu setup. The unchanged
native library contains no fixture-opening hook.

Setup-complete must echo that exact binding. It is a completion signal for the
setup action, not a claim of page readiness. Both participants acquire fresh input
observers exactly once and require quiet/released input. Neither resets a canceled
guard. Each waits for the other's fresh-admission record while continuing its own
quiet checks. Duplicate, preexisting, partial, changed, stale or misbound records,
process replacement, service/context changes and deadline expiry abort the run.
Records are exclusively created and synced before a separate completion marker;
readers retain file pins through capture. Failed attempts are never replayed.
After the reviewed developer setup has ended, the fixed
`resident_bootstrap_control setup-complete NONCE` entry verifies the candidate,
original actor and stopped services, both ended-admission records and the ready
binding, then publishes completion exclusively. It performs no UI action.

The observer uses one overall 180-second bound from entry, at most 60 seconds for
launch, at most 120 seconds for setup, and at most 10 seconds for its single
CaptureSource request, each capped by the original overall deadline. Setup cannot
renew any deadline. Existing actor/PID1 and independent recovery bounds remain.
The runtime, artifact and inactive-service checks continue throughout setup;
transport readiness never substitutes for Reader identity. Capture itself proves
both native source/full-order joins through the SDK. There is no preliminary
Observe, repeated request, page insertion, navigation or writing in this mode.

After both fresh admissions, explicitly reconnect once to the same verified child
before sending CaptureSource. The initial connection may have reached the SDK's
30-second idle retirement while setup was in progress. Reconnection and capture
share the same at-most-10-second request bound and all fresh guards/pins. This is
not a retry after capture failure. Test idle retirement with the actual owned
runtime/peer, proving one new handshake, unchanged child, one CaptureSource and
zero Observe/effect commands; guard refusal or expiry must send no capture.

Always shut down the owned child before reporting capture or setup failure. Save
the validated PNG and its identity/hash metadata as historical evidence only.
Original uncertain mutation history remains untouched. Stock-first independent
recovery remains mandatory even when preservation or capture fails.

Source preservation initially remains byte-exact for the entire original source
inventory in both actor and recovery. No metadata exemption is granted by this
setup protocol. Before a native candidate can be selected, inspect its backed-up
disposable fixture and qualify any necessary opening-metadata policy with narrow
typed fields; unrelated documents, page order, PDF/ink and unknown fields must
remain protected. A whole-directory exemption is forbidden. This implementation
alone is not a runnable approved native packet or installed first-gesture flow.

Owned host tests must cover the two-participant barrier, delayed/partial records,
wrong binding, replacements, input cancellation, expiry and single-use admission.
These model process coordination only; actual UI setup and persistence remain
native acceptance requirements.
