# Journal

## Entry 1 (opened 2026-10-25T09:18:17Z)

1. **Read:** TASK.md prerequisite: task 01 painting with a rig that builds; 01-build grader result
2. **Expect:** The prerequisite check confirms 01-build exits 1 with TIP_OVER_ROOT, so task 04 cannot inherit a buildable rig
3. **Chose / turned down:** Read the existing grader result once; do not draft physics against a rig that fails its required base gate.
4. **Happened** (2026-10-25T09:18:23Z): "built": {"pass": False, "read": "rig-parts build exit 1"}; "checked": {"pass": False

## At the end (2026-10-25T09:18:26Z)

- **Where I guessed:** No task 04 config or physics values were authored.
- **What I could not find:** The task requires a rig from task 01 that builds; the existing grader result says build exit 1 and CHECK_TIP_OVER_ROOT FAIL, so the soft-region recipe cannot be applied to a passing base rig.
