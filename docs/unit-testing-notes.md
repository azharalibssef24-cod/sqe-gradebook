# Unit Testing Notes

## 1. Introduction

This document describes the unit testing activities performed in Lab 7 using pytest.

## 2. Fixtures

Fixtures provide reusable test data and setup.

- Module-scope fixture: Created once for the entire test module.
- Function-scope fixture: Created separately for each test function.

## 3. Student Testing

Tests cover:
- Student creation
- Adding valid scores
- Rejecting invalid scores
- Duplicate student IDs
- Calculating student averages

## 4. Parametrized Testing

Used `pytest.mark.parametrize` to test six different score values.

Test cases include:
- 0
- 50
- 100
- -5
- 105
- 150

Each test case has a descriptive ID.

## 5. Roster Testing

Tests cover:
- Empty roster average
- Single-student average
- Multiple-student average

## 6. Mocking File Operations

Used `mock_open()` and `patch()` to test file operations without creating a real file.

Tests verify:
- Expected content is written.
- An `OSError` is converted into `GradeBookIOError`.

## 7. Test Execution

### Verbose command

Command:

`py -m pytest -v tests/`

Purpose: Displays individual test names and their results.

### Short traceback command

Command:

`py -m pytest --tb=short`

Purpose: Displays shorter error information when tests fail.

## 8. Final Test Result

Total tests passed: 18

Status: All tests passed successfully.