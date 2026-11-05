# Conservative legacy classification bridge: assessed precode contract

Main and the existing independent Sol reviewer accepted this five-file contract
delta on2026-10-12. Local implementationdbf8627 is independently reviewed in
[buddy-legacy-recognition-bridge-result.md](buddy-legacy-recognition-bridge-result.md);
capture provenance,
qualified recognition, adoption and native/installed Reader gates remain open.

This small local integration connects the existing three-value AnswerPageType
to the synthetic acquisition decision model. It performs no capture, SDK action,
Workflow call, Store access, target allocation or rendering. It neither changes
the existing classifier nor wires the installed Reader. Held8112 remains untouched.

Current classifier behavior is masked blank threshold0.998, optional cached
top150-pixel header threshold0.998, otherwise Invalid, including nonblank without
a header cache. Those legacy outcomes are classification facts only; they do not
prove relevant conversation ownership, Buddy absence or current native identity.

A pure function accepts a supplied SDK PageObservation, desired conversation UUID
and AnswerPageType, returning a modeled RecognitionWitness or unresolved reason.
Require explicit Synthetic origin, nonempty unique order and exactly one current
page membership. Derive the logical page from the observation and bind the full
opaque observation and desired conversation. Use an exhaustive mapping:

| Supplied legacy classification | Synthetic recognition |
| --- | --- |
| ExistingQA | LegacyBuddy |
| Blank | Blank |
| Invalid | Unknown |

Never map to RelevantBuddy, OrdinarySource or ConfirmedNonBuddy. A header match
cannot establish requested conversation relevance or a Store/native claim.
ExistingQA with missing association therefore requires adoption; blank/invalid
remain unresolved. Matching a supplied enum to an observation is modeled context,
not proof the classifier actually used that page's capture or that it was collected
now. Existing full opaque/witness/conversation guards remain necessary but do not
repair that provenance gap. Future qualified recognition remains separate.

The bridge accepts no image/Workflow/Platform/Store/effect callback and adds no
classifier algorithm, dependency upgrade, persistent format or registry. Existing
decision/continuity/acquisition behavior remains; a known relevant projection may
still return its independently modeled candidate, but the bridge itself cannot
issue reuse, insertion, binding, NativeCommitted or renderer authority.

Verify the three outcomes through actual public SDK mock current and successor
decision paths: with missing association, ExistingQA yields AdoptionRequired and
Blank/Invalid yield Unresolved, never inspection/insertion. Successor fixtures
obtain the ordinary source anchor separately and use an SDK-created Next receipt;
policy calls change no SDK state. Preserve foreign/stale observation and desired
conversation mismatch refusal, the existing22 SDK seam controls and the ordinary
non-mock library build. Do not fabricate private SDK observations merely to test
unconstructible invalid states.

Source basis: current exact AnswerPageType/classifier source, pinned public SDK
and reviewed synthetic decision model. No native, capture provenance, relevant
association, adoption or installed Reader qualification is claimed.
