# Public evidence and unresolved limits

Research read September 26, 2026. These are source-backed API facts and design inputs, not performed account/device tests.

| Source | Finding used |
| -- | -- |
| [Drive app data guide](https://developers.google.com/workspace/drive/api/guides/appdata) | `drive.appdata` grants app-private storage; appData cannot share, move between spaces or trash. Users can delete it; uninstalling the app from Drive removes that data folder. Therefore keep local copies and external export, and use explicit logical tombstones. |
| [Drive upload guide](https://developers.google.com/workspace/drive/api/guides/manage-uploads) | Pre-generated IDs permit idempotent retry, with 409 after an already successful create. Resumable sessions expose server-confirmed progress and expiration; use immutable ordinary JSON/binary uploads rather than Workspace conversion. Verify a conflicting ID's content before acknowledging. |
| [Generate IDs](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/generateIds) | `space=appDataFolder` is supported; allocate/persist a file ID before creating an immutable object. |
| [Changes list](https://developers.google.com/workspace/drive/api/reference/rest/v3/changes/list) | Removed entries can mean deletion or loss of access. App-data space and paging are explicit. Do not translate transport removal into a domain tombstone. |
| [Retrieve changes](https://developers.google.com/workspace/drive/api/guides/manage-changes) | Follow all next-page tokens and retain the new start token for subsequent polling. Our durability rule adds local commit-before-checkpoint and replay tests. |
| [Files update reference](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/update) | The reviewed reference does not establish atomic media `If-Match` compare-and-swap semantics. Absence of proof is not a claim the server never supports a conditional header; this protocol avoids needing it. |
| [OAuth installed applications](https://developers.google.com/identity/protocols/oauth2/native-app) | Native clients use explicit authorization and token refresh; granted scopes need checking. Keep grant acquisition separate from the record store, fake all credentials in this lane. |
| [Rust File lock API](https://doc.rust-lang.org/std/fs/struct.File.html#method.try_lock) | Standard file locking is available from Rust 1.89 (project MSRV 1.96). Current Unix implementation uses flock, Windows uses LockFileEx; lifecycle/interop must be tested, not inferred from a PID file. |
| [Historical official factory-reset release note](https://support.remarkable.com/s/article/Software-release-1-4-June-18-2018) | Vendor describes reset as removing files/settings. This older note is not evidence that a particular current custom directory survives any firmware action. Design treats reset as destructive and requires independent recovery. |

Local source facts at Rust `6fc7f9e`: `deploy/reader-buddy.service` retains `/opt/bin/reader-buddy`, `/home/root` working directory and existing protected environment file; `src/main.rs` defines current CLI/precedence. `src/device/backend.rs`, `src/workflow/mod.rs` and `src/workflow/symbol_pool.rs` show current cache/diagnostic/legacy state locations. No existing generic store or Drive adapter was found.

Unverified by this lane: actual firmware/update/reset persistence, vendor lock-tool availability, native power-loss behavior and live Drive OAuth/API execution. No hardware/account operations were performed. Host fixtures will prove implementation logic and filesystem contract under injected failures; they do not become native or live-account evidence.
