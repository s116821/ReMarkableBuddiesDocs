# Verification status

[Docs PR141](https://github.com/s116821/ReMarkableBuddiesDocs/pull/141) owns this finite paired implementation. Precode0c9452b2d752d8ac2341b090ac58fc5145bf9521 was independently accepted by Root against delivered Buddy4a75316 and existing strict Config/document/archive boundaries. Implementation is [Buddy PR129](https://github.com/s116821/ReMarkableBuddies/pull/129) at f1bfcb1abe0f2424fb5e241927805a12f271f28b. Current qualification is in progress; no canonical sync/archive or finished source review is claimed yet.

Production uses the existing whole saved-document validator and regular-file reader. It introduces only two explicit exclusive file selectors and config::portable. Existing Config/archive schemas, writers, provider/native paths and dependencies remain unchanged. Private export and redacted inspection are distinct outputs.

The first focused Windows compile failed because draft tests referenced the absent tempfile dependency. The failed portable-config-unit-r1.log is preserved. Tests were corrected to the repository's standard-library UUID temporary-directory pattern; no dependency was installed or assertion weakened. Windows unit-r2 passes all6focused library tests, with9existing platform/test warnings preserved. Linux-only symlink control is not compiled on Windows and is not counted as a pass. Actual Windows CLI2/2passes, with3existing library platform warnings preserved. Linux-only CLI FIFO/symlink control is not compiled on Windows. The passing library controls use real temporary files for projection/inspection, exact unchanged source/excluded-root checks, raw declaration/null preservation, whole-source validation and recursive duplicate refusal, closed artifact/version validation, inclusive1MiB/128KiB bounds and maximum escaped personalization text, plus consuming prefix/flush failure controls. Source/current-head Linux CI, independent final implementation review and same-pair finite sync/archive remain required.

No real user preferences, provider calls, tablet execution, archive integration, import/application, runtime activation or full portable-domain/REM52 acceptance is established by this work. Root owns final source review and integration; Main owns returned fixes and exact qualification evidence.


## Requirement/scenario mapping

| Contract | Source and meaningful control |
| --- | --- |
| Explicit allowlisted export | config::portable::project reuses inspection::document before selecting3raw keys; real_files_preserve_declarations compares exact private settings, digest and unchanged source while excluded roots stay absent |
| Exact declarations | omitted_sparse_null_and_disabled exercises absent parents/children, null, empty objects, disabled text and both research enum choices through export+validation |
| Whole refusal | whole_source_validation and offline_artifact_is_closed cover malformed/duplicate/unknown/invalid unrelated settings and version/type/excluded-key/trailing-data refusal |
| Input/output bounds | inclusive_input_bounds exercises exact/over config and artifact bytes plus maximum escaped text, unsafe/missing/directory/dash inputs; output_failures forces prefix and flush errors without replacement |
| Actual dispatch/no startup | portable_configuration_cli executes real selectors with unclosed stdin and unusable environment config, roundtrips offline without original source, checks exclusivity and semantic refusal; Windows2/2passed; Linux special-file control still requires hosted evidence |
| Linux-only files | unit symlink and actual CLI FIFO/symlink controls are gated unix; Windows does not establish these outcomes |

New report/portable containers deliberately have no Debug implementation exposing the artifact. Export's private text output is explicit; inspection summary contains only artifact digest/count/presence. No real preference data was used. No simulator delta is needed for an offline file/serialization command; native/runtime behavior is unchanged.
