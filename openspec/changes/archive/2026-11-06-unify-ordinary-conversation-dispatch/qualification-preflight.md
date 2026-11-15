# Receiving qualification pre-dispatch evidence

## Frozen source and reconciliation

Buddy200d21733c1a402d3b68a93430f0e05e82e16ca2 contains the bounded entry and
exact request sequence in qualification-plan.md. Normal reconciliation commit
be9ad1e retains delivered main516b60b29fe7d7db46a22480312d6155657a69d0.
The sole content conflict was simulator mode routing: retain both the existing
combined branch and newly delivered exchange-history branch. Their actual binary
scenarios were subsequently executed. Docs normally integrated delivered
1b26d39cd72442c373ad68c112d167c88ed52870 in the existing paired branch.
No importer, native experiment or other author branch was altered.

## Credential-free host checks, November 6, 2026

The existing Windows x64 Rust1.98.1 Cargo target was reused; no second cache or
provider invocation. Source contents passed:

- `cargo test --locked --offline --lib simulator::combined --all-features --target-dir ../ordinary-configuration-target`:
  all6 pass, including the maintained combined/deduplication and unavailable/
  over-budget history controls; the same seven-stage entry runs with real Stores,
  exact histories/image associations, reducer input digest and retained drafts.
  Additional controls reject an eighth call, any call after failure, expired
  deadline and invalid live allowances; pure protected identity checks require no
  credential access. Initial Reader and notebook-map parts exclude Source A's
  numeric facts. The scripted backend's expected replies are not model evidence.
- `cargo test --locked --offline --lib selected_qualification_loopback --all-features --target-dir ../ordinary-configuration-target`:
  existing maintained actual OpenAI loopback control passed, including redirect,
  disconnect and invalid-answer refusals. This is synthetic transport evidence,
  not a live receiving semantic pass. The opt-in no-retry/no-redirect switch is
  now available to this simulator entry; default production transport is unchanged.
- `cargo fmt --all -- --check` and source/Docs diff checks passed.
- Docs12 tests and guidance36/preserved126 checks passed. Strict OpenSpec all
  validation passed122/122; the active change remains unarchived.

The initial compile rejected an incorrect new-harness Writer Status::Refined
assertion and one unused import. Existing refinement returns Generated. Those
were corrected; the final6-test run uses that actual contract. The failed log is
retained rather than relabeled as a pass. Windows emits existing unrelated
platform-gated dead-code warnings; current strict hosted Linux CI remains separate.

## Actual binary payload capture

Built the clean committed source with
`cargo build --locked --offline --bin reader-buddy --all-features --target-dir ../ordinary-configuration-target`.
Actual binary SHA256 is
3a89532b2f98e5b0d8d9d3e41b6287eb780e0750b44431dd45bc05df55c7db25;
its version is `remarkable-reader-buddy dev.v0.73.0-13-g200d217`.
The report identifies source200d217 and source_dirty=false, not a release build.

Three actual CLI scenarios passed: the new scripted qualification, the original
combined scenario and delivered owned-exchange-history scenario. The new scenario
was copied with only its generated output path relocated into an owned evidence
directory; original and selected scenario hashes, exact argv/cwd/environment and
original stdout/stderr bytes are retained. An explicit empty owned dotenv and
minimal process environment with a nonexistent Config selector prevent ambient
credential loading. The report confirms credentials_resolved=false and seven
scripted engine-interface calls, zero provider calls/external exports/native effects.

Raw report SHA256:
01f4e93cb9bf4ab806f6b653cbdcc1b4719deffb1682a78c29ff8e9b7159fb19.
Capture manifest SHA256:
b58a791a37bcba375802db4ee6c131bcb02beba52dd746b6dec30a7eea8b527c.
This report preserves all original receiving text parts and replies, stage labels,
attachment raw/encoded digests, actual associations and persisted reducer digest.
It is the credential-free request plan for independent review, not live proof.

## Review and dispatch gate

No real provider request or protected credential resolution has been executed by
this preflight. Independent review must reconcile exact code/Docs/binary/image
identity, the scripted request trace and the privately selected Config digest,
model and HTTPS origin before a separately selected actual run. A fresh output
directory is mandatory; any provider/auth/quota error stops without retry. Keep
the seven POST/4000 token/90s/12min limits unchanged. Live returned text then needs
independent factual/source-attribution review rather than arbitrary wording equality.

Optional subject memory remains disabled by the current dispatcher. Memory-enabled
receiving, native composer/input/page effects and genuine aggregate-apply acceptance
remain their existing unfinished obligations. Neither this preflight nor a future
model pass completes them or grants native/export authority. The paired PR/change
stays active; later finite spec sync/archive must preserve those unfinished gates.
