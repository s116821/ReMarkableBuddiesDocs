## Why

Installed Reader currently writes the legacy display block as the assistant's stored text. That mixes question, answer and source coordinates in a single role and hides the target from structured continuation history.

## What Changes

Store the interpreted question and assistant answer in their existing separate turns. Record the normalized selection in the original resident capture and expose it with the ordinary continuation image association.

## Scope

This increment covers installed Reader persistence and local continuation. It preserves legacy and frozen records and uses the existing verification and output settlement rules.
