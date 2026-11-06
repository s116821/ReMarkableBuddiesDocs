# Observe the current resident test-key package fixture

## Why
The delivered Manager offline observer accepts only the historical legacy-no-sdk
six-file fixture, ordinary three-file payload and APKs at most32MiB. The accepted
new producer fixture contains35,582,576/36,231,072-byte APKs, a ten-file resident
ARMv7 payload and an SDK-bound ordinary AArch64 payload. The historical guard
correctly refuses this new shape; producer-side observation is not Manager proof.

## What changes
Extend only the existing opt-in public-key-only real_fixture.py observer, focused
controls and guide. Preserve the historical default/schema/caps unchanged. Add a
separately selected resident fixture handoff with external manifest pin and finite
reviewed metadata/layout constraints. Keep update/install authority false and all
Root-owned recovery/Stop drafts and normal Manager UI/ZIP behavior unchanged.

## Capabilities
- Modified: manager-signed-fixture-verification, for the explicit current fixture.

Actual tool execution and consumer observation remain separately selected; this
source change neither creates a production trust policy nor reruns packaging.
