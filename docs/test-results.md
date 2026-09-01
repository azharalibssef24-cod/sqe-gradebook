# GradeBook Test Execution Results

## Test Execution Summary

- Total Test Cases: 12
- Passed: 11
- Failed: 1
- Pass Rate: 91.7%

## Test Results

| Test Case | Requirement | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC-01 | REQ-01 — Valid Score | Valid score is added successfully | Score was added successfully | PASS |
| TC-02 | REQ-02 — Negative Score Rejection | Negative score is rejected with ValueError | ValueError was raised | PASS |
| TC-03 | REQ-03 — Non-Numeric Score Rejection | Non-numeric score is rejected | Input was rejected | PASS |
| TC-04 | REQ-07 — Score Boundaries | Score 0 is accepted | Score 0 was accepted | PASS |
| TC-05 | REQ-07 — Score Boundaries | Score 100 is accepted | Score 100 was accepted | PASS |
| TC-06 | REQ-01 — Valid Score | Score above 100 is rejected | Score 101 was accepted | FAIL |
| TC-07 | REQ-05 — Average Calculation | Average of 80, 70, and 90 is 80.0 | 80.0 was returned | PASS |
| TC-08 | REQ-06 — Empty Score Average | Empty score list returns 0.0 | 0.0 was returned | PASS |
| TC-09 | REQ-04 — Duplicate Student ID | Duplicate ID is rejected | ValueError was raised | PASS |
| TC-10 | REQ-01 — Valid Score | Multiple valid scores are added | All scores were added | PASS |
| TC-11 | REQ-08 — Student Name Comparison | Names are compared case-insensitively | Comparison returned true | PASS |
| TC-12 | REQ-02 — Negative Score Rejection | Score -1 is rejected | ValueError was raised | PASS |

## Failed Test

### TC-06 — Reject Score Above 100

**Expected:** The system should reject a score greater than 100.

**Actual:** The system accepted the score `101`.

**Result:** FAIL

**Defect:** `Student.add_score()` checks whether a score is negative but does not check whether the score exceeds 100.

**Required Fix:** Add validation to reject scores greater than 100.
