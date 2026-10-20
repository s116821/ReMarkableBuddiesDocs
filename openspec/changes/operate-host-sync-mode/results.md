# Host mode implementation

Precode d7479bf was published before source and accepted in full independent
review5581679917. Exact initial implementation is [Buddy67](https://github.com/s116821/ReMarkableBuddies/pull/67)
1a06873074e0ca382b022d0524b0fbf673b4aa94 on delivered c5fc975. Source guide
docs/host-sync-mode.md defines the concrete report/status contract for the separate
inspection-only Manager consumer. Source and this active Docs change remain one
unfinished coordinated delivery.

The eight owned paths add a root command/report/startup module, unit/actual CLI
tests and guide, main/lib routing, a validated crate-private original-token input
constructor/choice-validator visibility, and selected-aware internal maintenance
opening. The mode setter/history/namespace semantics are unchanged. Public legacy
opening remains format1-only, including personalization refusal on selected stores.
The real main guard retains distinct ordinary-mode and legacy-data leases through
run_loop, before configuration writes and provider/device/domain constructors.
No reader_runtime/context/Orchestrator/prompt, Cargo or SDK implementation is imported.

Windows actual verification: six Store/unit controls pass (current-mode/process
lease during actual writer, prefix failure/release, uncertain after-commit result
and intentional original retry/historical receipt, ordinary mode/data lifetimes,
selected-aware versus legacy opening, and live publisher Busy preservation).
Eight actual CLI tests pass: local/shared/isolated choices/reopen, original and
changed/stale/foreign requests, inclusive16KiB file/stdin parity/refusal, no-repair
and busy/missing/partial/nonowned state, selected records/media/current generation
preservation, unchanged actual personalization refusal, startup negatives before
runtime constructors, legacy-sync refusal and option/path safety. Five existing
binary interface/routing tests pass. Additional Unix FIFO input/lock control is
present but not executed on Windows; hosted Linux remains required.

Strict all-target/all-feature Clippy and no-default library's six new controls
pass. Affected existing personalization8/config2/inspectionCLI4/memoryCLI16 tests
also pass. These are affected checks after changing routing/admission, not a
relabeling or replay of earlier accepted storage/provider/native matrices.

The first actual CLI run retained four failures in the task tool transcript:
one real wire-validation gap accepted an extra field on the internally tagged
unit local-only variant, while three fixture failures came from Windows mandatory
lock-file reads and poison dotenv in normal startup. The command now uses a strict
struct-shaped empty wire variant converted to the unchanged Store choice/validator.
Fixture inventories retain lock existence/size while preserving every actual data
file byte; ordinary startup uses valid dotenv after separately proving one-shot
routes ignore poison. Final logs are separate from those original failures.

The command's report is one <=16KiB JSON line with report_version1, operation,
status, incomplete, activation_performed=false and data. Data separates actual
current_snapshot from original receipt and receipt_status (current/historical).
Inspect/initialize have null receipt fields. Mode null is unconfigured legacy
policy, not explicit LocalOnly or a worker-inactive claim. Operator requests keep
their original token/UUID; no retry/fresh-token substitution or activation follows.

Current exact source hosted full CI, independent implementation review and final
canonical sync/archive/delivery remain pending. No provider, device, live-model,
service, account, restore or reverse-engineering action was performed. Existing
end-to-end sync and frozen Reader/native/model requirements remain unfinished.
