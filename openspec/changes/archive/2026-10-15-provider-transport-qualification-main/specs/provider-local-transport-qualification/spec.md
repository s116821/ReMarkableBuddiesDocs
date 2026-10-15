## ADDED Requirements

### Requirement: Owned Linux actual-client transport qualification
Local transport qualification SHALL exercise the existing application client with generated loopback TLS and proxy resources using isolated child-process environment inputs. It SHALL require exact child completion plus provider/proxy witnesses, retain trust/name rejection and keep proxy credentials separate from encrypted origin authorization without global settings or production-source changes.

#### Scenario: Root and name validation
- **WHEN** correct, unrelated-root and wrong-name local certificates are exercised
- **THEN** the correct trusted case completes the synthetic request while negative cases demonstrate TLS contact/rejection and zero application requests, with original client behavior unchanged.

#### Scenario: CONNECT and bypass
- **WHEN** an owned HTTPS proxy or matching NO_PROXY is selected only for the test child
- **THEN** exact CONNECT/direct routing is witnessed, origin authorization remains inside TLS, proxy authorization does not reach the origin and untrusted TLS remains rejected through the tunnel.

### Requirement: Bounded fixture ownership and honest limits
Fixtures SHALL bound startup, request, child completion and cleanup, remove only their marked private resources and never call an ignored or unavailable control passed. Linux process-root/proxy evidence SHALL NOT establish other-platform, native, production DNS/root-store/proxy, provider billing or whole-issue qualification.

#### Scenario: Startup or client failure
- **WHEN** a tool, server or child fails or misses its deadline
- **THEN** qualification refuses with owned stop/kill/wait cleanup and no fabricated completion or machine-wide configuration change.
