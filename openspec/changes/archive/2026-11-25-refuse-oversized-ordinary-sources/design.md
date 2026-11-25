## Decision

Check the length of the complete `ReaderFacts` order returned by the guarded Observe. The installed profile uses a pinned `CaptureSource` codec and capture validator that accept at most 17 pages. End the current request through ordinary finalization when the order exceeds that bound. Finalization retires the request connection, releases its guard, and leaves the runtime owned. The next distinct gesture reconnects and observes its own source.

Keep unexpected protocol errors on the existing integrity path. Keep the separate insertion limit of 16 existing pages, the full source order, and the existing capture, observation, qualification, deadline and mutation checks.

## Verification

The installed-service fixture starts on an 18-page source. One case models the shipped adapter's observation refusal. Another returns a complete order admitted by the observation codec. Both check refusal before capture and zero model or page effects, then change to a one-page notebook and submit a distinct release through the same owned runtime. A normal response on the second notebook verifies request recovery.
