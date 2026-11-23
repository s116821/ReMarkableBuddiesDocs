# Capacities REST OAuth registration draft

This draft is for maintainer review. The production registry remains unconfigured while registration and end-to-end qualification are pending. [Capacities REST registration requirements](https://developers.capacities.io/api/overview/authentication)

## Proposed registration fields

| Field | Proposed value |
| --- | --- |
| Integration name | ReMarkableBuddies Manager |
| Short description | Connect your Reader and Writer tablet app to Capacities and export prepared notes to a space you choose. |
| Public homepage | [ReMarkableBuddies Manager repository](https://github.com/s116821/ReMarkableBuddiesManager) |
| Square icon URL | |
| Client type | Public native or local application. Authorization Code with S256 PKCE and one-use state. Token endpoint client authentication method `none`. |
| Exact callback | `http://127.0.0.1:48761/oauth/capacities/callback` |
| REST resource | `https://api.capacities.io` |
| Requested scopes | `api:read` for verifying the selected space, writable shape and saved object. `api:write` for creating prepared notes and applying supported updates. `offline_access` for tablet-owned refresh between explicit user sign-ins. |
| Maintainer contact | ssellers_apps@icloud.com |
| Provider verification build and access | Pending a reviewer-accessible build and coordinated access to an authorized development tablet or suitable staging setup. |

## Proposed request

Please register ReMarkableBuddies Manager as a public client for the Capacities REST API. Manager helps users connect their tablet to Capacities and deliberately export prepared notes into a space they authorize. Users sign in with their own Capacities account and select the space in the provider consent screen. OAuth sign-in is the only connection method in Settings.

Both the local browser helper and Electron desktop host direct users to Capacities in their browser and share the exact IPv4 loopback callback listed above. They request the three listed scopes for the REST resource using S256 PKCE. The local Manager host validates the consent callback and transfers the one-use authorization code and verifier through an identity-bound private connection to the selected tablet. The tablet exchanges the code, checks the granted space, and owns access token storage, refresh, and revocation.

Please confirm that the exact callback may be registered for both Manager hosts under the same public client ID. The integration uses a fixed local port and requires no client secret. Please send the confirmed redirect policy and public client ID to the listed integration contact. We have left the icon URL blank. Can Capacities use a default icon on the consent screen? [Capacities REST OAuth flow](https://developers.capacities.io/api/overview/authentication)

## Provider verification steps for the staging build

1. Open the local browser or Electron Manager, select the authorized development tablet, and use **Connect to Capacities** in the Reader and Writer settings. Confirm the system browser displays the registered app name and offers selection of a test space under the tester’s own account.
2. Approve access. The browser returns to the exact registered loopback URI. Confirm Manager reports the completed connection for the originally selected tablet. Check the retained tablet receipt to verify that the authorized space UUID matches `GET /space` before exports are enabled; the Manager status deliberately does not expose the grant or space identity.
3. Export a small synthetic prepared note. Confirm it appears in the selected space with the configured test tags and that readback identifies the same object. Repeat sign-in and export in the other Manager host with a separate test enrollment.
4. Deny a new consent request, then cancel or expire another request before callback. Confirm no enrollment is installed from those attempts. Disconnect a successful test enrollment and verify Capacities reflects the remote revocation and the app disables local use.

These are planned acceptance steps for an eligible staging build. Provide its exact version and reproducible setup with the request.

## Maintainer acceptance before enabling consent

- Review the provider’s reply for any consent-screen icon requirement. [Registration instructions](https://developers.capacities.io/api/overview/authentication)
- Match the returned public client ID and exact approved callback against Manager’s compiled registration. Confirm the REST authorization metadata, S256, one-use current state and the required audience and scopes. An unavailable loopback port leaves consent unavailable.
- Verify both host flows on the authorized tablet. Wrong state, repeated callback, changed selected tablet, and a lost exchange response must preserve the appropriate refusal or unresolved original operation. Credential headers, callback secrets, and token files stay outside renderer responses and portable preferences.
- Qualify rotation and revocation with a test enrollment. Continue only with securely published replacement bytes after rotation. A lost refresh response requires reconnect. Report local disablement and provider revocation independently. [Capacities token lifecycle](https://developers.capacities.io/api/overview/authentication)
