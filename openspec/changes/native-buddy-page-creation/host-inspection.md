# Host-only native metadata inspection

September 26, 2026. Static evidence only; no native page operation or runtime probe has been executed by this worker.

## Provenance and limits

The coordinator exported the authorized development tablet's executable and verified its hash against the running executable. Local inspection independently matched SHA-256 `071d85beef3ef2d4cc0e11002140b27b82a2cc04a2ed740a5669f591069b77df`. The private export is 22,046,100 bytes, ELF32 little-endian ARM EABI5 hard-float, build ID `740ce43fa440369522f51f3102cfcd986327ba81`. Coordinator inventory identifies RM2 firmware 3.28.0.172, armv7l, and a stable process identity across its passive pass. Mapped Qt filenames end in 6.10.3; filenames are not a completed ABI compatibility check. The four inventoried XOVI/broker paths were absent.

The proprietary export and metadata extraction intermediates stay local and untracked. No executable was run, uploaded or distributed. No worker SSH, device transfer, service action, navigation, model call, pairing or sync occurred. No fixed addresses are published or proposed as hooks.

Static Qt string tables, metaobject references, revision-13 headers and method/property records were decoded with bounds and string-terminator checks. The controller's superclass reference resolves to TaskTracker. Interpretation follows Qt's [metadata layout](https://raw.githubusercontent.com/qt/qtbase/6.10/src/corelib/kernel/qmetaobject_p.h), [method record layout](https://raw.githubusercontent.com/qt/qtbase/6.10/src/corelib/kernel/qmetaobject.h) and [revision/flag definitions](https://raw.githubusercontent.com/qt/qtbase/6.10/src/corelib/kernel/qtmocconstants.h). These are private Qt implementation details, not a stable application API.

## Confirmed static signatures

Class: `xofm::libs::library::DocumentController`, superclass `TaskTracker`, property `Library* library` with `libraryChanged()` notification.

```text
bool addPageWithTemplateAndPageSize(
    entry::Id documentId, int insertIndex, QString templateName,
    QSizeF explicitPaperSize, QJSValue callback, QString pageUuid)

bool addPageWithTemplateAndPaperSizeFromPage(
    entry::Id documentId, int insertIndex, QString templateName,
    int paperSizeFromPage, QJSValue jsCallback)
```

Both are public meta-method records. Cloned shorter records exist down to documentId alone; actual default values are unknown. `pageUuid` is a concrete lead for a caller-assigned intended target ID. Its format, acceptance, collision handling and retry semantics are not established. Neither bool return nor callback implies durable creation without runtime evidence.

## Ownership and serialization leads

| Static observation | Qualification still required |
| --- | --- |
| TaskTracker has bool isRunningTasks and isRunningTasksChanged(). Its onFinished/onFailed records are private slots taking shared task objects. | Busy scope, task identity, concurrency and completion meaning. Do not call private lifecycle slots or treat aggregate idle as a transaction receipt. |
| Library has bool isReady; signals include entryHasPendingStoreLines(entry::Id,bool), entryLockContested(entry::Id), changed(), statusChanged(entry::Id), entityChanged(...). | Establish which relate to this exact operation and whether any indicate durable metadata/page-order persistence. Generic change signals alone are insufficient. |
| DocumentLockManager has document: QmlDocumentWrapper*, taskTracker: TaskTracker*, onDevice: bool; pageModified and linesStored are slot records. | No public acquisition/release transaction was established. Slot names do not authorize manually calling them or prove locking guarantees. |
| Resource-name leads include AddPageButton.qml and page/document UI resources. | Bodies and runtime call paths have not been established; names alone do not prove PDF insertion behavior. |

Qt [thread affinity](https://doc.qt.io/qt-6/qobject.html#thread-affinity) requires owner-thread consideration. The actual controller object, its owner thread/event loop, QML registration/access, engine lifetime and document identity source remain unknown. A public project's QML access pattern is a lead, not proof that this firmware exposes the same objects. Any future adapter must use bounded asynchronous dispatch with lifetime and cancellation guards; never infer safety from a static signature.

## REM-37 acquisition contract implication

Preserve the proposed distinction between intended_target_id and observed_target_id. The explicit pageUuid parameter strengthens the case for preallocation, but keep capability-gated until qualified. Prepared records include operation_id, conversation_id, captured source document/page/revision/order/session/visit and expected binding heads. NativeCommitted requires a receipt correlated to that exact operation, exact expected page-order transition and observed target identity, plus qualified persistence evidence. REM-37 binding CAS follows NativeCommitted and records BindingCommitted. Ambiguity becomes ReconcileRequired; it never triggers blind native replay. Receipts and phases belong to the device-local REM-25 journal, not a second REM-37 journal or synced command channel.

## Next bounded experiment for separate review

Prepare a host-reviewed, narrowly scoped read-only runtime discovery probe only after the coordinator selects and qualifies its loading/rollback mechanism. The probe would report the matching process/build fingerprint, existence and exact runtime meta-signatures of the controller/library objects, owner-thread identity, engine/object lifetime, and read-only readiness/busy/document/page identity observations. It must not invoke page creation, callbacks, lifecycle slots, lock actions, arbitrary user-supplied QML or file writes. Owner-thread property reads require an active event loop, timeout and safe cancellation/lifetime handling. Loading itself changes the process and requires separate coordinator dispatch; the passive inventory did not authorize it.

If object access or a compatible loader cannot be established safely, continue host-only resource/call-path research. Only after runtime discovery and a reviewed disposable-fixture plan should a separately authorized one-insertion experiment test explicit pageUuid, exact order, callback/return timing, persistence, PDF mappings, undo/redo and interruption behavior. No feasibility gate is passed by this report; candidates A-F and Q0-Q10 remain open.
