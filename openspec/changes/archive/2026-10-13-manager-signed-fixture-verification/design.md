# Context
Root authorized original fixture consumption. Main helper4e79104 / Docsfdb33b7 produced historical v0.2.0/ff8ad75, legacy-no-sdk/not-qualified. Artifact hashes and the generation DER-SPKI pin were supplied independently of the adjacent key. Transport ZIP is a delivery container only, not Manager PR13 evidence.

# Goals / Non-Goals
Observe actual originals and focused refusals offline with the already qualified ee31d275 source-build verifier. Never regenerate a signer/index, extract or run APK payload, enroll a key, mutate package databases, invoke Vellum wrapper or infer production eligibility.

# Decisions
1. Consume six regular public files from an exact checked directory. Bound/hash all files, strict duplicate-free JSON, and require an independently supplied manifest SHA256 and DER-SPKI SHA256. Manifest is correspondence evidence, not its own trust anchor.
2. Reuse qualified source/archive/binary receipt validation. Require immutable local Linux image, nonroot effective-owner binding, no network, read-only mounts/root, no capabilities or privilege escalation, bounded tmpfs/process/time/output, isolated explicit metadata/payload/key/config roots. Mount no host trust directories.
3. Only `verify` and `adbdump --format json` apk applets. OpenSSL reads a public PEM into DER in tmpfs; no private signing tools or APK payload execution. Every observation brackets original/isolated roots with content/mode/link snapshots. Positive verification must exit0 with no stderr. Negative single-file verify must exit1 with recognized signature/integrity diagnosis; timeout/crash/usage are failures.
4. Compare package standard metadata and signed vendor tags with both authenticated index entries, source identity, full pkgrel, byte sizes, and receipt inventory. Read signed path/file digest metadata without extracting files. Report signed-index metadata hashes separately from complete-file SHA256. Do not invent an index hash algorithm or claim independent index regeneration; saved producer readback remains separately attributed.
5. Negative controls use copies and existing public material: wrong separately supplied pin; wrong explicit key set using a separately existing public key or deterministic public-only mutation; changed signed package/index metadata and package payload bytes. Originals stay unchanged. No new signer or replacement package generation.
6. Report host-only test-fixture eligibility=false, independently executed observations vs owner-reported compilation. Compiler/native/SDK/lifecycle/source-switching/reproducibility and signature-valid malformed cases stay open.

# Risks / Trade-offs
Pinned external code/image and developer build receipt are trusted execution inputs, not publisher attestation. Bounded capture/deadlines and container cleanup must fail closed. Metadata readback observes signed file digest claims, while verify checks actual payload integrity; it does not execute or independently rebuild binaries. Limits deliberately admit only this two-target legacy fixture contract.

# Delivery
Linked Docs and Manager PRs with exact heads, public original artifact/tool identities and focused evidence. Preserve accepted parents; independent review, parent-first merge, canonical sync and archive remain coordinated with Main/Root. No production action follows.
