# Preserve release-note strings at the maintained Action boundary

Manager's actual main run 38711594306 passed checks, build, both retained-artifact
integrations, official tagging, draft uploads and complete-byte verification, then
failed before final PATCH. The maintained request Action interprets each input as
YAML; raw multiline completion notes are not a valid scalar document. The draft
and original failure remain preserved. Buddy shares the same affected invocation.

Encode only the final notes input with GitHub's maintained `toJSON` expression,
and exercise the actual pinned Action with representative multiline notes. Keep
all semantic, tag, artifact, draft-ID, permission and recovery guards unchanged.
No manual tag/release mutation, older-source substitution or private coordinator.

This is a focused follow-up to completed ordered-ci-release, not a new release
engine or a claim that a frozen failed workflow can adopt a later code fix.
