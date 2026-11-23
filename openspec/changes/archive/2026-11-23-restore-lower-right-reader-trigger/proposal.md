# Restore the lower-right Reader trigger

## Why

The stock toolbar can intercept a hold in the lower-left corner. Reader should start from the lower-right on a tablet using default settings.

## What changes

- Use the lower-right corner for a one-finger Reader hold when no corner is configured.
- Use the same default in gesture simulations and document it in the user guide. Existing saved and command-line corner choices continue to take precedence.

## Impact

- Affected specification: `platform-runtime`.
- Affected implementation: Buddy configuration, simulator gesture fixtures and user documentation.
