# Existing default configuration

[Buddy #163](https://github.com/s116821/ReMarkableBuddies/pull/163) reuses the first-configuration publisher from [Buddy #139](https://github.com/s116821/ReMarkableBuddies/pull/139). The existing-local operation holds the same Store lease used by the personalization writer. It uses the pinned publisher for the canonical path and requires absence of the legacy path before publication and during readback.

The [all-feature host test step](https://github.com/s116821/ReMarkableBuddies/actions/runs/45330060382/job/138228963015) passed at `da2df67a634839f1c72cb76734e48774b3c9363e`. It covers a populated Store, an existing conversation and credential sentinel, then exercises the ordinary personalization editor using the saved revision. It also covers a conflicting legacy file, a malformed or unsafe config entry, a busy Store, concurrent creation and a failure after publication. The clean setup regression uses the already delivered ordinary archive to verify restore with the original configuration and credentials retained. The isolated-backup fixture in Buddy #139 remains in that draft.

[Manager #83](https://github.com/s116821/ReMarkableBuddiesManager/pull/83) wires the existing-default check and create into the browser and Electron flows using the qualified installed Buddy launcher. Once the save is verified, the existing revision-checked personalization editor reads the new file.

## Physical first save

The device operator tested one existing default installation on a reMarkable 2 over USB using signed Buddy `0.78.0_pre1-r0` at `7d7c9e53` and packaged Windows Manager `0.41.0` at `8d029ee0`. The [Buddy package and integration run](https://github.com/s116821/ReMarkableBuddies/actions/runs/45350645796) and [Manager packaging run](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/45366951184) identify the candidates. The Manager run built merge revision `9354bfcb`.

- The wired check reported the configuration missing. One Save in packaged Electron created the default configuration and verified readback.
- After reopening Chrome with the packaged helper and reopening Electron, both showed the default personalization preference as empty, disabled, and editable. Chrome reported the on-disk revision.
- The saved revision survived a Buddy restart. Existing data, settings, and credentials were byte-identical in the stopped-state comparison. The operator left the personalization preference at its default.
