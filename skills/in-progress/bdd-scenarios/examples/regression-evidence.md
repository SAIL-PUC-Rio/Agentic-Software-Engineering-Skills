# Fixture: evidence claims for a pure refactor

Shape of the `/evidence` scope-to-proof rows for a spec whose only Behavioral Specifications are `**Kind:** regression` entries (BS-001, BS-002 from [regression-good.feature](regression-good.feature)) and whose Testing Decisions say the existing suite passes before and after. Base `a1b2c3d`, current `e4f5a6b`.

| Claim ID | Requirement or property | Source | Verification | Evidence IDs | Status |
| -------- | ----------------------- | ------ | ------------ | ------------ | ------ |
| CLM-001 | Existing suite passes before and after | Testing Decisions | `npm test` on base and on current, same command | EVD-001 (base), EVD-002 (current) | PASS |
| CLM-002 | Records sharing a SKU are merged into one | BS-001 | `dedup_test` "merges records with same SKU" at the stage interface | EVD-002 | PASS |
| CLM-003 | A record without a SKU is rejected | BS-002 | No test verifies it | none | NOT_APPLICABLE |

Had EVD-001 (the base run) not been recorded, CLM-001 would be `NOT_RUN`, not `PASS`.
