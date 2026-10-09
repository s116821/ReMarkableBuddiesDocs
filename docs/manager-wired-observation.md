# Manager wired read-only observation

The bounded REM-41 observation slice gives the shared Angular UI a versioned
host adapter for explicit Linux USB/SSH reads. It returns observed tablet model,
firmware, architecture, boot identity and Buddy OS service state. Installed package
version, provenance and compatibility remain unknown; installation stays disabled.
It does not establish full REM-41 installer acceptance.

Follow the public component [setup and verification guide](https://github.com/s116821/RemarkableBuddiesManager/blob/main/docs/wired-observation.md).
Linux needs a user-owned Python environment with pinned Paramiko, iproute2/sysfs
and interface-bound socket support, independently verified SSH host-key trust and
protected authorized key configuration. Private tools/accounts are not prerequisites.
No credential, target, file or arbitrary command enters through the renderer.

The host verifies USB parent/vendor/product, interface generation/carrier/driver,
source address, ordinary and constrained on-link routes, and actual
SO_BINDTODEVICE readback before connection. It verifies the SSH host-key pin
before authentication. Netlink notifications plus periodic revalidation invalidate
changed USB/route identity. Reads have an absolute deadline, output limits and
known-file consistency checks; no Buddy command, admin API or Vellum executable
is invoked. Unknown state is not installation eligibility.

Electron exposes narrow observation/cancel IPC only to the owned top-level UI.
The browser path is an explicitly launched loopback helper serving the same built
Angular UI with exact Host/Origin, session-cookie and fixed-action checks. A remote
page or ordinary static deployment does not acquire tablet access. The user chooses
Read tablet state and can disconnect. Successful observations poll; failures,
changed boot/interface identity or cancellation clear current state and require
explicit reconnection. Late results cannot restore stale state.

Local fixtures cover route, trust-before-authentication, bounded SFTP reads,
fixed OS metadata alias, deadline/cancellation, active identity invalidation and
helper boundaries. Shared browser/helper and unpackaged/packaged Electron paths
have use-path checks. Linux RM1 read-only observation on October 8, 2026 found
reMarkable 1.0, firmware 3.28.0.172 and armv7l; the Buddy unit was not found/inactive.
This does not prove package absence, firmware compatibility, installation safety
or Windows/RM2/Paper Pro qualification. Windows native transport explicitly refuses
until its separate USB/interface-constrained implementation and hardware checks.

Current installer work still follows one Vellum-local package owner from official
Git-tagged Buddy artifacts; public catalog inclusion remains delayed post-1.0.
Observation neither installs/bootstrap Vellum nor changes services, accounts,
firmware or data. Existing completed release-preview and offline/published-ARM
qualification contracts remain independent.

The active central change is
[manager-wired-observation](../openspec/changes/manager-wired-observation/proposal.md).
Independent exact-revision review, CI, later spec synchronization/archive and
coordinated delivery remain required before accepting this bounded capability.
