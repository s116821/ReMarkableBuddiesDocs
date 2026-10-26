# Independent review repairs

This is an incremental response to the independent review of Manager1e0e8c2502b845e6508da93d98c81a3977260eee / Docs038908edbb3eaa8f65d26d97041e126866347dcb, not final acceptance, canonical sync/archive or delivery.

Manager repair commit `5299a742d74c2821019ceacbf8ce64d4aaca3ad9`, tree `281ff3317ea54b59d2d3ab6fb78d8c240773493f`, sole parent1e0e8c2 changes only `src/model-credential.ts`, `tests/model-credential-controller.test.mjs` and `tests/wired-hosts.mjs`. Earlier source, failure histories and precode acceptance remain intact. Continue the existing linked Manager40 / Docs109 pair.

## Findings and repairs

Root reported source run40333360931 Checks/Build/Title passing and Linux Integration job121610069550 failing specifically at the real wired exposed-capability assertion, tests/wired-hosts.mjs:82. The exact expected list omitted the admitted modelCredential capability. This was independently reproduced locally before repair. It was not a pip failure. The assertion now admits exactly that one additional capability, preserves the full existing allowlist and all existing guards, and adds explicit new-capability wrong-arity and caller-path rejection controls. Current source and packaged wired controls passed.

Root also reproduced a real unbounded client wait: Stop directly awaited a cancel IPC response. At14001ms a never-resolving cancel left Busy true although private entry was cleared. Two added real-controller/fake-clock tests failed before the code repair and both pass afterward. Stop now bounds its own cancel wait to14000ms with timer cleanup. It sends one targeted cancel, performs no retry or global cancel, retains conservative original uncertainty after timeout and releases Busy. Existing generation/reference/original checks remain. A valid cancel completion arriving after timeout and a newer ready editor cannot change safe state/reference or clear that newer raw entry. Private text and actual-input hooks clear synchronously before waiting.

## Scoped observed qualification

- All26 focused model-credential controller/core/helper/child tests pass, including the two new regression controls; controller-only7 pass. Original failing Stop logs are preserved.
- Lint and TypeScript no-emit compilation pass.
- The real wired source and packaged helper/browser/Electron controls pass with the exact exposed surface and added guards. Their fixtures are explicitly synthetic. These narrow surface controls use the existing clean1e0e8c2 production/package artifacts; the host/preload exposed surface is unchanged by this repair. They do not claim the rebuilt renderer's Stop behavior was exercised end to end on5299a74. The actual current TypeScript controller is exercised by the Node24 tests, and current hosted compilation/integration remains required.
- No dependency installation, authentication retry, broad rebuild, tablet/provider/native/SDK/RE operation, global cancel or automatic mutation retry was performed. Root's missing google-auth-library in its own helper checkout is an environment limitation, not a product finding; no local dependency change follows from it.

Native incremental bundles must use exact prerequisites1e0e8c2 (Manager) and038908e (Docs), with native modes/blobs, source manifests and separate RED/GREEN logs. Root remains publisher/reviewer and continues independent review and current hosted checks. All outstanding qualification/final lifecycle gates in tasks.md and verification.md remain outstanding; this repair does not close them.

Source basis: Root's exact CI/controller review receipt, current native repair diff and local RED/GREEN command output. Windows/current hosted outcomes are owned by Root and are not inferred here.
