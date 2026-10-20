# Producer verification and remaining gates

Implemented source Buddy76 aa8a7164b222e0f69371a1730b87cbc49505a471, paired Docs77. Precode reviews5588744686/5588756440 were read before code. Full source review5589006061 found one P2 reservation durability regression; correction acceptance5589074941 resolved it. Original review thread was resolved with reply4328149925. Other source paths/wire/legacy order were accepted unchanged. Source has12 owned paths preserving399 unrelated entries and old corpus/wire. Docs composes actual basic-companion deliverycc4cadf without editing its files.

The correction retains exclusive collision safety, creates Unix0700 reservation, secures/syncs destination and its parent before copying, and classifies post-reservation sync failure NotPublished while retaining output. Ten affected core controls plus final focused3 and strict all-target/all-feature Clippy passed. Two new injected controls prove ordering/private permissions and parent-failure boundaries. Fourteen original scoped controls and four Windows CLI groups separately cover original binding, mutex competitor, stage/marker/readback/prefix faults, promised-versus-omitted media, pure status with source/config absent, real case/junction refusal, source preservation and export→existing ordinary restore round-trip. Four relevant old storage regressions/five archive CLI/five ordinary-restore CLI/exact named Args passed.

Original actual Windows corpus remains immutable at productionadee57de94478e78627b45cb21ace470f8070bb4:38 reports/76 verified raw hashes,112203 bytes/SHA2562aedfcbbda9727bfdbba0767aeb6e059838c528a249103b819a096615d9de974, executablefe26551d2814b1098f87bb5324bafbf17291547cb8addfbe385bc03e152cb085 with durably persisted start/end provenance. It predates the reservation correction and supplies predecessor wire compatibility, not a corrected-build or Linux/device durability claim. No replay/relabel was needed. Status-after-verified-apply is exactly that; no induced transport-loss claim. The independent85-byte marker vector matches2d61ecb63ec1e95d63e178bad36e1a04131c04e586a00c829782f62c7daa1d61 and empty history19bf4c537633f421ba1fcec5e6897e9a29a392d701b7fe2ecdce93c21ec1272b.

Initial test-only Debug-bound/unused import diagnostics and repair Windows unused-mut Clippy failure were retained and corrected without suppression. Superseded adee/e0 candidate metadata and completed Checks logs were preserved before canceling duplicate builds; current exact CI remained untouched. No credentials/provider/runtime/tablet were exercised. The portable snapshot can contain private opaque endpoint/model/reference text; report privacy does not turn that archive into sanitized public content. Final review/normal linked merge/actual-main/release and broader consumer/native/project gates remain external observations.

## Exact Linux Checks proof

{
  "run": 39467229612,
  "job": 118781770949,
  "head": "aa8a7164b222e0f69371a1730b87cbc49505a471",
  "tested_merge": "fdd34794349045926a71b54b8d2c344b07fa09ac",
  "bytes": 256210,
  "sha256": "ecd10a6c4a040b049a9e17b818386b705b7a99d10d7b18e92a6821a5348623be",
  "verified_markers": [
    "exclusive_reservation_syncs_own_directory_and_parent_before_publication",
    "parent_sync_failure_is_not_published_retains_private_reservation_and_source",
    "intentional_omission_is_valid_but_missing_promised_object_is_not_observed",
    "same_real_mutex_spans_checks_copy_marker_and_readback",
    "actual_private_snapshot_preservation_verified_export_and_changed_path_restore_round_trip",
    "actual_symlink_destination_parent_is_refused_without_creation"
  ],
  "library_result": "ok. 381 passed; 0 failed; 1 ignored; 0 measured; 0 filtered out; finished in 122.71s"
}
