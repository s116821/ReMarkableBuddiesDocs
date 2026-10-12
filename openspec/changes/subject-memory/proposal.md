# Provider-independent subject memory

REM-24 requires useful optional subject/user context across Reader and Writer,
with offline local persistence, explicit provenance and bounded relevant retrieval.
Conversation transcripts, document research, handwriting learning and explicit
personalization remain separate domains. Existing generic SubjectMemory envelopes
are infrastructure, not an implemented memory capability.

Implement a typed local domain over the completed REM-36 Store, replaceable
store/update/query/inspect/forget operations, and a bounded receiving-buddy context
interface. Add actual Reader integration after independent transcription checking;
disabled memory preserves its existing calls and behavior. Writer may consume the
same interface later and remains usable without memory. No answering-provider,
agent runtime, vector database or network service is required for local operations.

This delivery depends on Rust parent `7b207ec8a42548c12960699854107236eb2bbd7f`
([PR 30](https://github.com/s116821/ReMarkableBuddies/pull/30)) and Docs parent
`60a8e0e7ec6ec181ed36652b9b7e33d222086a6c`
([PR 6](https://github.com/s116821/ReMarkableBuddiesDocs/pull/6)) for bounded
Store snapshots and typed conversation/source provenance. It excludes the
unrelated REM-42 inspector increment. Protected Reader/device WIP is preserved.

REM-52 owns generic shared/isolated sync and selected membership; coordinate
logical keys and reuse its primitives. Manager inspect/forget UI, full Writer
integration, selected cross-device policy and device/release acceptance remain
part of the owning full scope, not claims from local tests. No native packet,
device query/write, firmware, account or service operation follows from this work.

The continuing selected receiving increment adopts the already-present reviewed
REM-52 primitives, adds strict catalog/aggregate membership and connects actual
Reader/maintenance consumption. See [selected membership](selected-membership.md)
for the frozen domain contract and explicit cumulative-reading dependency. It
does not replace the default local adapter or qualify live shared/native work.
