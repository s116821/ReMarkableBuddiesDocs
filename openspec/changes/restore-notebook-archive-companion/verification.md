# Consumer verification

[Manager PR61](https://github.com/s116821/ReMarkableBuddiesManager/pull/61), source
`113072ab693d493f7e2356b5494c86fc41cbe40e`, pairs with
[Docs PR140](https://github.com/s116821/ReMarkableBuddiesDocs/pull/140).
The precode and its notebook complete-media refinement were independently
accepted before implementation. Final source review and hosted CI are pending.

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

The synthetic reports follow Buddy e664c2e's public notebook contract; they are
not captured producer or tablet execution. Hosted Linux/Windows package checks,
independent review, canonical sync/archive and actual release followthrough
remain separate until recorded below. Broader notebook/native/REM42/52/35 work
does not close merely because this consumer is delivered.
