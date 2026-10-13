# Why
The accepted Manager ZIP consumer cannot verify Buddy APKs. Main has supplied an actual historical two-target signed test fixture; an independent host consumer must check those original bytes with the existing pinned upstream verifier.

# What Changes
Add an opt-in developer observation harness for the exact six public handoff files, a separately communicated manifest digest and DER-SPKI digest, and an exact-source apk build receipt. Verify original package/index signatures and payload integrity, compare bounded metadata readbacks, and exercise wrong pin/key and altered-byte refusals. Preserve PR13 and prior offline qualification.

# Capabilities
## New Capabilities
- `manager-signed-fixture-verification`: public-key-only actual historical fixture observation.
## Modified Capabilities
None.

# Impact
Manager test orchestration and documentation only. No renderer, transport, release, production trust, signing, APK producer, installation or device operation. Central requirements remain here; paired implementation starts from accepted Manager46cc and Docsde00.
