## Why

During October 15 Windows USB qualification the user reported that the tablet connection widget repeatedly showing a read/check state made the app feel busy and caused anxiety. They explicitly requested subtle or invisible background connection attempts. Physical cable checks are already recorded; this presentation repair does not request another cable cycle.

## What Changes

- Keep the last successfully verified observation and its timestamp visible while an automatic refresh is pending.
- Keep initial and user-requested reads visibly pending.
- Preserve immediate clearing on an actual failed result, changed connection/boot identity, explicit disconnect and cancellation; late results cannot restore cleared state.

## Scope

REM-41 shared Angular connection controller and focused deterministic controls, used by browser/helper and Electron. No transport, interval, authentication, identity, host, release workflow or installation change. This does not complete Windows qualification or REM-41.
