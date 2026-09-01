# GradeBook Manual Test Execution Results

## Execution Summary

* Total Test Cases: 12
* Passed: 11
* Failed: 0
* Blocked: 1
* Overall Status: Testing completed with one blocked requirement
* Automated Regression Result: 12 passed, 0 failed

## Manual Test Results

| Test Case | Result  | Execution Note                                                                                    |
| --------- | ------- | ------------------------------------------------------------------------------------------------- |
| TC-01     | PASS    | Valid score `80` was successfully added to the student's scores list.                             |
| TC-02     | PASS    | Negative score `-5` raised `ValueError: Score cannot be negative`.                                |
| TC-03     | PASS    | Non-numeric input `"abc"` was rejected with a `TypeError` and was not added.                      |
| TC-04     | PASS    | Boundary score `0` was accepted successfully.                                                     |
| TC-05     | PASS    | Boundary score `100` was accepted successfully.                                                   |
| TC-06     | PASS    | | TC-06 | PASS | Score `101` raised `ValueError: Score cannot be greater than 100`. Original defect: GitHub Issue #15; fixed and retested successfully. |                                |
| TC-07     | PASS    | Scores `80`, `70`, and `90` produced an average of `80.0`.                                        |
| TC-08     | PASS    | A student with no scores returned an average of `0.0`.                                            |
| TC-09     | PASS    | Duplicate student ID was rejected with `ValueError: Student ID already exists`.                   |
| TC-10     | PASS    | Multiple valid scores `60`, `80`, and `90` were added successfully.                               |
| TC-11     | BLOCKED | The current `Student` class does not provide a dedicated case-insensitive name-comparison method. |
| TC-12     | PASS    | Score `-1` raised `ValueError: Score cannot be negative`.                                         |

## Automated Regression Test

The complete automated test suite was executed using:

`py -m pytest`

Result:

`12 passed in 0.05s`

The automated regression suite passed successfully with no failures.

## Defect Retest

TC-06 originally identified a defect because the implementation accepted scores greater than `100`.

The implementation was corrected to reject scores above `100`.

After the fix, TC-06 was manually retested and passed. The complete automated regression suite also passed all 12 tests.

## Blocked Test

**TC-11 — Case-Insensitive Student Name Comparison**

**Requirement:** REQ-08

**Result:** BLOCKED

The current GradeBook implementation stores the student's name but does not provide a dedicated name-comparison method. Therefore, the required case-insensitive comparison cannot be executed against the current implementation.

No GitHub defect issue was created for TC-11 because the test is blocked by missing functionality rather than a verified implementation failure.

## Final Assessment

The GradeBook implementation successfully passed all executable manual test cases. One test case, TC-11, remains blocked because the required name-comparison functionality is not exposed by the current implementation.

The automated regression suite passes all 12 existing automated tests.
