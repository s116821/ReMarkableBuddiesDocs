# Verification in progress

Initial implementation candidate: Buddy6bd396bf771695d9760ce33ecfd119b16264020c,
paired with accepted concrete contract Docscfd133ad6d1cd172b58d5c410a671a2337bab9f5.
This record does not close the producer or integrated project.

## Windows boundary
Fresh clean candidate passed fmt, strict all-target/all-feature Clippy,4 unit
tests and2 actual CLI groups. windows-cli-corpus.json preserves20 separate child
records/40 verified raw stream hashes plus clean source/tree/executable identity.
These prove only unsupported-before-stdin/Config behavior and fixed encodings,
not Windows filesystem maintenance or directory durability.

## Preservation
423 other source base entries are exact. Original lib.rs and retrieval/disk.rs
are complete byte-exact prefixes; removing only the new fields/route reproduces
original main.rs. The seven source test vectors equal accepted Docs bytes exactly
(4835 bytes, SHA256 7d0462d62e417fde0eac9533c39f3df976b64c5b1f8f96001538fad534e83031).
Existing Store/cache APIs and protected credential/Reader/Writer code are unchanged.

## Successor evidence and pending qualification

Test-only d6f4a4ca81237c758c52e77528acdb4364cad392 passed fresh Windows
fmt/strict Clippy/6bin/4unit/2CLI. windows-cli-inventory-corpus.json preserves its
separate20 records/40 hashes and new source/tree/executable attribution.

Original d6 Linux Checks120244239073/run39901600803 passed, including417 library
tests (1 existing ignored),6binary tests and4 new CLI groups. Its actual checkout
de834652ed1d53a691308e19301a5006913e3927 treefcfef1a0770e7f79d27843e367c65b2c5ce78fee
matches reviewed d6 exactly. linux-cli-inventory-corpus.json preserves47 child
records/94 verified stream hashes plus one independently verified prepared intent.
Original raw log627964 bytes SHA256
fc7d2d759738d3ba46c4aac1e5765d4af8b38431340aabd84ea92ea681ddc4e1;
normalized46256 bytes SHA256
c215af9ec62d125b92876e8de4493a35d1f69c61e7577361b5e8b0dc8a5ab3f5.

Coverage-only successor669c0774530699500984dda038cc5138ed474c4e adds five
explicit Linux control groups and modification-time preservation checks, with
no production/API behavior changes. Current Windows/Linux verification of this
successor remains required. Static source review5623992783 found no blocking
production issue at d6; it is not acceptance of unexecuted successor tests.

Current full CI, focused coverage review, canonical sync, completed archival,
paired final review, normal delivery and actual-main/publication remain pending.
No tablet, provider, real credentials or installed/native runtime qualification.

## Retained failures
Original173377e Linux39900485689 failed before tests on a duplicate conflict branch
and moved PathBuf in a test. Original raw job log128852 bytes SHA256
b3af0d21a9987e219dff4832700c39164f2f09c7cb607cb9c4eed9e1661f3e58 is retained.
The initial local173 CLI attempt failed clean provenance after the owner edited
a Linux file during verification; it is not qualification. Local ARM metadata
compilation lacked arm-linux-gnueabihf-gcc, and no installation was attempted.
The6bd Linux run then passed417 library tests but failed the stale retained binary
CLI inventory assertion before integration; raw210292 bytes SHA256
96d13b184708f5a7d8ba01fe44038b917ee113505f5a6e6da0065c3000a82b06 is retained.
No historical failed result is relabeled by later source corrections.

## Coverage mapping before completion

| Contract vector | Existing evidence | Remaining control |
| --- | --- | --- |
| strict wire/hash encoding and literal selector | common parser/vector/NoRead units; Windows child corpus | Linux raw malformed input before filesystem audit |
| preview preservation, apply and absent reconciliation | Linux preview_apply_status unit | file modification-time preservation alongside bytes/modes |
| original binding and unsafe slot refusal | changed_config/unknown_staging units | actual actor/root/generation/namespace replacement; header/capacity bounds |
| busy/missing lease and output failure | namespace_or_store_writer and consuming_output units | named held lock replacement and exact known-read allowlist |
| post-unlink uncertainty | injected sync/readback unit; absent status | original current Linux CLI corpus still required |

