## Why

A fresh lifecycle-only Qt shutdown diagnostic needs a recovery boundary independent of host connectivity. Stock failure dependencies and restart policy must be temporarily suppressed before the first stock stop; candidate failure evidence must survive restoration. Existing facts/input operators do not provide this exact ordering and one absolute recovery budget.

## What Changes

Add source-only Buddy operator packet preparation, an owned transient failure guard, and an independent singleton actor for one diagnostic activation and one candidate stop/restoration. Coordinate the SDK scalar trace contract without invoking facts, getters, input or forced rendering. Preserve old packets and spent nonces.

## Capabilities

### New Capabilities
- `native-shutdown-recovery-guard`: Bounded one-attempt development recovery choreography.

### Modified Capabilities
None. This does not change product/native page behavior.

## Impact

Buddy experimental tooling only; SDK owns its lifecycle recorder and separate source contract. Main alone selects a fresh packet/nonce, reviews exact artifacts and operates the tablet with advance notice. No device action follows from source/fixture results. Main coordinates review and persistence; native diagnostics are not production qualification.
