# Design

## Existing boundary

Source baseline is Buddy6b52a6db5067f18dcaf4f8da03c6290bae98e702; Docs baseline isf0bad1743cf03c851e8af316804068709b4221b9. config::portable has only Export/Inspect. Its complete validator accepts exactly three raw declarations and preserves omission/sparse/null semantics. The [original artifact contract](../archive/2026-11-06-export-portable-configuration/contract.md) says missing fields are not reset commands. The existing raw conditional publisher is Store::replace_config_document; basic::Custody supplies Store/mode ownership through consuming output. Personalization's current family is legacy1 plus ready ordinary notebooks, narrower than the selected-aware product/research family.

## Application policy

Use an explicitly named present-declaration overlay, not a snapshot reset. Missing settings/children preserve destination declarations. Present object parents merge only their present children, preserving absent children; an absent/null destination parent becomes an object when the artifact explicitly supplies an object. An explicit empty object therefore establishes object presence if needed but does not remove children of an existing object. Present supported null is saved as null, never a removed JSON member. Present scalar children replace that declaration. Validate the whole original destination, artifact and resulting target with the existing strict typed/duplicate-free configuration rules. Do not materialize defaults or decode/reserialize excluded values through typed Config.

This policy is deliberately not a general JSON merge-patch: null does not delete, arrays/unknown fields refuse, and only the fixed current preference schema is admitted. No clear/reset operation is included. An empty settings map is a no-op. A semantic no-op preserves every original file byte and acquires no Store.

## Conditional private protocol

Use a separate early CLI operation family and exact stdin input for changed requests. Inspect/Prepare/Status read only the explicit saved Config and request; no root probes or environment credential resolution. Prepare returns sanitized change metadata and a digest-only intent. Apply takes that original intent plus the original artifact, recomputes the target and refuses any changed destination/path/artifact/target. Status takes only the intent, observes exact desired full bytes versus unresolved, and never reapplies. Hash correspondence does not authenticate an artifact or establish native/runtime authority. All frames and derived hashes remain private maintenance transport.

## Existing-only Apply

Use one distinctly named portable-preference constructor with selected_aware=false and unchanged NotebookAdmission::Preferences. Admit legacy1 and complete owned ordinary notebook4 with absent/LocalOnly mode; refuse legacy2/3 and active/retained selected history. This is the common supported family for all three imported declarations and does not silently widen personalization. Preserve every other constructor/caller. Reuse full existing notebook readiness, recovery/local-manifest and mode admission under the original OS custody; never initialize/adopt/repair or clean stages.

Validate configured roots and canonical disjointness, including the existing Config target outside every data/cache/credentials root; refuse canonicalization/alias ambiguity. Reuse the existing canonical checks where practical without changing old routes. Recheck relevant identities under the admitted custody before publication. The filesystem model remains trusted local paths/cooperating Store writers, not adversarial pathname-race protection. Retain existing conditional publisher/mutex/readback and basic::Custody through write_all success/error, without adding flush to this mutating protocol. Keep the original exporter/inspector's write/flush behavior unchanged.

## Qualification

Exercise actual file/Store/CLI behavior on legacy1 and real record/media notebooks with absent/LocalOnly mode. Cover all overlay presence/null/sparse/disabled-text cases; exact Unicode/CRLF/control text under existing validation; excluded private declaration preservation; invalid whole originals/artifacts/targets and duplicate/version refusal; no-op exact bytes; Busy, stale original/path/artifact/target and Status without the artifact. Assert data/cache/media/identity/current/other credentials unchanged. Include legacy2/3 refusal, notebook readiness/mode/history corruption without repair, actual Windows case-alias and Unix special-path controls. Use existing publisher AtomicCall/AfterPublication/ChangedReadback hooks and immediate/prefix output faults with actual lock-held/released probes. Use actual bounded subprocess CLI with open stdin Inspect and poisoned runtime/provider environment; preserve current binary option inventory. No provider/native proof follows from synthetic host tests.

## Delivery status

Precode only: no production implementation or execution is claimed. Independent contract review and fresh normal baseline reconciliation precede code. Keep original failed evidence, exact tested revisions and platform limitations distinct. Complete this finite change in paired source/Docs PRs through verification, canonical sync and archival; broader synchronization and native qualification remain separate.
