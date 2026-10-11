## ADDED Requirements

### Requirement: Experimental capture has exact process provenance
The experimental RM2 capture path SHALL bind an explicit boot ID, PID and process start identity and SHALL refuse identity or mapping/header changes before accepting pixels. It SHALL NOT rediscover a different process by name after binding.

#### Scenario: Bound process is replaced
- **WHEN** the PID start identity or boot differs at any capture boundary
- **THEN** capture refuses and publishes no image or cached output

### Requirement: Ambiguous allocation discovery preserves bounded evidence
RM2 allocation discovery SHALL retain bounded selected-identity, map and matched raw-header evidence. Zero or multiple heuristic matches, malformed evidence or scan-cap exhaustion SHALL refuse capture; no ordering, cached address or image resemblance SHALL select a match.

#### Scenario: Two allocations have the expected header
- **WHEN** two matching allocation headers are discovered
- **THEN** bounded match evidence is retained and no pixels are accepted without separately qualified native backing attribution

#### Scenario: Discovery reaches a bound
- **WHEN** the maps, scan or evidence cap is exceeded
- **THEN** discovery is explicitly incomplete and refuses rather than treating a partial scan as unique
