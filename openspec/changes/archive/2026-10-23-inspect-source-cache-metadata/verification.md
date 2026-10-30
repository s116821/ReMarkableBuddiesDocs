# Implementation verification

The producer is implemented at Buddyb473875768eccd9fed5c7174911e6554c6bc9781
against accepted concrete contract Docs8503d4c0e62ea478d5fd7ce24a2e52d39cf75340.
This verifies synthetic source/CLI behavior, not shipment, Manager integration,
tablet, provider, native freshness or installed runtime qualification.

## Current Linux execution
Current run39908914965/Checks120267182946 passed fmt, strict all-target/all-feature
Clippy,429 library tests/1 existing ignored,6binary tests,4inventory CLI groups,
preserved cleanup CLI/regressions, all seven frozen digest vectors and maintained
checks/audits. All six inventory Linux fixture groups and the shared fixed-report
control executed. Current source39908914965 completed Title/Checks/Build/Integration PASS;
PR Release correctly skipped. This qualifies the exact current b473 candidate,
not a future merge or native runtime.

Actual clean b4a09e8666d4b6ad1c4b467a6b80af2dd7e58e5c was fetched; its
93b9b7c928f4702c9a38b676da8a090956313a1a tree equals reviewedb473. Both Linux
corpora record executable SHA256
840d47c5a08be27b7fb5ed7bc3f02af3f3290567f165529cd3d0f9998b2a7b52.
Original raw640731 bytes SHA256
3d3a94fb19638e5f0019f3f2bcb06d3f005372ddae2727a9c91e576ee41b17da.

Inventory12 records/24 raw hashes were independently verified, normalized8771
bytes SHA256810163ffc8bfd85b8ce57a9695412aaa329cde35525ccb2e92ce4d9445e5792a.
Separate cleanup compatibility47 records/94 hashes and1 prepared intent were
verified, normalized46256 bytes SHA256
82ffb4eaf80b6c47964e92f19ba2f36f17be42b685fafb91d5ee8dd3f56a7df6.
The Linux wrappers retain their original source/tree/executable attribution;
old cleanup captures are never relabeled as this new execution.

## Current Windows boundary and diagnostics
Fresh frozenb473 fmt/strict Clippy/6binary/6shared-cache unit/3inventory CLI/
2preserved-cleanup CLI pass. Clean sourceb473/tree93b9 and executable SHA256
1752c4d41bafddd3f68a95203a71cc702181c4b8384bc165c9479ea302672df1 are recorded.
Inventory7 records/14 hashes independently verified: raw6033 bytes SHA256
fa687bc7dcebe4a838b18499fe55d9a31cf5d02db3b6b903bbad850e5d16a2a6,
normalized4878 bytes SHA256
d61188fba15bcfe9daac3bfca0f7f29afa3eaa9f60deed4ed6421cf2cde52020.
Cleanup20 records/40 hashes verified: raw11110 bytes SHA256
b934e36da35c17d78306a7714d3f4ebbaa083abc85cdcd1efc47aeaffd3b6586,
normalized9702 bytes SHA256
ccf4624c02104fce35bfa9fad104a745204ed23f30fb872c7cbfe038cd554a18.

These prove early unsupported/no-input, recognized conflicts omitting supplied
values, ordinary potentially echoing syntax diagnostics and old cleanup refusals.
They are not Linux metadata/cleanup or local Windows filesystem qualification.
Normal syntax-error stderr is not falsely described as a sanitized JSON report.

## Exact requirement/vector coverage

