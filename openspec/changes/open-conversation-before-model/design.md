## Context

The current service captures the source, routes the request, verifies the interpreted question and generates an answer before it decides where to put the answer. A successful insertion can therefore look like a missed gesture for much of the request. A write to a notebook requires the correct destination. Opening the conversation requires the source and its page association, both of which are available earlier.

## Decisions

On submission, retain the source page identity and the capture from which the request will be read. Start opening the conversation as soon as those are available. Reuse the normal placement logic for new and existing pages. Carry the selected destination forward with the same request. The source stays the input to the model after the screen changes, including when Reader and Writer share the gesture and routing requires a model call.

Opening the page is a separate user-visible effect from publishing an answer. Check response formatting, text fit, and output destination when publishing the reply. If the person has left the conversation, keep its outcome for that conversation. An unrelated page must keep its contents. When a reply cannot be completed or displayed in full, use the existing fixed user-facing failure categories. Group equivalent failures where they lead to the same next step for the user. Keep provider payloads, request identifiers and diagnostics in the service log.

The earlier text-fit change made a fully formatted answer a prerequisite for page creation. For ordinary handwritten submissions, this proposal supersedes that ordering and preserves the text-fit check at the actual write. A response that cannot fit still belongs to the conversation the user has already opened. [Earlier text-fit change](https://github.com/s116821/ReMarkableBuddies/pull/187)

Use the page operation's completion and the current destination at the point of writing. Reuse observations that still establish the needed facts. An additional full-page capture or service query on the ordinary path needs an identifiable state change or new question to answer. This change introduces no workflow timer. Pending feedback, when supported, belongs on the Buddy page and may update when the request state changes.

## Verification

Hold a controlled provider response outstanding while observing the ordinary service. Confirm the destination becomes current while the provider is still pending. Then release a success or a failure and check the resulting conversation. Cover both a new conversation and an existing adjacent page. Use the actual installed tablet service to record gesture release, visible page opening, provider completion and visible reply separately. Record what the screen showed as well as the timing. A page saved on disk alone cannot establish when it became visible.
