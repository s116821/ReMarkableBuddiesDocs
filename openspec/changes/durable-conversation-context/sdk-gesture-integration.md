# SDK gesture mapping consumed by Reader

This is the existing SDK task3.6 / Reader backend integration requirement. SDK
owns physical model/orientation mapping; this change owns its actual Reader
consumer. Existing logical requests and mock outcomes are reused. Native SDK
Platform navigation remains Unsupported until its observation/guard adapter is
qualified. No new native module, service change or menu path follows.

The SDK produces a pure virtual trajectory only for explicit RM2 Portrait;
unknown model/orientation and other device/orientation profiles refuse. Preserve
the existing Reader arithmetic: Next700-to100 and Previous100-to700 at y512,
50ms initial hold and15 moves at10ms intervals. Reader remains sole event emitter
and always attempts release after an ordinary gesture error. A plan or echo is
neither a native receipt nor page authority; process crash release is not implied.

RealNavigation captures explicit customZoomOrientation from the existing bounded
document configuration observation, along with exact document/page/visit/order.
Missing or unrecognized settings remain Unknown. This is physical gesture
configuration, never proof of the active native view. Require unchanged bracketed
source metadata, recognized portrait source chrome, retained request/input guards
and explicit Portrait before submitting the planned path. Recheck configuration
through existing subsequent destination observations; drift refuses completion.
Normalized image dimensions alone do not select an orientation. SDK planning
also checks Touch's actual detected model; Unknown cannot default to RM2.

Preserve existing one-gesture submission and bounded composite destination
verification. Do not mint SDK PageObservation, adopt historical input, relax
selected ReaderContext or claim native authority from document configuration.
Unverified fallback lacks an admitted profile/orientation and refuses before
input. Development diagnostic swipe calls require explicit orientation rather
than silently choosing portrait; they remain separate from product behavior.

Focused verification exercises exact portrait paths/direction, unsupported model
and orientation, missing/changed document configuration before input and during
completion, ordinary error release and existing actual NavigationIo behavior.
Do not repeat the complete navigation/mock/native matrix. Preserve all earlier
verification and blocked interpretation WIP separately. Any live gesture is a
separate Main-owned announced current-state test; none follows from compilation.

Source basis: SDK cb1d9c7 logical-navigation contract/task3.6 and navigation.rs;
accepted Buddy3fb580c existing xochitl_integration, navigation_completion and
native_page source. Document configuration is explicitly not native authority.

## Separate committed consumer delivery

The clean consumer successor starts at Rust
`1f4b29134532f720dd4aba34a14549b295861ad7`, paired with Docs
`bea05aba7191fd22ca1ad7bbc806e9d50a971140`. It pins the reviewed SDK
`5c0bc303bb9b22e8e01bce9b2bd2a7fe47c8010e` rather than adopting later SDK work.
The protected active working files remain byte-identical and unstaged.

Copy only the mapping consumer changes: dependency pin/lock, Touch model
accessor, planned-path emitter, bounded document orientation parsing,
NavigationIo orientation forwarding/admission/drift checks, and removal of the
unverified backend fallback. Hardware diagnostic navigation receives explicit
orientation arguments; its separate pen-stroke validation and path changes are
excluded. No gesture tool, native payload, service or installation is added.

The existing six focused consumer checks were executed against protected working
bytes, not this new committed successor. Verify the successor's affected source
and strict lint, then use hosted Linux/ARM checks for platform compilation. Keep
native operation, process-crash release, landscape/other-device support and
current-page authority explicitly unqualified. This delivery does not change
REM53 personalization implementation or its public parent.
