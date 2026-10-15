## Why
Accepted cooperative response-wait cancellation leaves TLS/root-store/DNS/proxy integration unqualified. The pinned Linux verifier and proxy matcher expose supported per-process environment inputs, enabling actual-client loopback qualification without account or machine-wide changes.

## What Changes
Add an owned Linux integration fixture using the existing OpenAI client, Python SSL/loopback proxy and OpenSSL-generated ephemeral roots/certificates. Test trusted/untrusted/wrong-name TLS, HTTPS CONNECT and NO_PROXY behavior. Production source, Cargo, protected Main files and accepted cancellation tests remain unchanged.
