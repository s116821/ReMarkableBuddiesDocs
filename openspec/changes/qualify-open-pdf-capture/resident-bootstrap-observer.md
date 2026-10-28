# Bounded native bootstrap observation

The next native qualification question is whether the unchanged read-only
bootstrap can launch its copied Reader with the installed launch environment,
consume admission, expose the authenticated endpoint and return one Observe
result. This does not qualify page creation, selection, source continuity or
Writer. The existing native artifact remains mutation-disabled.

Provide an explicit development example using the production ResidentRuntime,
Store journal and SDK transport. Freeze the exact observation-only profile,
adapter and stock executable digests in this example. Accept only a fresh
32-lowercase-hex nonce, with fixed payload paths below its owned staging root
and a fresh private runtime root. Do not accept commands, environment overrides,
alternate hashes or mutation requests. Use the installed launch's minimal
environment and `--system` argument, one 60-second absolute startup deadline,
one at-most-10-second Observe deadline and bounded owned-child cleanup.

Use the real request input observer through preparation/handshake/Observe and
final reply admission. Retain runtime identity and historical reply or failure,
plus explicit shutdown results. An observation refusal is evidence, not a retry
condition; do not navigate, draw, reopen or select another document. Keep all
fresh directories and logs for later verified archival/cleanup. No native
authority or current source lease is minted from a successful reply.

CI shall compile a separate ARMv7 diagnostic artifact from the same exact source
revision after ordinary source checks. It is not a release package or installer
asset. Preserve the normal application package inventory and release gates.

Before ANY native execution, freeze the helper binary and payload hashes and
independently review the exact controller and recovery setup. That controller
must verify the original stock/Buddy identities, source preservation and idle
device, arm UI-independent bounded recovery, stop competing services and prove
their original groups empty before starting the helper. The helper does not
stop or start services. Its owned-child exit does not itself restore stock;
the independently reviewed controller must prove restoration and retain evidence.
No installed production profile may be inferred from this diagnostic.

The October 26 02:29 UTC read-only inventory found no Python or timeout command,
unchanged stock/Buddy process identities, and no resident profiles/latch. The
legacy Buddy service has no watchdog. Consequently an SSH shell or that service
is not sufficient independent recovery for the planned bootstrap run.

## Implementation and evidence

Buddy `2d9f53aaa444b4de5c0218be33a3ee6a87799827` implements this contract in
`examples/resident_bootstrap_observer.rs`. Independent source review accepted
its fixed hashes, guarded single Observe, original deadlines and explicit
shutdown-before-reporting. Existing guarded Runtime methods and the sampled
service property getter are public for the example, without changed behavior.
The separately uploaded ARM artifact records its checksum and actual frozen
build source SHA; GitHub's merge build SHA must not be confused with the PR head.

Formatting and whitespace checks pass. The new workflow packaging regression
passes locally; the full workflow fixture suite has eight passes and one
environment failure (`spawnSync jq ENOENT` on Windows). Hosted Linux execution
and ARM compilation remain pending. No local Rust build was attempted with
insufficient disk space. Source review does not authorize native execution.

The read-only tablet inventory is retained under
`bootstrap-prerequisites-45aee32d3be24681a9e24fa7f2e16aef`, with source SHA256
`7147f5ce4cd24c206e34e2074c178f6733c0664e0d009091d9505649f2f78542`.
It sampled services and available commands only; no payload transfer, service
change, input or document mutation occurred. Native acceptance remains open.

## Completed bootstrap diagnostic, October 28, 2026

Buddy `72cef541562f9884ca3b348a339a81b0cb8e81bd` passed
[full CI 40437426851](https://github.com/s116821/ReMarkableBuddies/actions/runs/40437426851),
including the new input-handoff regressions. The collected ARM source
`6e62582d04c191b7a524167a58d35400449317e9` has the reviewed head's identical tree.
Controller SHA-256 is
`127e114a8b3762c17d22cb208a250357ee7a5c5715e63f557426e99ca5a45aba`;
observer SHA-256 is
`36ba20e327dcad583de2329b38055c94d77ed46ef7e4854b873953e36a313e01`.
The fresh isolated clean fixture passed 41 calls and both recovery checks, then
separately reviewed cleanup passed with real services unchanged.

Candidate `080c1914df7a447eb54ec609225f6640` was staged, independently reviewed,
and selected once after a fresh live inventory matched its original process,
group, policy, unit and 191-entry source inventory. Its candidate digest is
`3833471cb79b0bd365b1ef4a2ab75c651aaae55ce29cc3cc3011c9487f777456`.
All 36 execution/collection calls succeeded. The retained evidence verifies both
nonce-bound input-admission boundaries, launch admission, the authenticated SDK
Observe reply, child shutdown and independent stock-first restoration. The child
was reaped with no cleanup error and no pending mutation; source inventory and
unit files were preserved. Execution receipt SHA-256:
`d6a52f5921f58ed6ce627af2e11d69d53c58d68952e42be11fcc37134d5012f9`.

The actual reply was `Ok(Rejected(UnknownIdentity))`. This completes the question
of whether the resident runtime can launch, exchange one authenticated Observe
and return to stock under the diagnostic recovery controller. It does **not**
identify a Reader page, explain the refusal, establish visual/source continuity,
or qualify capture, insertion, writing or the installed Session. No refusal was
retried and no input/navigation was injected. The original minimal environment
also emitted a non-UTF-8 locale warning; the warning alone does not establish the
cause of UnknownIdentity.

Separately reviewed cleanup passed 18 calls, removed only the two diagnostic
definitions, and verified restored stock PID 14606 and Buddy PID 14675 unchanged.
Its receipt SHA-256 is
`9baef438026beafd50fb2849f51023e633f29f566fe256b4bcbbe6414f7b1412`.
Payloads, control records and failed earlier attempts remain preserved. This
candidate is spent; none of this evidence authorizes its replay.

Next implement and qualify the actual source capture path under the SDK's
[native capture contract](https://github.com/s116821/ReMarkableOpenSDK/blob/9804c66219750bf68a2159e51d1c02a4f705f51b/openspec/changes/integrate-resident-native-adapter/native-capture.md),
with full-order checks inside both native source callbacks and private image
ownership until final admission. Product activation must still reacquire source
and input correctly; the diagnostic Buddy-stop gap grants no request continuity.
