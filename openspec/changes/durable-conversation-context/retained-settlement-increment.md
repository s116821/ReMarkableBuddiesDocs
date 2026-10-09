# Retained settlement and uncertainty reconstruction increment

This implements the retained-only part of the accepted
[selected intent migration](selected-intent-migration.md). Main owns domain code;
generic storage remains unchanged. Current source is Buddy `b51dd7d` with the
storage owner's `commit_retained` and final `selected_predecessor` interface.
No production backend qualification is available yet.

## One fact transition, one retained transaction

Use the existing OutputPending OutcomeFact's stable record ID. Append a causal
child containing the existing schema2 settlement extension, exact original
Receipt/Root/Turn references and original publication pins. Keep every prior
retained record/media reference. Call only Store.commit_retained with the current
minted token, original publication operation and actual original receipt ObjectRef.
Do not revise Root, Turn, source, binding or any active winner key. The winner
manifest preserves its scope, object/media references and their exact stored bytes.
Its publication transaction ID changes through the normal store publication path;
the settlement fact is also the durable latch
transition evidence, so no second journal or separately written latch is added.

Unknown remains ReconcileRequired. Explicit verified submitted/no-effect states
can release only that original intent's latch. They require a sealed domain
verification capability checked while the canonical aggregate admission guard is
held. Its proof must match the exact original intent and settlement request;
stored strings, timestamps, imports or callbacks cannot implement this capability.
There is no production implementer before the owning backend verification gates.
Synthetic test implementations must be labelled as such.

## Exact historical closure, current metadata guard

Recover the original committed preparation and actual publication/predecessor pins
before preparing new UUIDs. Require the original receipt and its complete causal
closure to remain reachable through current retained manifests, with the original
receipt exclusively retained. Shared immutable ancestors may remain in the winner;
they cannot authorize editing any active key. Validate
the current retained chain of the pending fact independently from active winner
heads. The original accepted closure is the authority for its typed references;
unrelated retained conversations and replacement current heads cannot substitute
for it. Conflicting fact heads, broken parent closure, foreign evidence, missing
bytes or wrong admitted intent refuse the transition and latch reconstruction.

Every supplied immutable evidence reference must exist in the retained original
closure and match its exact ObjectRef. This initial increment does not introduce
new backend evidence records: a later actual backend integration must specify and
verify those records before enabling a production verified capability.

Hold the canonical domain admission guard through current token validation,
verification and retained publication. An identical settlement operation retry
looks up and validates its exact historical retained publication before UUID
allocation and returns historical evidence without a live token or effect. A
changed request or original identity under that operation conflicts. Historical
recovery never refreshes a token; any new transition needs the current Store token.

## Reconstruction and verification

Reconstruct an original intent's uncertainty from the validated original pending
fact and its current retained causal head. No settlement or Unknown keeps the
latch. Only an explicit verified head with matching original intent linkage and
the current Store's actor can
release it. Replacement activation, elapsed time, sync/provider success and a
receipt lacking its admitted intent cannot release it. A verified head is terminal;
a later new transition cannot reopen it, while identical historical retry remains
available without a live token. Reconstruction is read-only
and cannot enqueue or replay effects. Missing/corrupt/foreign or conflicted state
refuses reconstruction; callers must retain uncertainty on that error.

Actual Store fixtures must exercise pending publication, replacement retaining
the original closure, unknown and synthetic verified transitions, exact winner
content preservation across publication metadata changes, original reference/pin
substitution, missing verification,
stale token, identical lost-ack/restart retry, changed replay request, and reopen
latch reconstruction. The storage owner already covers atomic retained metadata
publication; domain tests check old-or-complete transition meaning. All native,
Attempt/backend and imported-restore qualification gates remain open.

Source basis: current repository APIs and the accepted migration contract. This
is an implementation plan, not a claim that retained settlement is implemented.
