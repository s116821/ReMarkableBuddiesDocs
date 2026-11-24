## Why

Touch activity during ordinary boot can end Buddy startup while the activation slot is still unused. Users then need to restart Buddy before Reader listens.

## What changes

Wait for idle input during read-only ordinary activation preparation within the current startup deadline and service watchdog. Keep the existing one-way boundary at activation publication and preserve request cancellation and input integrity handling.

## Impact

Ordinary installed Reader startup and its operational logs.
