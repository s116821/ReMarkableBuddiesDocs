# Durable resident selection attempts

The existing Store-owned journal will cover insertion and current/adjacent target
selection as distinct typed effects. Its historical filename stays
`native-insertion-attempts-v1.json` to preserve one authoritative journal, one
Store lock and global consumed-operation uniqueness. The JSON schema advances to
format 2 on the next successful write; format 1 remains readable for insertion
history only. Existing record frame/digest/outcome fields remain unchanged by
upgrade. Older consumers refuse format 2 rather than silently ignore selection.
Limits remain 1024 total attempts and 8 MiB, without eviction.

Before selection pending admission or any bytes, retain the conversation, original
operation, exact canonical SelectAdjacent frame and original digest. The frame
contains the original source, target, complete expected order and connection
identity. No UI action, binding decision or native authority follows from merely
reserving it. SDK validation admits only an existing current or immediate-next
target; the native executor must freshly establish actual identity/order.

## Conversation admission

All effect operation IDs stay consumed forever, including known refusals.
A Reserved or Indeterminate insertion/selection blocks every later effect for its
conversation. Presence or current-selection reconciliation never clears this.

An observed insertion prohibits another insertion, but permits a new selection
of that exact document/target. An observed selection likewise permits subsequent
fresh selection of that same document/target and prohibits insertion fallback.
These are new caller-selected operations with fresh expected facts, never replay
of the old request. Their order may differ from an older successful observation;
the executor must validate the newly supplied complete order before acting.

A durably recorded NotDispatched or Rejected outcome permits a new operation
subject to all earlier reservations. A refused selection must not erase the
target restriction established by an earlier observed insertion/selection.
When there is no previous accepted target, the journal alone does not decide
whether a page belongs to the conversation; the existing qualified binding/reuse
decision remains a required caller precondition.

Known selection success requires a distinct TargetObserved response with exact
document, target and unchanged requested order, in addition to same wire revision,
scope, sequence, operation and original digest. An insertion response cannot
complete selection, nor the reverse. If reply publication reports failure, close
the connection and return the original indeterminate operation/digest; do not
automatically retry either effect or publication.

The actual valid stored record is authoritative when later loaded. Failure before
the outcome write leaves Reserved, which blocks both effects. If the complete
correlated reply was stored before an error was reported, reloading it recovers
that historical outcome: a stored observed result permits only a new same-target
selection; a stored known refusal permits a new operation subject to earlier
restrictions. Stored Indeterminate never becomes known merely by reloading.
This resolves publication acknowledgment uncertainty, not unknown native effects.
Every later effect still requires a successful synchronized write of the entire
journal, including prior evidence and the new reservation, before any bytes.
Reading a file alone is not a durability or effect-admission claim.

## Reconciliation and lifetime

One shared consumer effect path performs reserve/execute/outcome retention for
both command kinds, without automatic reconnect or retry. Read-only reconciliation
dispatches Reconcile for an original insertion or ReconcileSelection for an original
selection. Permit selecting a specific original operation as well as the latest
attempt for a conversation; unknown/mismatched originals refuse before IO.
It uses a new request operation and leaves every stored attempt unchanged.

Successful historical selection is not a capture/write lease, current binding
proof, native transition settlement or Supervisor recovery authorization. The
resident process effect gate independently retains uncertain native work.
This increment does not enable the installed Reader or the disabled native factory.

## Required checks

Exercise actual Store restart/restore and owned authenticated sockets: selection
journal before bytes; exact success; current/adjacent shapes; wrong kind/target/order;
lost/partial/indeterminate reply; reservation and reply publication failure,
including failure-after-successful-write followed by reopen and admission of both
command kinds under the actual retained outcome;
cross-kind reused operations; unknown selection blocking insertion and selection;
insertion-to-selection target matching; known selection allowing fresh same-target
selection while refusing insertion/different target; earlier target restriction
surviving a later known refusal; concurrent mixed effects; format-1 upgrade without
record rewrite; malformed/unsupported history; bounded capacity; original typed
read-only reconciliation without file changes or replay.

Source basis: current SDK v2 protocol/executor, Store-owned insertion journal and
the REM-25 current/adjacent reuse contract. The format-2 admission policy above is
this increment's design, to be independently reviewed and tested before delivery.
