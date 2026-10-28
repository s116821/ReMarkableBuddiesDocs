# Resident historical capture consumer

Upgrade the existing Buddy consumer to SDK revision 3 and expose CaptureSource
through ResidentConnection and the installed Session request dispatcher. The
caller supplies the expected ReaderFacts; SDK correlation must validate both
returned source samples against those facts. The owned HistoricalCapture remains
historical image evidence, not a PageObservation, input epoch or write lease.

Use the same original deadline, input progress, main-thread health and runtime
integrity checks before, during and after transport. Ordinary cancellation,
deadline and EOF retire the connection while retaining the resident child.
Malformed image, source mismatch and protocol correlation failure are integrity
failures. Never automatically retry capture or renew canceled input admission.

Capture is read-only and does not reserve or complete a mutation journal entry.
Original v1/v2 insertion and selection bytes/digests must survive restart and
append unchanged. An unresolved effect remains unresolved after capture or
connection retirement; later effects must still refuse until separately admitted
proof settles the reservation. A read-only Reconcile reply or target-presence
observation does not itself provide that settlement.
Keep the journal's control-frame bound unchanged even though live capture
responses can exceed it.

Exercise the production runtime/request/client route with an owned socket child:
large valid image, changed source, corrupt image, timeout, input cancellation,
same-process reconnection, and preservation of earlier unresolved effects.
Verify original v2 fixtures in addition to the retained v1 corpus. These modeled
checks establish consumer policy only. Actual native capture, first-gesture
Reader/Writer/blank-start composition and native acceptance remain required.

The observation-only development example must pin the matching revision-3
profile and library from SDK80b29eb's capture-native-library-r2 build. Changing
those compile-time pins prepares a new artifact; it does not update, replay or
requalify the frozen revision-2 bootstrap candidate. Version-1 diagnostic
candidates still issue one Observe only, with no retry or navigation. Version-2
capture candidates follow [resident-capture-setup.md](resident-capture-setup.md)
and require explicit setup, fresh admission and independent recovery.
