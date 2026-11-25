## Why

The installed Buddy can refine an existing draft, but it omits the subject memory already configured for the service. A refinement submitted through the ordinary conversation receiver can use that same memory today.

## What changes

Pass the admitted local memory provider to Writer when a physical request selects the current draft on the tablet. Reuse the existing bounded retrieval and draft publication path. Preserve the behavior of a disabled or empty memory store and of explicitly staged development requests.

## Capabilities

- Modified capability: `subject-memory`.

## Impact

Changes the installed Buddy refinement receiver. No new service, configuration, network request, export destination or Manager control is needed.
