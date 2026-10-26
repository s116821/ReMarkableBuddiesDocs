# Resident caller progress integration

Buddy `c3ba9c11773bd82277c48b0149d1587be8665371` pins SDK
`df4383e0af4bccd2e4e1a6b14615e8f281dc5cb3` in both dependency declarations and
the lockfile. ResidentConnection forwards caller progress through handshake,
observation, both effects and both reconciliation forms. The existing Store
reserve/finish path remains shared. No new journal or native capability is added.

ResidentRuntime continues its installed admission callback through socket
appearance and handshake under the original startup deadline. It rechecks copied
files and the child after callbacks, and retains the normal owned-child cleanup
path on cancellation. The real child fixture distinguishes cancellation before
socket creation from cancellation after receiving Hello. Store/socket regression
cases cover insertion and selection cancellation before and after dispatch,
original wire identity across reopen, explicit no-dispatch proof and uncertain
reservation refusal.

Independent review accepted source and these controls. Further lifecycle review
identified that the endpoint retires an idle connection after 30 seconds, while
the runtime currently retains one connection. An unused new Session observation
wrapper that treated all request failures as fatal was removed before publication.
The next product route must distinguish ordinary cancellation/timeout/idle EOF
from session integrity failure and reconnect to the same verified resident
process with fresh identities. The current Session connection helper is not yet
that product route. Normal request retirement must not restart xochitl.

The preliminary `buddy-progress-r1.log` passed 96 resident tests, then its lint
phase was deliberately stopped with exit 137 to remove that wrapper. This is
intermediate-source evidence only. Final-source `buddy-progress-r2.log` passed
all 96 resident cases (37.22 seconds), then exited 101 during the binary test
compilation with an LLVM output-stream I/O error. The host C: drive was full;
binary tests and local lint did not complete. Preserve this failed log rather
than crediting the earlier revision or relabeling the run successful.

Hosted Buddy run `40253971614` at `c3ba9c1` passed formatting and strict
all-target/all-feature Clippy; its all-feature tests remain in progress.
SDK run `40253152513` at `df4383e` passed Linux and Windows staging checks;
the build stage remains in progress. These are scoped results, not completed
pipeline or installed/native acceptance claims.

SDK stable all-feature tests/lint, explicit Rust 1.88.0 checks, exact package
containment and rebuilt Qt interoperability passed as recorded in SDK PR31's
[evidence comment](https://github.com/s116821/ReMarkableOpenSDK/pull/31#issuecomment-6406089072).
The prior Buddy activation revision `8c10f63` separately passed its full local
chain and hosted run `40251260065`; that does not validate this newer consumer.

Source basis: current source, independent review, actual owned socket/child and
Store output, and hosted checks. First-gesture admission, actual installed/native
qualification and full Reader/Writer acceptance remain unfinished.
