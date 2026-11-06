# Composed selected Reader memory publication

## Why

The implemented Reader and selected memory consumer share document gates. They
must publish through one ordered set rather than reacquire a participating gate
or treat a stale/foreign view as current. The implementation is delivered through
[Buddy33](https://github.com/s116821/ReMarkableBuddies/pull/33), while the unique
contract/evidence in [Docs22](https://github.com/s116821/ReMarkableBuddiesDocs/pull/22)
still needs its own finite lifecycle. [Buddy37](https://github.com/s116821/ReMarkableBuddies/pull/37)
is retained as superseded source provenance, not a second implementation to merge.

## What Changes

- Preserve the original precode, source/result chronology and bounded panic
  witness without rewriting old failures or promoting their evidence scope.
- Synchronize the delivered composed-publication requirement and its shared-key
  and resident historical-evidence scenarios into canonical Reader analysis.
- Correct only the obsolete unconditional configured-memory refusal in the
  existing selected-draft contract: unsupported/foreign providers still refuse,
  compatible selected memory uses sealed joined publication, and native effects
  remain unavailable.
- Archive this completed receiver slice in the same existing Docs22 delivery,
  leaving `durable-conversation-context` and broader issue gates active.

## Impact and boundary

Docs only. Source550805a is contained in accepted52595dc; delivered squashf6af5d1
has the exact52595dc tree. No source edit/build, new model call, tablet operation,
new persistence engine or blanket native/live/lifecycle qualification is added.
Root owns independent final Docs review/checks, publication and normal squash.
