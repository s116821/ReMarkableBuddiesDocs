# Explicit conditional forget of one prepared memory fact

## Why
The delivered companions inspect one selected fact but do not prepare or confirm a
conditional removal. Read results alone do not authorize a mutation, and a lost
reply cannot safely be retried as a new request.

## What changes
- Propose one explicit supported-value preparation/confirmation in both hosts.
- Retain original conditional intent privately in one live-host memory slot with
  an exact display reference, single-use claim and conservative uncertainty.
- Separate historical receipt acknowledgement from deliberately inspecting current
  data, and document the initial lack of durable restart recovery.

## Scope and dependency
This is consumer precode, not an implemented API. Main owns the producer/Store/
mode/receipt change prepare-conditional-memory-forget and its corrected contract
at64ff69baf2e066f203eadd587cb2d3864173b1a6. Corrected producer and consumer reviews,
actual producer compatibility evidence and full paired lifecycle are gates before
consumer delivery. No generic editor/purge, provider/service, remote staging,
database, durable journal or tablet qualification is added. Prior inspection29/67
is delivered and remains unchanged; its automatic publication is separately observed.
