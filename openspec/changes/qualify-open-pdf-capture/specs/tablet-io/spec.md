## ADDED Requirements

### Requirement: Experimental capture has exact process provenance
The experimental RM2 capture path SHALL bind an explicit boot ID, PID and process start identity and SHALL refuse identity or mapping/header changes before accepting pixels. It SHALL NOT rediscover a different process by name after binding.

#### Scenario: Bound process is replaced
- **WHEN** the PID start identity or boot differs at any capture boundary
- **THEN** capture refuses and publishes no image or cached output

### Requirement: Ambiguous allocation discovery preserves bounded evidence
RM2 allocation discovery SHALL retain bounded selected-identity, map and matched raw-header evidence. Without separately qualified native backing attribution, zero or multiple heuristic matches SHALL refuse capture. Malformed evidence or scan-cap exhaustion SHALL always refuse capture; no ordering, cached address or image resemblance SHALL select a match.

#### Scenario: Two allocations have the expected header
- **WHEN** two matching allocation headers are discovered
- **THEN** bounded match evidence is retained and no pixels are accepted without separately qualified native backing attribution

#### Scenario: Discovery reaches a bound
- **WHEN** the maps, scan or evidence cap is exceeded
- **THEN** discovery is explicitly incomplete and refuses rather than treating a partial scan as unique

### Requirement: Experimental native-backed acquisition hands off owned bytes
A separately selected native-backed experimental producer SHALL acquire one exact RGB32 portrait plane through one held process memory handle between fresh native tuple/header and process/map checks. Only a complete bound frame with producer exit zero SHALL be accepted for pure native/overview PNG conversion. The converter SHALL NOT reopen process memory or infer native authority from conversion alone. Failed, short, extra, stale or mismatched framing SHALL publish no accepted image.

#### Scenario: Producer closes successfully
- **WHEN** exact selected nonce/process/boot, supported layout, both native tuples/headers, full plane and terminal framing agree and the producer exits zero
- **THEN** both PNG views derive from those same owned bytes, preserving sampled lifetime/coherence limits

#### Scenario: Closing evidence or frame is incomplete
- **WHEN** producer exit, framing, selected identity, tuple/header equality, layout or exact byte length fails
- **THEN** conversion/admission refuses without using prior cached pixels or an alternate allocation
