# Resident visual diagnostic source result

Buddy `87b63ad7793b0d17025b76e8df596fcbfaab2a58` implements the bounded
[diagnostic contract](resident-visual-diagnostics.md). The development observer
retains stage entry, return and error records before owned shutdown. SDK API
invocation is distinguished from preceding admission, but does not establish a
socket write or native dispatch. Records grant no page identity or write authority.

The predecessor native attempt `cc059b`, using Buddy `ec2897b` through CI merge
`a1d6e7f`, reached matching observer-ended and actor-ended records. It published
no before-image or ready marker and selected no input or setup completion. The
actor expired during a service observation; the retained evidence does not prove
that a visual request reached native code. Independent recovery succeeded.
Separate cleanup verified the unchanged 191-entry source inventory, restored
stock/companion/Buddy services and removal of only the two diagnostic definitions.
A separately captured and inspected stock image showed the normal My files UI.
These are recovery observations, not successful SDK capture evidence.

Final owned Linux validation compiled one library test executable and reused it
for the default and explicitly selected protected-root scopes:

- 776 library tests passed; 30 tests were explicitly ignored in the default run.
- All 14 setup tests passed with ignored tests included.
- The new owned-peer diagnostic runtime test passed with ignored tests included.
- Strict all-target/all-feature Clippy, formatting and whitespace checks passed.

The four added tests cover delayed/failing/expired progress, bounded diagnostic
refusal with mandatory shutdown, actual peer reconnect/API failures, and a
successful callback whose original deadline has elapsed by retention completion.
That last control does not isolate file-sync latency. Independent source review
accepted the final deadline anchors and error/shutdown ordering.

The first validation found a consumed-runtime reference in a new test; it was
corrected. A subsequent run was deliberately superseded before completion for
the final timing corrections. Neither is credited as final validation.

SDK remains `f03cc72`. The new Buddy ARM artifact and a separately admitted native
diagnostic remain required. No new native attempt uses this source yet. Actual
source capture, automatic creation/reuse, installed workflows, preservation and
write/reopen acceptance, simulator alignment and final delivery remain open.
