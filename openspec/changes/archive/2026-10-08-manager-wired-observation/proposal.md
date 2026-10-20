# Why
REM-41 is marked Done in Linear but current Manager main still exposes not-configured transport and InstalledUnknown. Completed release-preview/offline/published-ARM verification does not establish full installer acceptance. Add the next independent requirement: bounded read-only wired state observation in the shared browser/Electron Manager, without installer mutation or premature issue closure.

# What changes
- Versioned host adapter for explicit observe/cancel and sanitized state, with Linux USB parent/interface/on-link route and kernel-bound socket proof, independently configured SSH host key and protected user-owned key authentication.
- Reuse maintained Paramiko for SSH/SFTP; fixed bounded OS/file reads only. Expose observed model, firmware, architecture and service state; installed version/provenance remains unknown where no authoritative metadata contract exists.
- Controlled Electron IPC and an explicitly launched loopback helper serving the same Angular browser build. Normal websites cannot open SSH; no credentials or arbitrary commands enter renderer interfaces.
- Clear stale state on cancellation, timeout, cable/route/interface change or device boot change; require explicit reconnect after failure, never discover or switch targets.
- Public setup, failure fixtures and focused Linux RM1 read-only qualification. Main later owns Windows qualification; Windows transport remains explicitly unsupported until its own proven interface/socket binding adapter exists.

# Scope
Owning issue REM-41; no Vellum/bootstrap/install/service/firmware/account/config/data mutation, no Buddy HTTP/RPC/admin API, no SDK build/debug retry. One Vellum owner remains authoritative for later installation; public catalog delayed post1.0. Frozen REM-52/54 pairs remain untouched. Deliver paired Docs/Manager implementation PRs; archive only accepted completed capability.

# Canonical coherence at accepted lifecycle completion
The completed observation capability adds a narrowly specified preload contract.
Its lifecycle delta clarifies only manager-foundation's restricted desktop boundary
to permit separately specified narrow capabilities alongside identity, retaining
sandbox, no arbitrary command IPC and no Buddy API. The original pre-implementation
plan above and source evidence remain preserved; no further runtime capability is added.