These gaps are not marked verified. A focused test-only successor will complete
controls without changing the accepted production contract or legacy APIs.

## Current executed coverage:669c077

Current Linux Checks120247726452/run39902717766 passed fmt, strict all-target/
all-feature Clippy,422 library tests (1 existing ignored),6binary tests,4CLI
groups, retained suites and maintained checks/audits. All15 new library tests,
including the five added coverage groups, executed successfully.

Actual clean Linux checkout68aba6bfc5e955644173c59d1aeed8529bc7dc9f was fetched;
it has reviewed669 tree50531b8de160e31984260fe8741baf5db64290cc. Executable SHA256
552e546b4b14cce41e2535eeb60020230f717a215fa650d14c61b889273c92a9.
Original log628964 bytes SHA256
1e2ea1a9444f7337c9934bbd2d14f28881b159422221e4390a8f19f48782d5f7;
current47 CLI records/94 raw stream hashes and one prepared intent were independently
verified. Normalized46256 bytes SHA256
9153378bcbbcf8e37281f78e6a85cbbd33074bcfb901360921ef38ba17b555aa.
linux-coverage-corpus.json retains this current source/executable attribution.

Current Windows fmt/strict Clippy/6binary/4unit/2CLI pass. Its separate20 records/
40 hashes, source669/tree50531b8 and executable
bd079eb86d505cd3b169995578404d5a22d0cfd4a2a16400cc15199647474668 are retained in
windows-coverage-corpus.json. Raw log11111 bytes SHA256
7ed85a7c595ebeeadb0e801c042e38fbd16a9d4191b92a9be6c59b3bdfc38f5d;
normalized9702 bytes SHA256
ccf4624c02104fce35bfa9fad104a745204ed23f30fb872c7cbfe038cd554a18.
This proves only Windows early unsupported/no-read behavior and fixed encodings.

Focused independent source review5624059085 at669 found no blocking finding and
verified the cfg(test)-only successor. Original production review5623992783 atd6
remains applicable to unchanged production behavior; neither substitutes for
current executed evidence above.

| Promised control | Executed current evidence |
| --- | --- |
| closed/raw wire, digest and alias admission | common frozen/closed/NoRead units; malformed_utf8_duplicates_shapes_ids_and_bounds_access_no_paths; actual CLI refusal/EOF groups |
| noninitializing exact known header reads | exact_known_read_allowlist_excludes_all_other_payloads; dedicated_admission_does_not_need_durable_payload_directories; actual CLI poison-commit fixture |
| original actor/root/generation/namespace/config-path/file binding | changed_config_marker_generation_and_file_identity_refuse; actor_roots_generation_namespace_path_and_changed_valid_bytes_refuse |
| namespace/entry/header bounds and unsafe/schema shapes | unknown_staging_unsafe_and_bad_material_preserved; capacity_header_bound_object_shape_and_namespace_reparse_refuse |
| existing lease and named identity custody | namespace_or_store_writer_and_missing_lock_never_initialize; replacing_a_held_named_lock_refuses_before_observation |
| one-slot preservation and uncertainty | preview_apply_status_preserve_every_other_file_and_never_recover; post_unlink_uncertainty_is_never_rollback_or_retry; consuming_output_keeps_both_leases_through_partial_failure |
| preservation metadata | before/after file bytes, modes and mtimes in nonmutating scenarios, excluding OS-managed access times |

These current results resolve the earlier mapping gaps. Older captures/failures
remain separately attributed and unchanged. Source Build/Integration, final
paired Docs/source review, normal Docs-first merges, actual-main and publication
remain independent delivery gates. No tablet, provider, real credential, installed
runtime, native source freshness or integrated project qualification is claimed.
