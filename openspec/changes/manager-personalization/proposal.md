# Why
REM53/REM42 require a shared personalization editor. An editor can become useful once the actual narrow Rust configuration/readback command is published; it must not pretend disk persistence activates a running request.

# What Changes
Integrate inspect/edit/save/disable/clear in both Angular browser/helper and Electron over existing hard-wired host adapters. Preserve multiline Unicode and exact text, enforce the actual versioned field contract and stale-write digest, display verified disk readback separately from restart-required activation. Use the backend's existing Store lease/CAS, not a second config writer or Buddy service API.

# Capabilities
## New Capabilities
- `manager-personalization`: shared personalization editing through the actual bounded configuration command.
## Modified Capabilities
None until the published seam establishes a required cross-capability change.

# Impact
Shared UI, narrow authenticated host actions, fixed CLI stdin/readback transport and focused actual protocol/shared browser/Electron fixtures. Central Docs pairs with the future concrete Manager implementation; no planning-only delivery or source version minted. Main/Root's Sol lane owns the Rust/config/CLI contract and broader request-context application.
