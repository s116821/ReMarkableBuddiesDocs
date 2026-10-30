# Actual-main provider transport qualification

## Why
The accepted asynchronous transport is now on actual Buddy main4c90b5a, but its existing Linux TLS/root/proxy and response-limit qualification remains only on original stacked PR44/45. Deliver that already completed two-file suite independently, preserving original branches/contracts/results. No runtime behavior or dependency changes.

## Scope
Import only exact tests/provider_transport.rs and tests/fixtures/provider_transport_server.py from accepted22586a7d3bafa1d94cae7911b5a5bf4c09357e27. Preserve all existing main files, privacy parser, graph and SDK boundary. Publish this central contract BEFORE source import. Two original accepted capabilities are one coherent suite, not whole REM40, real-provider or native qualification.
