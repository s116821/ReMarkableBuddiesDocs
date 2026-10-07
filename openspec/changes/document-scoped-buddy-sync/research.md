# Source basis and mechanism limits

Read October 6, 2026. These are repository/API facts and candidate design inputs, not performed live-provider or hardware tests.

| Source | Finding / design consequence |
| -- | -- |
| [Drive upload guide](https://developers.google.com/workspace/drive/api/guides/manage-uploads) | Pre-generated IDs prevent duplicate creation; a retry after successful creation returns 409. Multipart sends metadata and small ordinary-file content in one request. This supports candidate create-or-read slots, but the guide does not by itself prove all interruption/concurrency cases required here. |
| [Generate IDs](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/generateIds) | Supports `appDataFolder`; IDs are generated for the requesting user. Explicit account/app binding is required; arbitrary cross-account group use is not assumed. |
| [Drive app-data guide](https://developers.google.com/workspace/drive/api/guides/appdata) | App-private namespace cannot be shared using ordinary Drive sharing; cloud data can be deleted. Maintain local data/external backups and treat transport removal as recovery, not logical deletion. |
| [Drive files update](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/update) | No verified media compare-and-swap contract was selected from this reference. This is not a claim that conditional headers are universally unsupported. |
| [rclone Drive limitations](https://rclone.org/drive/#duplicated-files) | Names can be duplicated and listings can lag. Name lookup/list-then-create cannot prove a unique group/document owner. |
| [rclone bisync concurrency](https://rclone.org/bisync/#concurrent-modifications) | Maintained snapshot/recheck behavior reduces risk during changes, but does not establish this application's first-valid-commit document transaction. General file mirroring is insufficient for the required policy. |
| [REM-36 archived research](../archive/2026-09-27-shared-storage-sync/research.md) | Existing bounded worker, app-data scope, idempotent object upload and uncertain-removal handling are reusable. Its causal-branch policy was not first-writer adjudication. |

Current project issue chronology supplied the mode separation, document conflict boundary, first-valid-commit replacement policy, native exclusions, media inclusion, hardwired Manager control and domain ownership requirements. They are published in this proposal and scenarios so contributors need no private issue access. Repository facts were inspected at the exact revisions recorded in proposal.md. The commit-slot chain, catalog registration and selected aggregate projection are proposed engineering inferences requiring independent review and qualification.

Open questions requiring evidence: simultaneous different-client create at one pre-generated ID; what is visible after an interrupted multipart create; whether a partially claimed ID can safely complete without weakening winner identity; required operation-fence seam in the active REM-37 ledger; owner-approved projection of records that reference multiple or unknown source documents. Fail closed rather than inventing a lock/timeout fix. No credentials, user documents or provider account contents were inspected for this research.
