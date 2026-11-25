## Configuration ownership

Keep `check-initial` and `create-initial` for empty-root setup. Add `check-existing-default` and `create-existing-default` to `--configuration-operation` with the same no-input JSON report shape. Use the latter pair only on an existing default installation observed through the qualified wired host.

Verify absence of both the canonical and legacy configuration paths. Reuse the existing first-configuration staged, descriptor-relative no-clobber publisher for the canonical path. Admit the existing default Store through the ordinary preference open and retain its ownership through closing readback. Read/check never initializes storage. Busy, invalid and unsupported roots or a legacy configuration refuse. If publication may have occurred without verified readback, report uncertainty and leave the original operation intact.
