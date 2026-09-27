# Host controls and Qt lifecycle checkpoint

September 26, 2026. Independent review checkpoint only. This does not implement the deployable probe or qualify native creation.

The isolated local research repository `work/rem25-probe-host` is at `73ae4966d1b139a24bd7c0ad4167e3993b5f114e`. Its BUILD-EVIDENCE.md records exact source/build commands, test results, package/license provenance, artifact hashes and remaining work. It contains original host harness source only, with no proprietary firmware, production project dependency or tablet artifact. The coordinator and reviewer have shared local access; no feature PR has been opened.

The available GCC9 Linux image had no Qt development files. Authorized host-only acquisition produced an isolated Ubuntu/Qt6.4.2 x86_64 image `sha256:7d49afd1385159295111480f49f69ee41f87c458ec746e7be583371447d236d0` from official base `ubuntu@sha256:008173c23f95b170204355c12626cb5a965d779a7e1283b09e9cffbb1bf33ca3`. Official apt indexes/package hashes were verified by apt without unauthenticated overrides. Full selected package versions and installed Qt binary hashes are retained locally; Qt package copyright files were inspected. The final image identifies the tested environment; the floating apt recipe alone is not reproducible. No compatible ARM Qt sysroot is established.

Passed host cases:

- Atomic single-attempt concurrency; object/depth/time/string/output bounds; no malformed partial entry append.
- Real Unix datagram credentials and PID/UID/nonce rejection, full queue returning without blocking, unsafe socket mode, symlink/missing endpoint, expiry and oversized output.
- GCC9 AddressSanitizer and UndefinedBehaviorSanitizer controls run.
- Real Qt startup and deferred callback, normal/delayed/no event loop, expired/injected fingerprint refusal, destroyed context, foreign-thread metadata refusal, zero getter/native-method invocation and 512-object truncation.
- A separate dlopen-before-application shared-library fixture registers and runs one deferred callback, then stays inert across application recreation. This is host Qt behavior, not XOVI qualification.

The Qt harness needed explicit position-independent compilation; the initial default build saw no application instance/objects, while -fPIC and the shared-library fixture passed. Constructor/bootstrap code does not hash the executable, discover dependencies, perform filesystem IO or scan metadata. Its fixed state/scheduling still uses Qt internals and is not a hard realtime guarantee. Cooperative budgets cannot interrupt a stalled Qt call.

The checkpoint deliberately has no deployed protocol, real native fingerprint proof, full bounded JSON/method-signature serialization, native allowlist/window/engine resolver, XOVI package or ARM artifact. QMetaMethod::nameView requires Qt >=6.9; host Qt6.4.2 does not exercise it and no allocating fallback was added. The one-shot transport remains a prototype with trusted-runtime-directory assumptions and requires production collector/credential review. The actual target import manifest is not stable, so no new tablet provider export is requested from the host-only fixture manifest.

Next review should evaluate source controls and bootstrap evidence, then define the minimal actual probe and target sysroot/import requirements. Device activation/transfer/SSH, exact provider ABI and minimal verified rollback remain coordinator-owned separate gates. No native feasibility check is marked passed.

## Loader-acceptance lifetime follow-up

The original host checkpoint was independently accepted within its labeled synthetic scope. Follow-up local source `c67b097abbd68787ba2124bc04897a5f117603ae` adds accepted-loader registration tests. XOVI's tagged source can unload a failed-condition extension after static constructors; deployable registration now belongs only in accepted _xovi_construct, with late-load refusal. The new host model passes accepted single-lifetime, shouldLoad refusal without registration, failed-condition unload before registration, and late-load refusal. Full original controls/lifecycle tests still pass. No native XOVI execution follows from the synthetic ordering model. See loader-probe-design.md for the tagged-source unload audit and limitations.

## Usage checkpoint

Research source is preserved at local commit9f822a7ab03148436e41a36c3d576ad36ee61b32, including RESTART.md and exact SDK acquisition script/container recipe sources. The independent review accepted host lifecycle code at c67b097 within synthetic scope; subsequent changes are acquisition/restart documentation and preserved sources. At87% shared usage no new builds/experiments are being started. The direct official SDK download remains unfinished in local resumable chunks; no full checksum, installation, ARM build or tablet provider comparison has occurred. Main coordinates the90% stop and any owned download is to be stopped then with partial files retained. Consult the local final-stop note before resume; this snapshot is not a completion claim.

## Final pre-limit stop state

The SDK download subsequently completed:424978767 bytes, SHA256 e2daf17a86d375aae6d290af993060f3dfb488568ca83c401eaa47869e975179 matched both assembly and independent Windows hashing. The failed first run retained49 complete chunks; one bounded resume fetched the remaining two. No owned downloader or SDK Docker pull remains running. SDK installation, ARM compilation and provider comparison were not started. Local source checkpoint is b004edd729aa08969b3730062b3988d365890831 with FINAL-STOP.md overriding historical in-progress notes and exact resume instructions; all caches are preserved. Worker stopped research at88% usage under the pre-90% checkpoint direction. No native qualification or completion claim follows.
