# Lab 11 — Automated Test Coverage

## 1. Baseline Coverage

The initial coverage report was generated using pytest-cov.

- Tests before improvement: 98
- Baseline line coverage: 99%
- Uncovered line: 100 in `gradebook.py`
- The uncovered line handled non-string names in `validate_name()`.

## 2. Closing the Coverage Gap

Added a test named `test_validate_name_rejects_non_string()` in `tests/test_validate_name.py`.

The test verifies that passing a non-string value raises the expected `ValueError`.

After adding the test:

- Tests: 99 passed
- Line coverage: 100%
- Branch coverage: 100%

## 3. Identifying the Weakest Files and Functions

The project contains one meaningful Python source file: `src/gradebook/gradebook.py`.

The final coverage report shows:

- Statements: 82
- Missing statements: 0
- Branches: 42
- Partial branches: 0
- Coverage: 100%

No uncovered lines or branches remained. Therefore, three weakest source files or functions could not be identified from the final report.

## 4. Coverage vs. Quality Discussion

The original `test_save_to_file_error()` test checked only whether a `GradeBookIOError` exception was raised.

This was a coverage trap because executing the error-handling code increased coverage, but the test did not verify the actual error message.

The assertion was strengthened to:

`pytest.raises(GradeBookIOError, match="Unable to save roster to file")`

This verifies both the exception type and the expected error message.

The strengthened test passed successfully.

## 5. Coverage Threshold

Updated `pytest.ini` with:

`addopts = --cov=src --cov-branch --cov-report=term-missing --cov-fail-under=85`

The minimum required coverage is 85%.

A single-test run produced approximately 40% coverage and failed the threshold, confirming that enforcement works.

The complete test suite passed with 100% coverage.

## 6. Final Results

| Measurement | Result |
|---|---:|
| Total tests | 99 |
| Passed tests | 99 |
| Line coverage | 100% |
| Branch coverage | 100% |
| Missing statements | 0 |
| Partial branches | 0 |
| Minimum threshold | 85% |

**Conclusion:** The GradeBook project achieved 100% line and branch coverage, strengthened an error-handling assertion, and successfully enforced the minimum coverage threshold.