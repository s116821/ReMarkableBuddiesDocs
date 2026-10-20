# Manager owned-data inspection integration

The bounded REM-42 Manager increment consumes Main's reviewed Rust report_version1
at source6b1b9fd539c33ced6ab56541ef332ba05e4ed693 /Docs4b425c9559fed5446a730d56bc9e68b6b8e80bb4.
The backend is now source-delivered by [Buddy #32](https://github.com/s116821/ReMarkableBuddies/pull/32)
at `42b5108653563f2437ab793921c298e50bc268dd` and [Docs #14](https://github.com/s116821/ReMarkableBuddiesDocs/pull/14)
at `24066fba710534fc797b0e6e142bb7cb43f940b2`. This does not claim tablet deployment.
Main retains Rust/CLI ownership. The archived [Manager change](../openspec/changes/archive/2026-10-19-manager-owned-data-inspection)
owns only shared Angular UI, report parsing and existing host adapter integration.

See the [Manager public guide](https://github.com/s116821/ReMarkableBuddiesManager/blob/feat/rem-42-owned-data-inspection/docs/owned-data-inspection.md)
for fixed CLI/configuration, manual setup, interpretations and checks. Browser and
Electron use the same UI and schema parser. Host commands are parameterless and
wired; no Buddy service API, native document read, credential environment sourcing,
cleanup/restore or provider interaction follows. Linux is the existing native
adapter's supported host; Windows/macOS refuse honestly until separately qualified.

Absent, missing, omitted and uninspected category/reference evidence remains
visible. Apparent bytes are per path, domain reference totals are nonadditive,
complete totals require complete inventory and no reclaimable/current-native claim
is made. Actual command/schema support, not equal application SemVer or a fabricated
minimum release, establishes report compatibility. Git tags remain version authority.

The user-facing category consequences describe why records/cache/history are
separate. Unknown account/native/install compatibility stays unknown. Disconnect,
re-read and changed connection/boot invalidate results; inspection pauses automatic
observations until explicit re-read. Busy reports never stop a service.

This does not close whole REM-42 or its REM-37/41/52/53 dependencies. The bounded
product/spec and CI-successor reviews passed; the three accepted
requirements and six scenarios are [canonical](../openspec/specs/manager-owned-data-inspection/spec.md).
Current-main checks/final review and coordinated backend/Manager/Docs delivery remain
merge gates. Fixture browser/Electron/SSH evidence is distinct from live tablet/provider proof.
