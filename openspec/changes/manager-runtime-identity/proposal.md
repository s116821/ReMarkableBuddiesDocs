# Why
REM41/42 require actual installed/runtime state alongside available releases. The Manager currently reads OS/service observations but never queries the known Buddy binary's existing --version interface. This bounded read can proceed independently of runtime activation, package installation and deferred human physical tests.

# What Changes
Add explicit guarded self-reported binary identity inspection in both browser/helper and Electron, reusing existing authenticated USB/SSH admission and narrow host boundaries. Display the reported value separately from installed package ownership/provenance and running-process version, which remain unknown. Do not treat it as a trusted Git tag, SDK/firmware compatibility or install/update eligibility.

# Capabilities
## New Capabilities
- `manager-runtime-identity`: bounded known-binary version observation and shared display.
## Modified Capabilities
None; existing observation and separately specified maintenance interfaces stay narrow.

# Impact
Fixed read callback, strict report/adapter/controller, shared display and meaningful SSH/host/UI evidence; central paired delivery. No new Rust command, SDK writer, Vellum wrapper/installation, service restart, source version or actual tablet operation. Main retains package/runtime/device ownership; uses accepted Manager38136/Docs9509 parents in existing checkouts.
