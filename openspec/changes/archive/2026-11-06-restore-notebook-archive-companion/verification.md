# Consumer verification

[Manager PR61](https://github.com/s116821/ReMarkableBuddiesManager/pull/61), source
`cb28da032ee8501622b04f20a95d734e713136d6`, pairs with
[Docs PR140](https://github.com/s116821/ReMarkableBuddiesDocs/pull/140).
The precode and its notebook complete-media refinement were independently
accepted before implementation. Independent final review accepted production
source `113072a` and the actual retained logs/captures. Successor `cb28da0` changes only
the existing wired-host test's expected capability list; runtime code is unchanged.
Hosted run42140319278 at this exact source passes Checks, Build and both Linux
and Windows Integration, with release correctly skipped for the pull request.

## Local results

- Node24.21.0: full Node suite997pass/1existing skip,998total, using two concurrent
  test files. New notebook controls cover explicit family/version/selector/path
  domains, mandatory complete media, exact original packet retention, uncertain
  Apply history, cross-family reference refusal, shared ownership, expiry,
  disposal and queued controller cancellation. Existing legacy vectors remain.
- Existing CPython3.12.14/Paramiko5.0.0: restore transport5pass/1POSIX-only skip.
  Fixed command/stdin controls cover all six selectors, paired versions and
  notebook complete media. No actual Windows USB/SSH or tablet run is claimed.
- Actual development browser/local-helper and Electron main/preload/UI pass the
  new lane's40Busy directions and37preview invalidations against20existing peers,
  alongside the existing notebook archive matrix. Actual shared UI verifies
  keyboard preview, immediate private-field clearing, one deliberate Apply,
  preserved uncertain history after Status, lifecycle clearing and peer guards.
  Narrow390px and wide1280px captures were produced; browser390 and native
  Electron1280 were visually inspected without clipping or exposed private paths.
- ESLint passes for changed runtime/UI/test scope. Production build649.12kB
  passes the unchanged650kB limit; the existing400kB warning remains. Repeated
  equivalent guards were consolidated rather than raising the budget. Development
  build also passes. No dependencies, lockfile, workflow or budget were changed.

The first broad local test attempt failed with the Windows Python alias/missing
dependencies and heavily concurrent child timing. The retained second run uses
the already-present CPython/dependency directory and two-file concurrency; no
test assertion or timeout was weakened. The initial new cross-family assertion
was corrected to expect the existing honest `not-dispatched` refusal with zero
I/O. Earlier production builds exceeded the unchanged limit by671/265bytes;
guard reuse resolved the actual excess. A missing browser-global ESLint entry
for the new host-check fixture was added to the existing scoped list.

The first hosted run42139049125 failed on both platforms because the existing
tests/wired-hosts.mjs capability assertion omitted the new notebookRestore key.
The exact one-line expectation was corrected without changing the preload or
weakening the assertion. Actual local wired browser/Electron verification and
scoped lint pass. Both original failed job logs remain retained.
Current composed-head qualification is the successful run42140319278.

The synthetic reports follow Buddy e664c2e's public notebook contract; they are
not captured producer or tablet execution. Canonical notebook-restore-companion
requirements are synchronized, preserving legacy behavior. This finite consumer
is archived in the coordinated Manager61/Docs140 delivery; final archive-only
Docs checks precede that pair's merge. Root owns Manager-first, Docs-second
integration and actual main/build/release verification in the current task record.
No merge or release outcome is claimed before it occurs. Broader
notebook/native/REM42/52/35 work does not close merely because this consumer is delivered.
