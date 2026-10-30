# Implementation verification

The bounded producer is implemented at Buddy
669c0774530699500984dda038cc5138ed474c4e against the accepted concrete contract
Docscfd133ad6d1cd172b58d5c410a671a2337bab9f5. This verifies synthetic source/CLI
behavior; it does not claim shipment, installed runtime, provider, tablet or native
source freshness. Actual delivery/publication receipts follow separately.

## Current Linux evidence
Run39902717766 Checks120247726452 passed fmt, strict all-target/all-feature Clippy,
422 library tests (1 existing ignored),6binary tests,4CLI groups, retained suites
and maintained checks/audits. All15 new library tests, including the five added
coverage groups, executed. Current run39902717766 completed Title/Checks/Build/Integration PASS; PR Release
was correctly skipped. This is the exact current669 candidate pipeline.

Actual clean checkout68aba6bfc5e955644173c59d1aeed8529bc7dc9f was fetched; its
50531b8de160e31984260fe8741baf5db64290cc tree equals reviewed669 exactly.
Executable SHA256552e546b4b14cce41e2535eeb60020230f717a215fa650d14c61b889273c92a9.
Original log628964 bytes SHA256
1e2ea1a9444f7337c9934bbd2d14f28881b159422221e4390a8f19f48782d5f7.
All47 CLI records/94 raw stream hashes and the one prepared-intent digest were
independently verified. Normalized46256 bytes SHA256
9153378bcbbcf8e37281f78e6a85cbbd33074bcfb901360921ef38ba17b555aa.
linux-coverage-corpus.json retains this exact current capture.

## Current Windows boundary
Fresh frozen669 fmt/strict Clippy/6binary/4unit/2CLI passed. Source669 has tree
50531b8de160e31984260fe8741baf5db64290cc; executable SHA256
bd079eb86d505cd3b169995578404d5a22d0cfd4a2a16400cc15199647474668.
All20 child records/40 raw hashes were verified: unsupported before reading held
stdin or Config. Original log11111 bytes SHA256
7ed85a7c595ebeeadb0e801c042e38fbd16a9d4191b92a9be6c59b3bdfc38f5d;
normalized9702 bytes SHA256
ccf4624c02104fce35bfa9fad104a745204ed23f30fb872c7cbfe038cd554a18.
windows-coverage-corpus.json retains it. This is not local Windows cleanup or
directory-durability qualification; all four operations are unsupported there.

## Requirement and vector coverage

| Requirement/vector | Executed current evidence |
| --- | --- |
| strict independent wire/hash and literal selector | common frozen_contract_vectors/closed_objects/nonliteral_selector units; malformed_utf8_duplicates_shapes_ids_and_bounds_access_no_paths; actual refusal/EOF CLI groups |
| nonmutating bounded preview/header-only custody | exact_known_read_allowlist_excludes_all_other_payloads; dedicated_admission_does_not_need_durable_payload_directories; actual CLI poison-commit fixture |
| original actor/root/generation/namespace/config-path/file binding | changed_config_marker_generation_and_file_identity_refuse; actor_roots_generation_namespace_path_and_changed_valid_bytes_refuse |
| namespace/entry/header bounds and unsafe/schema shapes | unknown_staging_unsafe_and_bad_material_preserved; capacity_header_bound_object_shape_and_namespace_reparse_refuse |
| existing lease/named identity custody | namespace_or_store_writer_and_missing_lock_never_initialize; replacing_a_held_named_lock_refuses_before_observation |
| one-slot preservation/reconciliation and uncertainty | preview_apply_status_preserve_every_other_file_and_never_recover; post_unlink_uncertainty_is_never_rollback_or_retry; consuming_output_keeps_both_leases_through_partial_failure; real CLI prepare/status/apply/absence |
| preservation metadata | before/after bytes, modes and mtimes in nonmutating scenarios, excluding OS-managed access times |
| explicit platform capability | Windows unsupported_host_never_reads_stdin_or_config plus20 held-stdin child records; Linux current filesystem/CLI fixtures |

All four requirements/four scenarios map to executed synthetic controls. The read
allowlist permits only Config, the five known bounded headers and selected slot;
separate guards deny durable payload reads/enumeration. Missing/poisoned durable
payload directories do not become an implicit Store recovery prerequisite.

## Source/spec preservation and independent review
423 other source base entries are exact. Original lib.rs and retrieval/disk.rs
bodies are full byte-exact prefixes; prior main production behavior is unchanged
outside the new route/fields. The later main delta updates only the CLI test
inventory/defaults and conflict controls. The669 successor changes only cfg(test)
instrumentation/test bodies; all430 other d6 tree entries are identical.

The original seven digest vectors are byte-identical across accepted Docs and
source fixture:4835 bytes SHA256
7d0462d62e417fde0eac9533c39f3df976b64c5b1f8f96001538fad534e83031.
The canonical four requirements/scenarios reproduce the accepted delta body.
Existing Store/cache APIs, protected credentials, Reader and Writer remain unchanged.

Independent concrete precode5623842544 accepted cfd after resolving the Linux-sync
and bounded-header admission findings. Production static review5623992783 atd6
found no blocking issue; focused cfg(test) review5624059085 at669 also found none.
Their original log/vector/preservation checks retain their own attribution.
Final composed evidence/lifecycle review and normal current CI remain gates.

## Separately preserved captures and failures

| Artifact | Original attribution | Records/hashes |
| --- | --- | --- |
| windows-cli-corpus.json | clean6bd, Windows boundary only |20/40|
| windows-cli-inventory-corpus.json | cleand6, new executable, same boundary |20/40|
| linux-cli-inventory-corpus.json | d6 actualde834652/treefcfef1a0 |47/94 plus1intent|
| windows-coverage-corpus.json | clean669 current boundary |20/40|
| linux-coverage-corpus.json |669 actual68aba6bf/tree50531b8 |47/94 plus1intent|

Every raw stdout/stderr hash is independently checked. Earlier files are not
rewritten as later source execution; their byte identities and source/executable
attribution remain fixed. None is a tablet/provider/runtime run.

Original173 Linux39900485689 failed Clippy before tests: duplicate conflict
branches and a moved PathBuf in a test. Raw128852 bytes SHA256
b3af0d21a9987e219dff4832700c39164f2f09c7cb607cb9c4eed9e1661f3e58 retained.
The initial local173 CLI attempt failed clean provenance after the owner edited
a Linux file during verification; it is unqualified. Local ARM metadata compilation
lacked arm-linux-gnueabihf-gcc; no installation/settings change was attempted.

Original6bd Linux39900775186 passed417 library tests but failed the stale binary
flag-inventory assertion before CLI integration. Raw210292 bytes SHA256
96d13b184708f5a7d8ba01fe44038b917ee113505f5a6e6da0065c3000a82b06 retained.
The later passing d6/669 captures never relabel those failed attempts.

## Remaining delivery and project gates
Normal Docs-first squash requires final paired acceptance and all current required
Docs/source CI. Then verify actual merge trees, actual-main runs and official
source release/tag/provenance independently. No earlier candidate run qualifies
another commit. Those receipts belong in PR comments/canonical task tracking.
Manager browser/Electron consumption, selected-mode cleanup, other owned domains,
source acquisition/freshness, native/provider/runtime qualification and integrated
project acceptance remain outside this completed producer implementation.
