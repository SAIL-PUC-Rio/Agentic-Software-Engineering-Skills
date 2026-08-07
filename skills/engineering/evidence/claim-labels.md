# Claim Labels

The skill speaks in terms of six canonical claim statuses. This is the full vocabulary — never use a status outside this table, and never substitute a synonym for one.

| Status            | Meaning                                                                  |
| ------------------ | ------------------------------------------------------------------------ |
| `PASS`             | A specific command, diff, or check ran and confirms the claim.           |
| `FAIL`             | A specific command, diff, or check ran and shows the claim does not hold. |
| `PARTIAL`          | Verified for some, but not all, of the claim's scope.                    |
| `NOT_RUN`          | A check exists for this claim but wasn't executed this time (skipped, out of budget, environment unavailable). |
| `NOT_APPLICABLE`   | No relevant check exists for this claim or category in this repo.        |
| `UNKNOWN`          | A check was attempted but produced no clear pass/fail signal.            |

## Rules

- Never round `NOT_RUN` or `UNKNOWN` up to `PASS`. A status reflects what was actually checked, not what's likely true.
- Report the implementation status and the evidence status as two separate lines. A publication failure never erases or overwrites the implementation result.
- Never call the task fully proven while the scope-to-proof map still has `FAIL`, `PARTIAL`, or open `UNKNOWN` rows.
