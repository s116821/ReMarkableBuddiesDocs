# Personalization configuration maintenance

This bounded REM-53 contract supports a real Manager editor through the existing
configuration writer. These maintenance operations do not invoke providers,
alter transcripts, synchronize the setting or prove a running runtime reloaded.
Owning changes: `personalization-config-contract` and its independent-main
integration `personalization-main-integration`, plus the declaration-preserving
notebook maintenance change `preserve-personalization-documents`. Older binaries without this
CLI/field reject unknown settings; do not write the field through an older binary.

The optional `Config.personalization` field defaults to:

```json
{"schema_version":1,"enabled":false,"text":""}
```

Text is UTF-8, at most16384 **bytes**, and contains no NUL. The JSON codec preserves
CRLF/LF, multiline Unicode, tabs and leading/trailing whitespace without trimming
or normalization. Empty text is ineffective even when enabled. Disable retains
the text; clear resets it to empty and disabled. It is a portable preference,
separate from source/document content, history, handwriting learning, subject
memory, credentials and operation/safety grants. Current explicit requests and
fixed source/page/operation protections outrank it when consumers are integrated.

## Fixed CLI and Manager handoff

Select an existing config using the already supported absolute
`REMARKABLE_BUDDIES_CONFIG` environment variable. The only new argv surface is:

```text
reader-buddy --personalization-operation inspect
reader-buddy --personalization-operation set
reader-buddy --personalization-operation disable
reader-buddy --personalization-operation clear
```

Commands run before dotenv/API-key/model/device startup. They accept no prompt,
path, arbitrary command or provider credential in the JSON request. Inspect reads
the explicitly selected config without opening or initializing a Store. Mutations
take one strict JSON object through stdin, at most131072 bytes. Invalid UTF-8,
duplicate/unknown fields, unsupported contract version or oversized text refuse.

Inspect returns a version1 JSON report, including the complete-file
`config_sha256` revision and exact editor value. Set input is:

```json
{"contract_version":1,"expected_config_sha256":"EXACT_64_HEX_REVISION_FROM_INSPECT","enabled":true,"text":"  First line\r\n第二行 🦊\n "}
```

Disable and clear accept only:

```json
{"contract_version":1,"expected_config_sha256":"EXACT_64_HEX_REVISION_FROM_INSPECT"}
```

Use a JSON encoder and byte-preserving stdin/SSH transport, not shell interpolation
of user text. Check `status`, not just process exit: consistent with existing
maintenance commands, operational refusals are structured reports. Success is
`status:"ok"`, `disk_reload_verified:true`, a new `config_sha256`, the exact
`personalization` value, and for mutations `runtime_activation:"restart-required"`.
Inspect uses `runtime_activation:"unverified"`. No other settings are returned.

Statuses are `ok`, `invalid-input`, `unavailable`, `unsupported`, `busy`, `conflict`
and `failed`. Failure reports have no prompt/config contents or exception paths.
Any unsuccessful/missing response after dispatch can be an uncertain write outcome;
inspect fresh before deciding whether to retry. Never assume a failed receipt means
the previous file survived. Explicit editor readback contains the text; do not put
its raw stdout or input into routine logs, telemetry, screenshots or issue comments.

## Ownership, reload and request boundary

Use the existing stop-confirm-lease maintenance protocol. An existing owned Store
is required for every mutation; missing/unrecognized storage is not initialized,
and a held runtime lease reports busy. The scoped personalization admission
validates ownership and the existing generation under one retained lease. Legacy
format1 remains supported; legacy selected/feedback formats2/3 remain refused.
An already-ready ordinary notebook format4 is supported only with exact current
actor/contract/capability readiness, complete local manifests, absent/empty selected
and retained history, and validated absent/LocalOnly mode. It does not initialize or
repair missing markers/directories, clean staging files or publish metadata. This
entry point belongs to shared storage and does not need subject-memory or Reader
runtime modules. The command reuses REM-36
`Store::replace_config_document` with whole-file CAS and its safe-path/staged atomic writer.
Only the personalization JSON member changes. Other raw saved values, omissions,
sparse objects and supported null declarations remain unchanged after decoding;
file formatting/member order may change. Set, disable and clear write the complete
existing personalization value, without materializing unrelated Config defaults.
The config must remain outside data/cache/credentials categories. History and
learning records are not cleared. Existing records must pass normal recovery
validation; unavailable commits refuse maintenance. External same-user hostile
writes and power-loss behavior are not new
guarantees of this command.

The reloaded setting and complete published digest are checked after saving while
the Store lease is retained. The lease ends before report serialization; the public
non-consuming report remains historical data and does not hold output/flush custody.
An output failure cannot trigger another publication. **Disk readback is not running-runtime activation.**
Manager must keep the saved/restart-required distinction and separately perform
the qualified controlled restart plus actual runtime verification before calling
the setting active. This increment neither restarts a service nor manufactures a
runtime reload acknowledgment.

Receiving consumers may take `Config::personalization_snapshot()` only after their
verified config load. It returns a validated immutable `PersonalizationSnapshot`:
`schema_version()` returns1 and `effective_text()` returns the exact enabled,
nonempty text or None. Keep that snapshot for the whole request; a later load/edit
cannot mutate it. Debug formatting redacts its text. The accessor alone does not establish
current-request precedence or end-to-end behavior; receiving contracts qualify
those integrations separately.

## Verification and unfinished work

Focused public controls:

```text
cargo test --locked --lib config::personalization::tests
cargo test --locked --test personalization_config --test storage_config --bin reader-buddy
cargo fmt --check
```

These use actual temporary configuration/store files and the actual host CLI,
with no API credentials, provider call, tablet, routing or service operation.
Missing owner/generation structure, unsupported markers, corrupt commits and
busy ownership are refused without repairing storage or changing configuration.
The refused attempt releases its lease before a later valid command runs.
Windows host controls do not prove Linux/native durability. Ordinary Reader/Writer
receiving behavior is qualified separately in the receiving contracts. Native
gesture/preset routing, runtime restart qualification, selected sync policy and
remaining Manager integration retain their coordinated REM-53/REM-42/REM-52 gates. Field presence alone does
not complete REM-53.
