# Notebook limits on the installed RM2 service

The signed RM2 profile for reMarkable OS 3.28.0.172 has two distinct limits.
Page counts include existing Buddy pages.

| Operation | Existing pages | Other requirements |
| --- | --- | --- |
| Observe and capture a source page | Up to 17 | The active source and the full page order must qualify before and after capture. |
| Open a bound current or adjacent Buddy page | Up to 17 | The association and live destination must qualify. Page count stays the same. |
| Insert a new adjacent Buddy page | Up to 16 | Buddy must qualify the insertion point, preserve existing pages, and verify the resulting order and destination. |

For a notebook with 17 pages and no eligible Buddy page, use a smaller notebook
for a new conversation. For 18 or more pages, the installed adapter refuses
source observation. Switch to a supported notebook and perform a new hold to
submit. Buddy leaves the oversized request's page untouched.

The OpenSDK observation wire format can represent 2,048 page IDs. The signed
native adapter qualifies orders up to 17 pages, and `CaptureSource` independently
enforces 17 in the SDK codec and capture validator. Visual-only capture carries
pixels without the correlated document, page and complete order required by the
ordinary gesture. The generic SDK `Platform::capture` returns an unsupported
result for its default native platform. [Native observation and capture](https://github.com/s116821/ReMarkableOpenSDK/blob/a0c6480be6785480c2e0da76a3c06697a18efae4/native/rm2_3_28_0_172/read_only_backend.h#L64-L83) · [Native order limit](https://github.com/s116821/ReMarkableOpenSDK/blob/a0c6480be6785480c2e0da76a3c06697a18efae4/native/rm2_3_28_0_172/order_observation.h#L33-L39) · [SDK capture contract](https://github.com/s116821/ReMarkableOpenSDK/blob/a0c6480be6785480c2e0da76a3c06697a18efae4/src/native_adapter/capture.rs#L24-L38) · [Generic SDK capture](https://github.com/s116821/ReMarkableOpenSDK/blob/a0c6480be6785480c2e0da76a3c06697a18efae4/src/lib.rs#L252-L255)

Larger ordinary submissions depend on an SDK release and a matching qualified
native adapter profile that can observe and capture the complete larger order.
Reusing or inserting a Buddy page additionally requires qualified selection
and mutation at that size. Buddy can then adopt the compatible SDK and profile
and verify the ordinary gesture end to end.
