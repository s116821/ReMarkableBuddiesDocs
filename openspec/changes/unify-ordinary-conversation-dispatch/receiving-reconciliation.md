# Delivered receiving baseline reconciliation

The existing Buddy124/Docs135 pair resumes on November5 after delivery of
Buddy33 f6af5d1 and Docs15 3bfecf70. Existing reviewed input174d0fb and
Docs0fbaea3 remain preserved. The precode reconciliation update is Docs8d1164c;
the normal Docs baseline merge is2bef2d2, retaining both parents. This is an
integration successor, not a transferred source/CI/live acceptance receipt.

Only two source files conflicted in the normal delivered-main merge:

- `workflow/mod.rs` retains the complete delivered resident source/health wait
  and begin/finish handling. Shared ordinary idle admission detects an installed
  resident source, validates Reader dispatch and delegates to that same owner;
  it never routes resident acquisition through legacy device waiting/preparation.
  Nonresident event batches retain the existing centralized trigger and history
  invalidation behavior. This is source composition, not new tablet evidence.
- `writer/mod.rs` composes the explicit ordinary-memory public entry and the
  routed exact-root/image receiver through one private owner path. The public
  optional-memory caller retains its supplied Provider; existing routed callers
  retain no memory until explicitly adopted by a separate reviewed contract.
  No silent opt-in, selected fallback, second Store or nested Writer owner is
  introduced. Both use the delivered memory admission/snapshot and finish logic.

Current selected Reader/joined publication, resident rendering and default SDK
pin integrate from delivered main, without copying Root's unfinished REM26 code.
Historical image associations and notebook-reducer digest binding remain in the
existing dispatch delta. Root still owns the shared Cargo target: only formatting
and source diff checks have run on this reconciliation. Compilation, affected
combined/Writer/Reader regression tests, hosted validation and independent
integration review remain pending. Earlier green results remain attributed to
174d0fb and their original inputs. No provider/key read or tablet contact occurred.

The active change stays open for its explicitly unfinished native composer,
gesture/page/effect and genuine aggregate-apply requirements. Root owns final
delivery scope and review; this reconciliation does not authorize silent merge
or whole-issue completion.
