# Inspect current revisions of a selected memory fact

## Why
Global search discovers relevant facts but can suppress conflicted, expired or
deleted records. The companion needs a deliberate fresh inspection of one chosen
search key before broader memory management can be considered.

## What changes
- Add the same read-only single-fact action to browser/helper and Electron.
- Consume the published bounded inspect-stdin Key/raw-envelope contract.
- Preserve every admitted current head, including local concurrent heads and
  tombstones; retain selected whole-view refusal and reject unsupported raw views.
  Never infer a winner or a complete catalog.

## Scope
This is a paired central Docs/Manager increment. Main separately owns producer
change inspect-memory-fact-over-stdin. Its implementation, actual report evidence
and qualified delivery remain dependencies. No mutation, inventory, arbitrary
remote staging, service action, provider operation or tablet qualification follows.

Implementation checkpoint: accepted by precode review5582813325 and implemented
in paired Manager29. Full implementation reviews5583174872/5583175955 accepted
eeb8de5/a454aea. Captured producer corpus and local compatibility are verified;
current source hosted package gates pass and own canonical sync/archive is complete.
Producer delivery is verified at4fad168/1c736fa. Final composed review, normal
consumer merge and actual-main/publication observations remain external gates. This proposal is retained as historical motivation/scope.
