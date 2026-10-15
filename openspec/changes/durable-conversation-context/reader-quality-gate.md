# Reader quality gate: development fixture transport

Strict final74 lint has22 dead_code diagnostics. Two identify the development
transport variant and factory. All references to
Workflow.with_selected_development_capture / RefusingBackend.with_capture are in
cfg(test) modules: controlled Reader-context tests and actual-Orchestrator/saved
byte harness tests. No installed capture or operator CLI producer calls them.
The non-test RefusingBackend always owns Unavailable and refuses acquisition,
request guard and effects. This concrete test-only transport should be test-scoped.

Before source change, independently review this bounded disposition. Scope the
development factory, transport enum/field and development-only match branches to
cfg(test), preserving the ignored opt-in saved-byte harness and its assertions.
Make normal RefusingBackend explicitly refuse as before; add no allow attributes,
dummy calls, public APIs, feature/pin changes or fake native consumer. Existing
production DeviceBackend signatures/refusal and native admission interfaces remain.

The other20 diagnostics concern controlled Pending minting, ReaderSourceAdmission,
ReaderContext/Permit, once-only dispatch/reservation, uncertainty validation,
Attempt preparation/dispatch and private backend binding/dispatch. These are
needed unfinished SDK/native integration, not obsolete code to delete or hide.
Production qualified capture/live source+backend binding, native geometry/render
correspondence and lifetime/recovery are absent. Keep those source interfaces and
full task2.10 gate open; this fix must not be described as a green lint gate.

Verify normal nonmock compile and selected CLI refusal before credentials/device,
existing actual-Orchestrator seven-case control, development captured-byte and
controlled-context fixtures, and strict full-target diagnostics. Expected remaining
gate is20 native dead_code errors, not a suppression/waiver. Check final source
diff against protected9 hashes and exact committed SDK; get focused independent
review and update paired evidence. No repeated unrelated full Windows matrix or
new diagnostic product surface is needed for this conditional fixture scope.

Source basis: actual74 diagnostic JSON, exact call-site inventory and current
source. No new native observation or qualification follows.
