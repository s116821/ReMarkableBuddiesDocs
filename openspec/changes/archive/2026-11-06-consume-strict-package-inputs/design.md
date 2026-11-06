# Design

Use a separate explicit `apk_package_inputs.py` CLI. Its external completion hash
and original producer SHA are independent inputs, not inferred from adjacent JSON.
Run the unchanged strict verifier, then bind actual full source/license and
independent SDK release proof to both retained target records. Normalize tuples
and lists through JSON representation only; compare every proof field.

Keep original producer and new packaging executor checkouts and revisions
distinct. The original tagged producer/release/SDK inputs remain read-only. Use
fresh disjoint external work/final roots. Stage exact binary and canonical build
metadata bytes with checked copies; source LICENSE and the pinned resident bundle
complete the existing generator inventory. Private build evidence stays private.

Extract the original builder's generation/observation tail into one helper. Both
CLIs use its unchanged container arguments, pins, 120-second phases, owned cleanup,
ephemeral private key and separately supplied generation-control SPKI pin. A
receipt consumer callback rechecks source, proof and inputs before generation,
after observation and before exclusive completion. The final receipt identifies
both the accepted build receipt/original producer and the packaging executor.

Host tests use owned synthetic files and mock only external source/tool/phase
boundaries. They prove refusal before launch, no compiler/build calls, checked
copies, unchanged metadata, failure without completion and separate public-key
observation. Actual signing/container/device execution remains a later explicit
operation, not a requirement for completing this bounded source capability.
