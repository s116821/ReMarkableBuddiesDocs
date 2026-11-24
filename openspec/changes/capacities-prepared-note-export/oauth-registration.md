# Capacities REST OAuth registration

The registration submitted on November 23, 2026 covers both Manager hosts. To prepare a live verification build, use the public client ID and redirect URI confirmed by Capacities. [Capacities REST registration requirements](https://developers.capacities.io/api/overview/authentication)

## Registration fields

| Field | Submitted value |
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
| Testing instructions | Follow the steps below with a USB-connected development tablet and a Capacities test space. The maintainer can arrange a session once Capacities issues a public client ID for that callback. |

## Integration and callback

Please register ReMarkableBuddies Manager as a public client for the Capacities REST API. Manager helps users connect their tablet to Capacities and deliberately export prepared notes into a space they authorize. Users sign in with their own Capacities account and select the space in the provider consent screen. OAuth sign-in is the only connection method in Settings.

Both the local browser helper and Electron desktop host direct users to Capacities in their browser and share the exact IPv4 loopback callback listed above. They request the three listed scopes for the REST resource using S256 PKCE. The local Manager host validates the consent callback and transfers the one-use authorization code and verifier through an identity-bound private connection to the selected tablet. The tablet exchanges the code, checks the granted space, and owns access token storage, refresh, and revocation.

Please confirm that the exact callback may be registered for both Manager hosts under the same public client ID. The integration uses a fixed local port and requires no client secret. Please send the confirmed redirect policy and public client ID to the listed integration contact. We have left the icon URL blank. Can Capacities use a default icon on the consent screen? [Capacities REST OAuth flow](https://developers.capacities.io/api/overview/authentication)

## Provider verification steps for the staging build

The public source is available for review now. For live sign-in, the maintainer must build Manager and Buddy with the same provider-issued public client ID and the registered callback, install Buddy on the development tablet, and supply the matching Manager revision. Both components currently leave that registration unset. [Manager registration](https://github.com/s116821/ReMarkableBuddiesManager/blob/f4385f356a5481ed2ad3df8c4cc6b8050a8175d0/host/capacities-consent.mjs) · [Buddy registration](https://github.com/s116821/ReMarkableBuddies/blob/c4ec69f6008d71c4278768713d71cce42a9cce4f/src/config/capacities/oauth.rs)

1. Connect the development tablet by USB. To exercise the browser Manager from the supplied source revision, install the locked dependencies with `npm ci`, run `npm run build` and `npm run wired:browser`, and open the printed local URL. For Electron, run `npm run desktop` with the same wired configuration. [Wired host setup](https://github.com/s116821/ReMarkableBuddiesManager/blob/f4385f356a5481ed2ad3df8c4cc6b8050a8175d0/docs/wired-observation.md)
2. Select the tablet. In **Settings → Reader & Writer**, choose **Edit Reader & Writer**, set **Export backend** to **Capacities**, then **Save Reader & Writer**. Choose **Connect to Capacities** and verify the registered app name in the browser. Select a test space in your own Capacities account and approve access.
3. Confirm the browser returns to the registered loopback address and Manager shows a connection for the selected tablet. Restart Buddy to apply the saved export setting. Export a small synthetic prepared note and verify it appears in the chosen space. Update the note and verify the same object changes. Repeat in the other Manager host with a separate test enrollment.
4. Deny a new consent request, then cancel or expire another before callback. Confirm neither creates an enrollment. Disconnect a successful test enrollment and verify Capacities reflects revocation and the app disables local use.

During the live session, the maintainer also checks the tablet receipt against the space UUID returned by `GET /space`, verifies configured test tags and records the exact component versions used.

## Maintainer acceptance before enabling consent

- Review the provider’s reply for any consent-screen icon requirement. [Registration instructions](https://developers.capacities.io/api/overview/authentication)
- Match the returned public client ID and exact approved callback against Manager’s compiled registration. Confirm the REST authorization metadata, S256, one-use current state and the required audience and scopes. An unavailable loopback port leaves consent unavailable.
- Verify both host flows on the authorized tablet. Wrong state, repeated callback, changed selected tablet, and a lost exchange response must preserve the appropriate refusal or unresolved original operation. Credential headers, callback secrets, and token files stay outside renderer responses and portable preferences.
- Qualify rotation and revocation with a test enrollment. Continue only with securely published replacement bytes after rotation. A lost refresh response requires reconnect. Report local disablement and provider revocation independently. [Capacities token lifecycle](https://developers.capacities.io/api/overview/authentication)