| Requirement/vector | Current executed evidence |
| --- | --- |
| bounded0/1/16 sorted metadata inventory, unread payloads and preservation | inventory_empty_one_sixteen_sorted_and_metadata_only_payloads uses exact header-read allowlist plus byte/mode/mtime snapshots |
| zero/max32MiB and unreadable/corrupt contents | inventory_zero_maximum_unreadable_and_corrupt_are_only_metadata; actual CLI corrupt/zero payload cases |
|17slots/oversized metadata/unknown/staging/marker shape/symlink/nil IDs | inventory_bad_capacity_names_markers_sizes_and_links_have_no_partial_list; preserved cleanup schema/ownership/bounds controls |
| busy/missing/replaced existing leases | inventory_existing_busy_and_missing_leases_refuse_without_creation; inventory_bracket_changes_discard_metadata_not_mutate_or_retry; preserved replacing_a_held_named_lock_refuses_before_observation covers both shared lease identities |
| changed Config/marker/slot length/identity/absence clears result | inventory_bracket_changes_discard_metadata_not_mutate_or_retry; retained shared-header actor/root/generation/namespace/path controls |
| custody through output failure/no mutation | inventory_output_failure_keeps_both_leases_and_preserves_all_bytes; preserved cleanup output/uncertainty controls |
| metadata grants no cleanup authority | every report flags unread/unvalidated/freshness/cleanup limits; actual fresh separate cleanup prepare refuses the listed corrupt/zero slot |
| separate parameterless/platform/parser contract | fixed_refusal_shape_and_limits, non_linux_config_is_never_admitted; actual held-stdin no-startup and three recognized conflict/three ordinary syntax cases on both hosts |
| cleanup compatibility | all prior15 Linux cleanup library controls, unchanged seven vectors and current47 actual Linux cleanup records/1intent digest |

The current source path never opens slot contents or constructs Store. Its private
header observation reuses the bounded known-file custody and maps the same fields
back into the old cleanup intent; inventory never fabricates a mutation token.
Guarded fixtures deny entry/durable payload reads/enumeration. Header admission
preserves ordinary supported format and existing lease/ownership requirements.

## Preservation and independent review
427 source baseline entries remain exact; disk/config/selected-payload validator
and all seven cleanup digest vectors are unchanged. Prior main is byte-identical
after removing only the new route/flag/test-inventory addition. The old public
cleanup report/intent module changes only Linux module visibility within the crate.
Its Linux implementation factors private typed header fields and sorted slot-name
admission, retaining old cleanup behavior and output/custody/uncertainty semantics.

Concrete precode5624361353 accepted850 after the parser-policy clarification.
Static source review5624594585 atb473 found no actionable finding and independently
checked Windows raw/corpus preservation. Current Linux raw/provenance/corpora were
also independently verified; these are evidence checks, not final delivery acceptance.

## Original captures/failure remain separately attributed

| Artifact | Source/platform/scope | Records/hashes |
| --- | --- | --- |
| windows-initial-inventory-corpus.json |c63 Windows boundary/parser only|7/14|
| windows-initial-cleanup-compatibility-corpus.json |c63 Windows cleanup refusals only|20/40|
| windows-current-inventory-corpus.json |b473 Windows boundary/parser only|7/14|
| windows-current-cleanup-compatibility-corpus.json |b473 Windows cleanup refusals only|20/40|
| linux-current-inventory-corpus.json |b473 actualb4a09e86, Linux inventory and separate cleanup revalidation|12/24|
| linux-current-cleanup-compatibility-corpus.json |b473 actualb4a09e86, Linux independent cleanup|47/94 plus1intent|

Every raw stream hash is independently checked. All six blobs retain their own
source/executable identity, original order and byte hashes. No prior capture is
rewritten or credited as a later source execution.

Originalc63 Linux39908525096/Checks120265944379 failed strict Clippy before tests:
a Unix permission fixture used decimal0 rather than octal0o0. Raw126317 bytes SHA256
1e552122a6f3fe7a04583e7a861c8b97052a2cff44385ee74b8884d1061251c4 retained.
Successorb473 changes only that one equivalent-value test literal. Passing current
execution never reclassifies the failed initial attempt as Linux qualification.

## Remaining delivery and broader scope
Final paired evidence/lifecycle review and all current required Docs/source CI
precede normal Docs-first squash. Actual merged trees, actual-main and official
release/tag/provenance must be separately observed and recorded in PR comments/
canonical task tracking. No prior run qualifies another commit. Manager consumers,
physical transport/native/provider/runtime and broad project acceptance remain
outside this completed source observer implementation; inventory grants no cleanup
permission and later cleanup still requires fresh selected-slot confirmation.
