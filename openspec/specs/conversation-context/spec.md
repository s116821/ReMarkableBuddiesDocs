# conversation-context

## Purpose

Define the implemented selected historical context, capture-byte retrieval and read-only Buddy binding inspection APIs. Historical records and candidates do not authorize native effects. Controlled Reader preparation remains recording-test-only; no production selected-source adapter or bootstrap is supplied by these APIs.

## Requirements

### Requirement: Pinned selected conversation context
Selected conversation context SHALL derive current turns and source records only
from one validated selected causal snapshot, excluding retained and all-history
losing branches. It SHALL retain existing complete chronology and explicit budget
refusals and SHALL NOT grant restored/native effect authority.

#### Scenario: Replacement during context assembly
- WHEN a caller captures selected context and a replacement occurs during token counting
- THEN the context preserves the captured winner's exact records and media coverage without resolving the new head, holding admission across the callback or granting current effect authority.

#### Scenario: Incomplete or over-budget selected history
- WHEN selected allocated chronology is incomplete or explicit context limits are exceeded
- THEN context refuses instead of dropping, summarizing, rewriting or substituting retained turns.


### Requirement: Pinned selected capture bytes
Selected capture retrieval SHALL preserve existing SDK historical, legacy and
development evidence classification and exact acquisition-parent/provider bytes
from one validated current selected causal snapshot. It SHALL require complete
live conversation chronology and current source links, use only selected included
media and existing image/receipt validation, and SHALL NOT reconstruct native
qualification or effect authority.

#### Scenario: Losing capture or retained omitted bytes
- **WHEN** an all-history losing capture shares the selected capture ID, or selected media is deliberately omitted while retained bytes still exist
- **THEN** retrieval uses only the selected current capture and its included media, and refuses omitted required capture bytes rather than substituting the losing or retained copy.

#### Scenario: Exact historical variants and stale selection
- **WHEN** existing selected legacy, SDK historical or development capture bytes are retrieved
- **THEN** acquisition parents, completion correspondence and provider image order remain exact under the existing variant validators; stale tokens and inconsistent image facts refuse without recapture, publication, provider calls or native authority.


#### Scenario: Pending publication cannot promote omitted winner media
- **WHEN** a fresh pending intent requests media omitted from the selected winner while identical retained bytes remain available
- **THEN** public pending publication and controlled Reader preparation refuse before their live source or plan verification, leave the selection and receipt state unchanged, and cannot promote retained bytes into selected inclusion; exact historical retry remains evidence only.

### Requirement: Current selected Buddy binding inspection
Buddy binding inspection SHALL use the existing token-checked selected admission,
deterministic Ledger binding key and validated selected causal closure. A candidate
SHALL require exact current live Root and Binding heads linked to the requested
conversation/document/page, complete relevant chronology and consistent ownership.
It SHALL retain exact historical receipt and selection/revision provenance without
reconstructing native or effect authority. The actual Workflow consumer SHALL
bind the result to complete matching SDK observations and SHALL perform no device,
provider or publication actions.

#### Scenario: Current binding across Store reopen
- **WHEN** the actual Workflow consumer inspects a current linked binding after the real Store is reopened with the same accepted selection
- **THEN** it returns the exact selected receipt, root/binding revisions, token and supplied SDK observation as historical candidate evidence, with zero successor inspection, navigation, rendering or publication.

#### Scenario: Omitted heads and historical competitors
- **WHEN** selected binding or root heads are absent, deleted, foreign, unlinked or bound elsewhere while ancestors, retained losers or ordinary Store heads contain a matching association
- **THEN** inspection remains explicitly unresolved or refuses, never substitutes that historical association and never interprets absence from the selected closure as an unclaimed or non-Buddy page.

#### Scenario: Invalid closure or changed selection and observation
- **WHEN** the selected closure is forked, ownership or chronology is inconsistent, the accepted selection is stale or foreign, or complete SDK observation scope/visit/input/order/current-page facts differ
- **THEN** the consumer refuses before any candidate or device action; matching UUIDs, origin strings and saved timestamps do not waive the mismatch or qualify native reuse.
