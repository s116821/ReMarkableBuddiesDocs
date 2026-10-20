# Delivered-parent APK integration

Source `61bcd76db6108a3f7a94fec37e00383691ae8a84` normally integrates
the existing APK branch `d68d5a0` with delivered main `42b5108`.
The effective child is exactly 16 release helper/test/configuration paths.
All 16 retain their exact original branch bytes, including the optional bounded
ABI reader. Every other tracked path equals delivered main, preserving its
Cargo/SDK identity, Reader implementation and maintained release workflows.
Historical pending Reader ancestors are not included in the effective child.

The paired Docs integration uses delivered parent `3eb4174`, retaining the five
original APK change artifacts unchanged plus this result. Historical r5 evidence
remains attributed to its actual v0.2.0 source and absent-SDK build. It does not
qualify SDK-consuming current source, reproducibility or installation.

Current Windows host checks ran 34 tests: 31 passed and three platform/container
controls were skipped. Docs ran 12 tests successfully; manifest checks preserved
25 current guidance files and 126 original blobs. Strict OpenSpec validation
passed all 42 items. Diff checks passed. No container, source compilation,
signer, package generation, installation or tablet contact was performed.

Current exact-head hosted checks and independent integration review remain open.
Source/compiler reproducibility, consumed-SDK variants, full signed negatives,
production trust, release integration and physical lifecycle remain unfinished.
No task completion, canonical sync or archive follows from these host controls.

Source basis: complete Git index comparisons against both merge parents,
unchanged existing source/spec artifacts and current retained host-check logs.
