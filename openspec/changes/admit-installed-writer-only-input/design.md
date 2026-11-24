# Installed Writer input

Use the same verified output profile and supervised service as the combined app. A stationary three-finger hold opens or reuses a blank page after all fingers lift. It uses the existing page owner and makes no model request.

At release, select only a refinement already queued in the current service activation. Buddy first publishes the complete request under its queue lock, then records the boot-clock second by which it was visible. That second must precede the timestamp of the kernel touch frame that reported the release, on the same clock. A delayed poll or a stalled write cannot attach a new request to an earlier gesture. If the input driver cannot supply that clock, the ordinary Reader and blank-start gestures remain available. An older or interrupted slot without a publication time stays untouched until expiry. A three-second hold started after successful queueing orders the two events.

Inspect the selected request for the captured document and page. Claim it after validating the current draft, conversation and page binding, immediately before the Writer operation. Recheck the complete slot and its expiry while holding the queue lock. A different page, stale draft or replaced request leaves the slot available. An unqueued corner hold in Writer-only mode leaves the service listening. Reader-only mode skips the Writer queue.

In combined mode, a valid Reader corner hold still opens Reader if the optional Writer queue cannot be read and the service remains healthy. In Writer-only mode, that case returns to listening. Keep Reader-only input, history and cancellation behavior. Hardware acceptance uses the installed service, real finger gestures and visible page results.
