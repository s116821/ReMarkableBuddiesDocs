## Why
REM-40's measured provider wait cancellation remains blocked by scoped HTTP worker joining. Preserve a deterministic actual local-provider readiness reproduction before a runtime repair.

## What Changes
Add owned loopback barrier fixture and explicit cancellation witness/return deadline. No production transport/domain/native changes in the baseline. Runtime repair requires exact file ownership and maintained cancellable transport review; source/code/qualification remain unfinished until the original correctness control passes.
