# Same-runtime connection retirement and reconnection

Buddy `40adfbe` adds explicit socket retirement and reconnection to the owned
ResidentRuntime. It retains the original child identity, copied artifact pins,
consumed admission and Store. Reconnection validates these before and through
the handshake and never reruns activation, spawns a replacement or replays an
effect. A failed reconnect leaves the child owned for later explicit recovery
or shutdown. Installed lease/group/health admission remains the caller's job.

ConnectionFailure retains the SDK cause and lost-request identity through
anyhow. EffectFailure distinguishes transport, reply-retention and unresolved
prior-effect refusal. Original uncertainty survives socket retirement, a failed
new handshake, observation failure, repeated reconnect and shutdown. A renewed
connection with unresolved work permits historical observation/reconciliation
but refuses effects even for a different conversation before journal or wire IO.

The owned Python child fixture accepts multiple connections without consuming
another admission and asserts fresh connection/handshake identities. Four new
Rust regressions exercise idle EOF and cancellation with an unchanged process,
changed artifact/consumption refusal before handshake, actual dispatched
selection cancellation through later observation failure, and before/after
reply-publication loss across a canceled reconnect and new-conversation refusal.
The fixture models immediate idle retirement instead of waiting 30 seconds;
it does not qualify the actual native endpoint's timer or owner reclamation.

Independent source review found and accepted a correction: a failed new
handshake originally returned NoPendingMutation despite retained old uncertainty.
The runtime now rebinds only that lost field to the original operation/digest,
preserving the exact new failure cause. The combined regression covers this
failure and a subsequent successful reconnect plus shutdown.

Formatting, diff whitespace and Python fixture syntax passed. Source review
accepted the corrected code. Compilation, execution and hosted CI are pending;
the host has insufficient disk for another local build. Earlier c3ba9c1 test
results do not validate this new revision. Do not mark the installed request
route or native acceptance complete based on these runtime primitives.

The existing installed Session connection helper still conflates request failure
with fatal session failure. It must gain typed input/health classification and
retain lease/group admission through actual requests before product wiring.
First-gesture source reacquisition, Reader/Writer flows, package lifecycle and
native acceptance remain open in the coordinated change.

Source basis: current implementation, retained prior validation output and
independent source review. No new tablet action or capability activation occurred.
