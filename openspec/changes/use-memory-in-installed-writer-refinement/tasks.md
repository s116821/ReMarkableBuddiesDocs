## Implementation

- [x] Use the admitted local memory provider for a queued refinement of the current draft. Retain Writer ownership through publication and placement.
- [x] Preserve disabled and empty behavior, exclude development-plan requests, and check incompatible memory before claiming an installed request.
- [x] Cover the installed refinement in [Buddy CI](https://github.com/s116821/ReMarkableBuddies/actions/runs/45394849140/job/138447893135) and validate the subject-memory spec. A mismatched store leaves the request available. With the correct store, Writer uses the same draft and source and passes the saved fact to the model once.

## Tablet verification

- [ ] On a tablet running this change, refine the current draft using a distinctive fact saved for that document. Leave the fact out of the draft and refinement prompt, then check that the revised note on screen uses it in the same conversation.
