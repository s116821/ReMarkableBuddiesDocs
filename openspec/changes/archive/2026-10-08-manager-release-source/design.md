# Design

## Decisions
Use GitHub's canonical ReMarkableBuddies `/releases/latest` public REST endpoint,
with no credentials, 15-second cancellation and five-minute polling while open.
Reject drafts, prereleases, non-stable semantic tags and malformed/cross-repository
URLs. Read uploaded/nonempty asset metadata; this does not verify bytes or signatures.
Show candidate separately from qualified availability. No connected device profile,
signed APK verification, exact source/SDK contract or package ownership proof exists
yet, so eligibility always refuses and no install action is callable.

Use one shared TypeScript controller and Angular view. Local storage is app policy,
not device state or package origin. Default official; do not erase a valid previously
saved community preference when its source is unavailable. Community selection is
disabled until actual listing. Storage failure is visible; no claimed persistence.
Never compare equal SemVer as package equivalence or infer an installed version.

Allow only GitHub API in renderer connect CSP. Electron remains sandboxed with no
new preload capabilities. Refresh does not communicate with Buddy/tablet. One
in-flight request, cancellation on destruction and stale status after faults avoid
late request replacement or claiming old metadata is current. No release engine.

Tailwind uses upstream Angular PostCSS integration, pinned dependencies and shared
theme/focus tokens. Both distributions use identical templates/styles.

## Prior Art and Boundaries
reManager separates installed package versions from refreshed catalog compatibility
(app_packages.go); reuse the distinction rather than treating metadata as installation.
Vellum documents signed local APK installation independent of public listing.
These are references, not implemented Manager installation or hardware evidence.
https://github.com/rmitchellscott/reManager/blob/main/app_packages.go
https://github.com/vellum-dev/vellum-cli
https://docs.github.com/en/rest/releases/releases#get-the-latest-release
https://tailwindcss.com/docs/installation/framework-guides/angular

Actual Vellum signed APK/target SDK manifest verification, device identity, wired
helper, package lifecycle/source equivalence and catalog feed remain separate
REM-41 gates. REM-46 pipeline qualification is unchanged; no new schema producer.

GitHub unauthenticated public requests share a 60/hour IP budget. Both automatic and manual refresh honor Retry-After and X-RateLimit-Reset; missing headers use a conservative five-minute delay. See https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api .
