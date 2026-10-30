# Manager Drive authentication implementation evidence

Manager sourcedfd5fc217a7bace9ee0f70c74d016ce3684ed0e7, [PR15](https://github.com/s116821/ReMarkableBuddiesManager/pull/15),25-file delta over accepted original-fixture source10263. Existing implementation/Docs parents preserved; no new worktree/agent. Central pre-code cd78442 was committed before dependency/implementation changes; design evolved to accurately record synchronous commit and opaque revocation confirmation. REM42 ownership was posted in comment951ae959 before edits. Main retains provider/domain/Rust/native code; all unchanged.

## Implemented scope
Shared Angular/Tailwind account state works without a tablet. Maintained google-auth-library11.3.0 performs PKCE/auth code/refresh/token-info/revocation; fixed Google audience/appdata scope/actual Drive user identity are checked before protected host persistence. Cached restart state is explicitly unverified. The helper uses its existing origin/cookie boundary and a separate canonical192-byte fixed-action endpoint; prior64-byte wired endpoint unchanged. Electron main-frame IPC accepts fixed actions, with only one host-issued current-grant confirmation ID for revocation; browser consent is an explicit external link, native consent uses only host-minted URLs. No token/path/command/client/endpoint enters renderer parameters.

Protected fixed-file Python broker uses POSIX ownership/modes/nonlink/FD bracket or inherited independently qualified Windows handle/ACL reader. New Windows files have current-user/protected DACL at creation without takeover. Cooperative exclusive lock and original client/grant SHA256 CAS bracket atomic replace/delete. Final generation check precedes a bounded synchronous child commit; no host event interleaves before actual atomic commit. Cancellation afterward is not implicit disconnect/revoke; unknown receipt is unavailable, not proof of no write. Private stale lock/stage and hostile same-user/power-loss limits remain documented.

Explicit local disconnect does not call provider revoke. Revocation is separately confirmed, has cross-client impact preview, and refuses a changed grant/client before provider traffic. Error/uncertain outcome retains truthful state and custody. OAuth callback binds127.0.0.1 ephemeral port, exact Host/path/GET/one-time state/recognized unique query fields,5minute TTL and8192-byte URL. Library calls force15seconds/64KiB/no retries/redirects and disable default logging interceptors through the supported option. No live Google consent/client creation, Drive object listing/upload/delete, backup group choice, tablet credential transfer, SSH/service/firmware/account pairing or release/tag/merge operation occurred.

## Executed checks and attribution
Local supported Node24.21/Python3.12:
-10actual maintained-client/owned HTTP protocol controls PASS, with actual Linux private-file custody. Positives cover PKCE exchange/granted scope+audience/about, cached restart and actual refresh; refusals cover wrong/duplicate-state/path, denial, scope/audience, changed account, late response after cancel/disconnect, failed/confirmed revoke, stale opaque confirmation, oversized/redirected response, TTL and insecure path/CAS. All tokens/client identities are explicit synthetic fixtures, not real credentials.
-The same10protocol controls separately PASS with the actual esbuild-bundled host runtime. No source-bundle equivalence is merely inferred from import success.
-Three shared controller +one actual helper HTTP boundary controls PASS: no token-bearing status/arbitrary or verifier-bearing/duplicate-parameter consent link, stale UI suppression, exact opaque confirmation and origin/cookie/canonical action/body/size refusal.
-Six Python custody controls:5PASS/1actualWindowsACLskip on Linux. Actual owner-only save/replace/disconnect, corruption/CAS preservation, JSON duplicate/size/extra action, POSIX link/hardlink/mode and child failure secrecy are separate from OAuth protocol. Windows protocol tests use explicit memory custody; actual NTFS custody tests must run in hosted Windows, no Linux pass substitutes.
-Full Manager checkPASS:97Node controls (83inherited+14new), lint, dev/prod build and actual browserDPR1/1.25/Electron checks. Production UI165.84KiB at precommit dirty identity. Final exact app tree then rebuilt, native Linux package and separate new shared browser/Electron/packaged auth UI matrices PASS. Their status/IPC responses are explicit synthetic fixtures; they prove sandbox/preload/shared rendering, cached/pending/cancel/connected/revocation confirmation/failure/local disconnect/malformed secrecy and390/1280 layout, not live Google or native storage. Before substitution, packaged/unpackaged modules execute real protected-helper missing-config refusal and invalid-revocation-argument rejection. Captures use fixture@example.invalid only; inspected visually.
-Dependency npm audit0known findings; no audit override or waived gate. Initial dependency install used systemNode18 and emitted engine warnings; the supported Node24.21 install/lock generation/checks supersede it. Final lock preserves unrelated packages; only maintained dependency graph added. Packaging initially refused missing LICENSE names: data-uri-to-buffer4.0.1 includes its full MIT grant in README, preserved unchanged; bignumber carries LICENCE.md, also preserved. No grant was invented or source relicensed. Host dependencies are bundled only in Node runtime, not renderer; matching notices + dependency inventory included. Project version placeholders are inherited REM46 debt, unchanged; no new project versions minted/maintained.

Hosted exact Linux/Windows/Docs CI and independent review remain pending at first publication; final receipts will be added in comments. Source-policy/private-token/caller/custody review is required before canonical sync/archive. WholeREM42/liveGoogle/domain/backups/native/physical/full-parent/deployment/release gates stay open. Actual selected native page observations and Main panic work were not repeated or touched.

## Original local evidence and limits
Raw routine logs and temporary credentials are not duplicated into durable storage. Source/tests/public guide and sanitized screenshots/receipts are canonical artifacts. Earlier initial Electron renderer fixture returned disconnected while poll expected connecting; the explicit fixture state was corrected, product source not weakened. An early aggregate publication snapshot exceeded the output bound; per-file bounded chunks then produced a GitHub tree exactly equal to the local verified tree before adopting API commit metadata. No truncated artifact was published.

Primary implementation references: [Google installed-app OAuth](https://developers.google.com/identity/protocols/oauth2/native-app), [Drive about.get](https://developers.google.com/workspace/drive/api/reference/rest/v3/about/get), [official OAuth client](https://github.com/googleapis/google-auth-library-nodejs), actual pinned installed source and lock. These support provider protocol selection, not an assertion of live qualification.

Source basis: current task/issue/contracts, primary provider/tool sources and actual owned protocol/filesystem/shared UI executions, explicitly separated from synthetic renderer responses and unfinished native/provider gates.

## Owner requirement and scenario verification
Compared all three requirements and six scenarios in the named delta against the current implementation and tests:

| Requirement/scenarios | Implementation | Executed evidence and limit |
| --- | --- | --- |
| Explicit maintained authorization; independent sign-in and wrong/stale/failed consent | `host/drive-auth.mjs`: begin/callback/exchange/account, maintained OAuth2Client, token-info audience/scope/expiry and Drive permission identity | Ten owned HTTP controls use the actual maintained client and synthetic provider responses; actual Linux private-file commit is exercised. Shared UI works with no tablet. Live Google consent remains unqualified. |
| Bounded host custody and narrow actions; successful operation and unauthorized caller/insecure path | `host/drive-store.mjs`, `host/drive_store.py`, helper fixed-action endpoint, Electron main-frame handlers and strict public protocol | Separate actual custody, helper HTTP, controller and sandbox/IPC controls; no secret-bearing renderer state accepted. Actual Windows NTFS controls are separate hosted checks, not implied by Linux or synthetic UI. |
| Truthful cancellation/lifecycle; late response and restart/revocation | generation/abort guards, final synchronous guarded persistence, cached restart, opaque digest-bound confirmation and separate disconnect/revoke | Deferred HTTP response, refresh/account replacement, stale CAS/confirmation and failed/confirmed revoke cases; cancellation after commit is not an implicit revoke. Backup/domain/tablet operations stay outside scope. |

This is the implementation owner's verification, not independent acceptance. Existing Root/Main independent review is requested in [PR15 comment6149417857](https://github.com/s116821/ReMarkableBuddiesManager/pull/15#issuecomment-6149417857). Canonical sync/archive still waits completed checks and that review.

## Preserved CI failures and test-only repairs
Initial source06b hosted run38422038442 failed an inherited wired-host exact surface assertion that omitted the new narrow auth capability. Source280a879413a39a22eb96b69905e3484662edd32a fixes only that assertion and adds exact auth methods/argument refusal; corrected unpackaged and packaged wired checks passed locally. Hosted run38422916232 then passed unpackaged Drive UI checks on both systems but both packaged Electron screenshot captures timed out after fonts loaded. Source2e95c212f62b3284b460022dc2da8333b4a6854e explicitly shows the test native Electron window that MANAGER_TEST otherwise creates hidden; packaged browser/Electron checks pass locally. This explains the repair hypothesis, not proof of the hosted cause. Production auth/custody code is unchanged by either successor. Current hosted run38424474360 is pending; earlier failures remain failures. Docs source0904b9c5a2b72af2423760ba20ede6c5695c3ddd CI38422352215 passed.

Source2e95 CI38424474360 then exposed an immediate unpackaged test startup race on Linux: show() was called before a BrowserWindow existed. The visibility hypothesis is not an accepted repair. Current sourcedfd5fc217a7bace9ee0f70c74d016ce3684ed0e7 waits for firstWindow as before and uses the existing repository Electron native capturePage stayHidden/stayAwake path instead of Chromium full-page capture; empty captures refuse. Browser remains full-page; native Electron evidence is the actual viewport, not a claimed full-page image. Both updated local unpackaged and packaged UI executions and lint pass. Production source is unchanged. Current hosted successor checks are required.

## Completed exact hosted checks
Manager sourcedfd5fc217a7bace9ee0f70c74d016ce3684ed0e7, normal CI [38425178494](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38425178494): Release policy, Linux Foundation job115392642904 and Windows Foundation job115392643109 all SUCCESS. Completed logs were inspected separately. Linux real custody5PASS/1Windows-native skip; Windows real custody5PASS/1POSIX skip, including actual broad NTFS grant refusal and atomic save/replace/disconnect/CAS controls. Both logs confirm unpackaged and packaged shared Drive browser/Electron checks; images/status remain synthetic UI evidence, not live Google. Windows completed log contains no GitHub error markers, Python FAILED summaries, Node not-ok entries or traceback/assertion/timeout/error markers, including its inherited multi-command PowerShell checks. This is current log evidence, not a general claim that those inherited steps can never mask failure. Docs cc9efaaa9f4a2a3bc26a5aadf6a06b106f6e45be CI38425387623 SUCCESS; owner27strict/12portable/20guidance126preserved checks PASS. Final result/task-only successor still requires its own Docs CI.

No available bug-bot or independent review submission was present in fresh PR15 timeline at this receipt. Root has assigned the existing Sol review lane; independent acceptance remains an external gate for canonical sync/archive. The capability stays active and PRs draft pending that review. Next Manager personalization editor readiness was refreshed against full REM53/comments and current actual config: no prompt field or verified write/reload command exists in the inspected scoped backend; unknown fields refuse. [REM53 comment4a73ca2b](https://linear.app/magentumdragon/issue/REM-53) asks Main for this narrow contract without gating a simple preference on all consumer work. No stub saved UI or second backend writer is introduced.

## Independent acceptance and bounded lifecycle closeout
Root's current coordination message reports the existing Sol reviewer independently accepted the new OAuth source/spec delta without actionable findings at Manager dfd5fc217a7bace9ee0f70c74d016ce3684ed0e7 / Docs contract cc9efaaa9f4a2a3bc26a5aadf6a06b106f6e45be. It inspected actual integrity-checked maintained dependencies, protocol/custody/cancellation/revocation source and completed Linux/Docs CI logs; it did not execute tests or a real account. Windows auth/package checks were pending when reviewed; the owner subsequently inspected the completed fully successful Windows115392643109 log above. Review execution is not relabeled as test execution. Root is publishing the scoped public review; the permanent receipt will be linked/read back separately when available. Result/task-only Docs2cc4c6b2485fc6ad4e6e25581ed8389a67653b65 CI38426724189 SUCCESS.

Only the completed manager-drive-auth capability is synchronized: canonical three requirements/six scenarios preserve the reviewed delta bytes, with no delta markers/duplicate requirement headings. Only its five own files move to changes/archive/2026-10-13-manager-drive-auth; results/tasks record closure and other proposal/design/delta bytes remain unchanged. Other lane changes stay active. This archive and ready implementation PR15 remain one paired delivery with parent-first integration/reconciliation/review/merge requirements; no merge/tag/release or whole REM42 completion is asserted.

Real Google consent, deployment desktop-client provisioning and same-app/account backup-namespace qualification remain unperformed. No domain backup browsing/restore, credentials/tablet installation, physical/native capability or parent consolidation follows. REM53 readiness remains the exact Main-owned optional field/save-readback/reload contract, requested in comment4a73ca2b; generic consumer completion is not substituted as its dependency. The scoped software capability can close without falsifying these explicit external gates.

## Permanent review and final archive receipt
Fully read canonical [review5506455745](https://github.com/s116821/ReMarkableBuddiesManager/pull/15#pullrequestreview-5506455745): accepts the bounded software capability at Managerdfd5 / contractcc9ef; results/tasks successor2cc4 accurately records completed checks. Root independently inspected final Windows steps/log: native NTFS5PASS/1POSIXskip,97Node tests with zero failures, browser/Electron/packaged authentication checks complete with explicit synthetic auth responses. The independent Sol reviewer did source/spec/dependency/existing-evidence review, not new tests or live sign-in; Root's Windows log check is separately attributed. Current review/inline threads contain no bot findings. Full review limitations and prohibition on cumulative merge through unfinished parents are retained.

Closeout Docs3ab79fdb9b9459b81cce5a0f95673d4250b4a5fc CI38427069757 SUCCESS. Own archived proposal/design/delta are byte-identical to pre-closeout2cc4; canonical three unique requirements/six scenarios exactly match reviewed delta without delta markers. Only this accepted capability is closed. This permanent-receipt-only update changes no spec, task, implementation, test or eligibility; its ordinary Docs checks remain required.

## Current source integration preparation

The existing source branch inherits offline-host preparation `b73ed9ad` and actual
bundle main `1a1ffa0`. Relative to previous head `c5bf0bc`, only the three inherited
quiet-refresh doc/runtime/test paths change. Authentication runtime, protocol,
custody, renderer/IPC and synthetic test bodies remain exact to accepted `dfd5fc21`.
Existing producer compatibility is inherited from #13 and remains separately
attributed; original authentication review 5506455745 is not a cumulative audit.
The two parallel CI conflicts retain the previous exact CI/pipeline bodies,
including common Drive guards, retained source/package host checks and selected
Windows NTFS refusal. Ancestry conflicts retain accepted shared software; no new
authentication or producer behavior is introduced.

Docs incorporates actual main `e73f0c2`, keeping the shared guide exact. Only this
receipt is extended. Original proposal/design/delta/tasks, canonical three
requirements/six scenarios and the five-artifact own archive remain unchanged.
Historical personalization-readiness statements above are earlier checkpoints;
REM-53 owns its current contract/status, which is not revalidated by this auth pass.
All delivered-main records and unfinished work remain preserved.

No live Google consent, account query, refresh, revocation or other provider call
is performed by this preparation. Existing UI fixtures synthesize authorization
and account responses and abort unknown external traffic; their observations do
not become live-provider evidence. Local preparation uses lint/static preservation
and Docs checks rather than rerunning provider protocol/UI tests. Normal current
CI, bounded successor review, actual offline-observer parent delivery and final
reconciliation remain required before coordinated source/Docs delivery.
Production client provisioning, backup namespace/domain/restore and physical
qualification stay unperformed and separate. No tablet, settings, new resource
or reverse-engineering action occurs.


## Final actual-parent reconciliation

The offline observer parent delivered normally as Manager main
7c3589e77ba02d665134f96ac096de59fd766f2e and Docs main
1ca5d722d7353578452e4606be0fc3d48defbf86 after final accepted reviews
5580938132/5580938630 and all current source/Docs checks passed. Actual-main
pipelines are observed separately; no new release is inferred from that test
merge. Auth source now includes the actual parent, with its complete accepted
preparation tree56794fc1854b01f3021f422ad19f2e23f196e2aa unchanged. The sole CI
conflict preserves the accepted existing common Drive test command.

Docs incorporates actual main1ca5d72, keeping both conflicting signed-observer
archive receipt/tasks files exact to authoritative main. Only25 stale active
parent copies are removed; their completed main archives and canonical specs
remain exact. The own five-file auth archive and canonical three requirements/
six scenarios stay unchanged except this result receipt. Final current-head
CI and independent review remain delivery gates.

Preparation reviews5580913339/5580913969 and original auth reviews retain their
scopes. No local OAuth/provider/credential operation or original synthetic
protocol/UI matrix was repeated. Live Google consent/client provisioning,
backup namespace/domain operations, restore and physical qualification remain
unperformed. No tablet contact, production account or settings change occurred.
Source basis: actual GitHub merge/check/review metadata and complete Git tree
and own archive/canonical preservation checks.
