## Why

Reader can recognize a circled or highlighted subject while preserving the separate handwritten question. The installed conversation page currently shows the question and answer without telling the reader which source Buddy used.

## What Changes

- Ask for a short selection description in the existing installed Reader proposal.
- Store a recognized description with its original resident capture and show one About line above the exchange when the installed renderer can fit it. Show a neutral uncertainty line when the proposal explicitly cannot identify the subject.
- Keep ordinary typed continuations tied to the original source without adding another About line.

## Capabilities

### Modified Capabilities

- `reader-analysis`: Separate a bounded optional subject from the handwritten question and answer.
- `conversation-context`: Retain the subject with the original resident source evidence.
- `reader-answer-pages`: Show the subject once in the original installed Reader exchange.

## Impact

Buddy uses its existing Reader provider passes, resident history transaction and installed conversation-page formatter. This scope covers Reader display and source history. The regional Writer flow and broader tablet acceptance remain tracked in the parent change.
