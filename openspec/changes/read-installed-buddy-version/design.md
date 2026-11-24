## Selection

Reuse Manager's service-launcher resolver. Its two recognized executable paths come from the host. A loaded unit selects its direct Buddy executable. An absent unit with an empty launcher record selects the known standalone binary. Never execute the arguments carried in the unit's record. Invoke the selected executable with the fixed `--version` argument.

## Freshness

Verify the boot and service observation, each protected parent directory, and the executable's metadata. After reading the CLI output, compare the executable metadata, service observation and selected path again. A changed path discards the result even when both files independently pass their metadata checks. A missing or unsafe selected file ends the attempt.

## Verification

Exercise both layouts and a change of service path against the existing SSH test peer. The packaged browser and Electron checks exercise the same public action. On hardware the comparison is between the CLI report and Manager's displayed value. The package version and the running service have different evidence.
