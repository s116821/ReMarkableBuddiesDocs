# Existing default configuration

[Buddy #163](https://github.com/s116821/ReMarkableBuddies/pull/163) reuses the first-configuration publisher from [Buddy #139](https://github.com/s116821/ReMarkableBuddies/pull/139). The existing-local operation holds the same Store lease used by the personalization writer. It uses the pinned publisher for the canonical path and requires absence of the legacy path before publication and during readback.

The host tests cover a populated Store, an existing conversation and credential sentinel, then exercise the ordinary personalization editor using the saved revision. They also cover a conflicting legacy file, a malformed or unsafe config entry, a busy Store, concurrent creation and a failure after publication. The pure check and absent-Store refusal are exercised without device contact.

Manager wiring uses the first-configuration UI contract from [Manager #76](https://github.com/s116821/ReMarkableBuddiesManager/pull/76). The browser, Electron, and physical save/restart acceptance remain with the coordinated integration.
