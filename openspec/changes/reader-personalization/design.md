# Design

## Existing behavior and source basis

The actual Reader analyzes source images, independently verifies the handwritten question, records the interpretation, optionally regenerates an answer using subject memory and publishes through existing ownership guards. The current memory receiving function refuses empty context, so attaching preferences only to successful retrieval would omit ordinary requests without memory. REM-53 description and all ten accessible comments were read chronologically; Rust PR39's accepted configuration snapshot is reused.

## Decisions

1. Capture the validated immutable preference from the configuration loaded at startup. A disk maintenance save continues to report restart-required; this increment does not claim a running reload, controlled restart or Manager activation receipt.
2. Keep preference out of initial image analysis and independent transcription. Snapshot it once for a prepared request and assemble it once in the later answer generation. Persist the verified question exactly as before.
3. Use a receiving answer context shared with existing subject memory. Disabled or empty memory does not prevent an enabled preference from applying; configured unavailable/incomplete memory retains existing refusal behavior. Usable memory plus preference produces one answer regeneration, not two serial rewrites.
4. Encode preference as a separate configuration field with explicit precedence: current explicit request and fixed source/operation/output contracts outrank preference. Never invent transcript turns, change source association or grant operations. Preserve exact multiline Unicode text inside the context, without routine logging.
5. Disabled or empty preference follows the previous provider sequence and default behavior. Validate configuration through the existing schema and bounds; do not duplicate them.

## Verification and limits

Offline workflow tests must inspect outgoing requests, persisted question and call counts for unset, enabled, disabled, empty, memory-empty, memory-present and disagreement cases. Exercise multiline Unicode without echoing user configuration into diagnostic logs. Representative live provider evidence checks actual precedence and source-grounded answers; deterministic framing tests alone cannot establish semantic obedience. Simulator evidence does not prove hardware, Writer support or live runtime activation. Canonical sync and archive wait successful scoped implementation, checks and independent review.
