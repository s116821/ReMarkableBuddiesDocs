# Verified source basis and constraints

Current canonical requirements are owned by REM-42 (both companions, owned
categories, sizes and no Buddy service API) and REM-23 (generation4 accounting
remains required after the bounded notebook merge). The public requirements below capture the relevant existing contract and
compatibility constraints. Immutable source and canonical specifications provide
the contributor-facing basis; private tracking is not a prerequisite.

- [Merged producer6fd4082](https://github.com/s116821/ReMarkableBuddies/tree/6fd4082c6401bab698a5c685bf0735b12f91340c)
  has the reviewed3e6618c tree. src/storage/inspection.rs recognizes1..3, report1/2;
  current-generation evidence clamps to1..3. It lacks contract-v3.json and
  notebook-feature.json accounting, and its feedback-envelope branch requires
  format==3. A format-enum edit alone is insufficient.
- src/storage/types.rs bounds inspection input at4096items,1MiB records and8MiB
  metadata. The existing FileUsage/DomainUsage aggregate sizes are not allocated
  bytes or logical liveness. Observed metadata is separate from retained media.
- src/storage/notebook_generation.rs and feedback_generation.rs define the actual
  feature4/feedback3composition. validate_ready is current-generation-specific;
  it must not be applied blindly to every retained4generation. Preparation,
  publication/recovery and records validators are not observer startup APIs.
- src/conversation/mod.rs and notebook.rs define Value-only Source3 and
  Conversation3; archived bytes are referenced media. Invisible plans/stages
  still need accounting and must not be misrepresented as visible turns/calls.
- [Managerb6ca2305](https://github.com/s116821/ReMarkableBuddiesManager/tree/b6ca230515f4d70f95fad066a9190430778c9a69)
  host/owned-report.mjs and its types have distinct exact report1/2 branches;
  report2formats are1/2/3 and complete requires3/six domains. src/owned-data.ts
  checks connection/boot/epoch and currently uses inspectOwned(). Existing
  accounting UI is not report3 support. Current handwriting work stays with its
  owner; these facts must be refreshed before Manager implementation.

Implementation source scope must be pinned and independently reviewed against the
then-current revisions. This assessment changes no storage, envelope/domain,
recovery, Writer or Manager code. The existing reports and public/manual paths
remain a compatibility obligation. The exact consumer base must be refreshed
before its implementation; the pinned Manager baseline is evidence for existing
contracts, not a claim about a later feature candidate.

The proposed selector/counter representation/consumer branch are design choices,
not sourced existing capabilities. Completion requires actual source and both-host
qualification; precode schema/vector checks are not executed product evidence.
