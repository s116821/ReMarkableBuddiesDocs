## Decisions

Keep the current upstream tools, package builders, inventories and publisher unchanged. The calling ci.yml has one Checks job plus an application-only reusable workflow. The reusable workflow has Build, Integration and Release, so docs-only changes never enter the publication concurrency queue. Buddy runs three jobs on PRs and four on main. Manager runs four on PRs and five on main: one Windows Checks job, one Linux Build job, Linux/Windows Integration and final Release. Its existing Linux prechecks run at the start of Build before candidate calculation or compilation; no Linux or Windows tests are removed to reach the limit.

Checks performs existing metadata/range/path/title checks, existing lint/unit checks, and the local workflow topology control. Application-specific steps are conditional on the maintained path filter. There is a single application output, avoiding matrix-output ambiguity. A failed Windows Checks or Linux precheck prevents application compilation. The standalone title policy remains only for non-main target branches; main PRs have no duplicate title job.

Build first calculates the existing read-only semantic candidate. It then compiles the same pinned uploader recipe and existing application packages. It returns the frozen tag/SHA, uploader artifact ID/bundle digest, and application artifact IDs.

Integration downloads the exact Build artifact IDs. It runs existing application artifact checks on each supported host. Linux additionally verifies and executes the built uploader and the existing pinned metadata Action controls against loopback only. No production credentials are passed to these tests.

Release retains its existing exact merged-main admission, semantic/tag checks, remote identity checks, same-ID retry, missing-only upload and exact notes serialization. It depends on all Build/Integration success and never rebuilds. PRs skip publication. Docs-only changes skip the reusable workflow entirely.

## Compatibility and acceptance

The existing required-status contexts are not currently readable through this chat's connected endpoint, and direct network access is unavailable. Read them before delivery. A renamed context must not weaken branch protection or leave an impossible pending requirement. No repository settings are changed by this preparation.

Preserve all historical GitVersion and failed publication evidence. Reconcile each current PR against the corrected main workflow, preserving its unfinished feature changes and resolving CI conflicts explicitly. Do not paste new YAML onto an old branch that lacks its current release helpers. Record exact branch heads and identify stale superseded CI drafts instead of blindly merging them. This work does not require rebuilding applications locally solely for YAML restructuring; focused workflow/action controls, actionlint and actual hosted checks on the final PR remain required. Hosted/platform evidence remains pending until publication access is available.
