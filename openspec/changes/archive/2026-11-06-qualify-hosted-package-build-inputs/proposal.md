# Hosted package build inputs

The accepted strict APK source producer cannot use the observed Windows bind
mount ownership and cannot substitute weaker normal release tarball metadata.
Expose its existing build/qualification phase separately from APK generation,
and orchestrate it through a manually gated maintained GitHub workflow on a
normally owned Linux workspace. This finite scope implements packaging task3.3's
build-input prerequisite, not production signing or complete packaging.

No dispatch is selected by source implementation or ordinary PR checks. Keep
real tag/SDK, ordinary Git/ownership/raw-byte, compiler/runtime and pre/post guards.
Return explicit frozen binaries/build metadata/private evidence plus a final
completion manifest. No alternate ownership mapping, safe-directory exception,
metadata fabrication, new build framework or automatic release trigger.
