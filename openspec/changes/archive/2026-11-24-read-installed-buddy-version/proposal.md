## Why

Manager's **Read binary version** action looks under `/opt/bin`. The resident package used on reMarkable 2 installs its executable under `/home/root/.local/lib/remarkable-buddies`. The button can therefore report a missing or outdated binary on a working installation.

## What Changes

Use the service's selected executable for a version read. Keep support for standalone installations and report an unavailable result if the service selects an unknown executable or changes during the read.

## Capabilities

### Modified Capabilities

- `manager-runtime-identity` covers standalone and resident installations in both Manager hosts.

## Impact

The existing wired host helper and its regression cases change. The action continues to report the CLI's self-reported version. Package ownership, running-process identity and update eligibility use their own evidence.
