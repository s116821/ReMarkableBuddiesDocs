# Design

## Context

Start from merged Manager7ff5167 / Docs7686a67. Existing trusted Paramiko5 SSH/read code, helper origin/session boundary and sandboxed Electron remain shared. Windows currently refuses before spawning the host. Full REM-41 Vellum ownership/installer/REM42/35 work remains outstanding.

## Goals / Non-Goals

Support Windows10/11 x64 read-only observation through the two existing UIs. Prove actual USB ancestry plus network identity and interface-bound socket; never add an IP/source-only fallback. Do not qualify hardware via fixture evidence, install software on the tablet or alter release/version authority.

## Decisions

Use fixed host-only config with Windows adapter GUID, selected USB device instance ID, VID/PID, source, independently pinned host key and private-key path. Read selected adapter metadata via a fixed bounded Windows PowerShell/CIM query, never interpolating caller commands. Correlate GUID/index/LUID/PnP, walk present cfgmgr32 device parents and require the nearest non-interface USB parent to match selected identity. Use GetBestRoute2 for both normal and constrained route; require selected LUID/index/source, zero next-hop, matching peer prefix. Snapshot includes devnode, MAC and immutable adapter identity.

Use Winsock IP_UNICAST_IF: input index in network order, getsockopt returns host order. Readback must equal selected current index before bind/connect. No unsupported-option fallback.

Register all IPv4 interface/address/route notifications conservatively and selected USB devnode notifications before baseline/dial. Any notification invalidates the operation, closes its owned socket and refuses result publication even if identity later looks equal. Also repeat full snapshots during reads. Unregister outside callbacks.

Use pywin32 security/file handles for ACL/owner/reparse validation and bounded reads. Require local absolute paths; reject reparse components, remote paths, unowned config/keys, null DACL and grants outside current user/SYSTEM/Administrators. Keep parent private. Open file with no sharing to prevent replacement while security/contents are checked; no SSH agent/password fallback.

Retain Node13s kill boundary on Windows and a Python12s process deadline, existing phase limits/read limits and fixed peer/root. No logging raw exceptions.

## Risks / Trade-offs

Conservative notification invalidation may stop a read on unrelated network changes; explicit reconnect is preferable to ambiguous generation proof. CIM snapshot overhead is bounded and may yield timeout on overloaded hosts. ABI checks and actual OS API refusal/control tests must run on Windows CI; physical unplug/replug, competing route, driver/ACL and supported tablet qualification remain Main's required gate before claiming shipping hardware support.

## Migration Plan

Existing Linux config stays unchanged. Windows uses a separate strict schema with the same contract envelope number. Paired central Docs and implementation PR, implementation review then bounded sync/archive/final review. No new version fields.
