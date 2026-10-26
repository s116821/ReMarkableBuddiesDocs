# Pre-implementation state

This is proposed behavior only. No source/API implementation, new provider/model call, device action, deployment or qualification is claimed. Source016d78a and Docs mainb66d1b9 contain the separately accepted Reader delivery. Original Reader, native, selected, pending feedback and held failed/spent handwriting work remain preserved.

Current source inspection finds a static catalog with an explicit caller-validation/pending-persistence boundary, ordinary Ledger current-head decoding and existing Store/mode snapshots. The proposed receiver uses stored associated facts rather than inventing another pending record domain. Its limitation is explicit: it does not establish unpresented state or retain a failure before any durable fact exists.

Source basis: current REM-40 description/all32 comments, delivered canonical feedback/layout/ledger contracts and direct current source inspection. The optional advertised Linear field-notes operation returned ToolNotFound; no external field notes were assumed. Scope and implementation remain pending independent review.
