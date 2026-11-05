# Bounded composed-publisher panic witness

Status: focused test-only precode for the already accepted composed-memory
publisher at Rust2f6f738/source4e79104 descendant. This does not implement native
output or grant a new SDK capability. Existing protected Cargo/native files and
SDK pins remain byte-identical; no device, model, account or service operation.

The accepted result leaves runtime panic behavior source-reviewed only. Existing
Store Fault values return errors and therefore cannot witness an unwind while the
actual selected receiving pins and combined admission gates are held. An unrelated
panic or standalone Mutex test would not satisfy this gap.

Add a cfg(test)-only, thread-local one-shot panic arm immediately after the actual
SelectedMemory joined-publisher callback marks its receiving view consumed, and
before it returns validation to the existing Reader writer. The hook exists only
in the unit-test build; no public fault enum/API, environment switch, production
branch, persistence format, dependency or native interface is added. The normal
production path and original data-only publication remain unchanged.

A dedicated unit-test child uses actual Store, selected catalog/aggregate/Reader
admissions, real receiving query and the same actual Provider publication route.
It sets up a valid current request and immutable source/image records, arms the
one-shot hook, calls the composed method under catch_unwind and proves the intended
panic occurred at that point. Reusing the same receiving view must refuse through
its poisoned pins; a new view/admission handle must not silently recover poisoned
shared gates to publish in the same live process. No assistant draft/receipt or
current Attempt state may appear, and original data/image bytes must remain.

Reopen after dropping the affected process-owned handles may establish ordinary
fresh data authority through existing APIs; it must not reinterpret the failed
operation as a historical acknowledgment or silently replay it. Scope the test's
assertions to actually available data APIs. If a claimed recovery expectation is
not part of existing semantics, retain it as an open gate rather than invent it.

Run only this dedicated test in an owned child with a finite20s deadline; timeout
fails and kills/waits the exact child. Keep the one-shot arm thread-local so parallel
unit tests cannot affect each other. The parent must not count a caught test-harness
panic as success unless the expected callback witness and no-publication/retry
assertions complete. Preserve a normal positive composed control already recorded;
do not rerun unrelated broad matrices or call native gates passed.

Before source changes, existing independent review checks exact injection placement,
production cfg exclusion, actual fixture route, poisoning/refusal and child-bound
ownership. Freeze the smallest test-only successor and execute from exact immutable
committed source using the existing checkout/export process. Record exact revisions,
child result and source/production limitations; no source pin/protected modification,
merge/Done/sync/archive or full3.20/4.7 acceptance follows from one panic witness.

Source basis: current central composed-memory-admission/result/tasks, actual
SelectedMemory::publish_selected_reader_text callback and SelectedAdmission joined
writer/ordered gates, and the existing error-only Store fault/test controls.
