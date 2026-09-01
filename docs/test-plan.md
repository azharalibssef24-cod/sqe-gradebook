# Test Plan — SQE GradeBook

## 1. Introduction

This test plan defines the testing approach for the SQE GradeBook project. The purpose of testing is to verify that student records, score management, and average calculations behave correctly and that invalid inputs are handled appropriately. Testing will identify defects and provide evidence that the implemented functionality meets the defined requirements.

## 2. Test Items

The primary test item is the SQE GradeBook software, with focus on the `Student` class and its student record, score management, duplicate student ID validation, and average calculation functionality. Testing will cover valid operations, invalid score inputs, score boundaries, duplicate student IDs, and average calculations.

## 3. Features to be Tested

The following features will be tested:

* Student creation with a valid name and unique student ID.
* Rejection of duplicate student IDs.
* Adding valid student scores.
* Rejection of negative scores.
* Rejection of scores greater than 100.
* Rejection of non-numeric score input.
* Acceptance of score boundary values 0 and 100.
* Calculation of the average for students with multiple scores.
* Calculation of the average for a student with no scores.
* Case-insensitive student name comparison where applicable.

## 4. Features Not to be Tested

The following features are outside the scope of this lab:

* User interface testing, because the GradeBook functionality is being tested through Python code.
* Database or external storage integration because the current implementation does not use an external database.
* Performance and load testing because the lab focuses on functional correctness.
* Security and authentication testing because authentication is not implemented in the current GradeBook module.
* Deployment and production environment testing because testing is performed in the development environment.

## 5. Test Approach

Testing will use functional testing of the GradeBook Python code. Each test case will have a unique ID, requirement reference, objective, preconditions, numbered steps, expected result, priority, and test type. Both positive tests using valid inputs and negative tests using invalid inputs or error conditions will be included.

A total of 12 test cases will be executed. At least three test cases will explicitly cover negative or error-path scenarios. Regression testing will be performed after defects are fixed to verify that previously working functionality continues to pass.

## 6. Pass/Fail Criteria

A test case will be marked **PASS** when the actual result matches the expected result and the required functionality behaves correctly.

A test case will be marked **FAIL** when the actual result differs from the expected result or the required behavior is not achieved.

A test case will be marked **BLOCKED** when it cannot be executed because of an unavailable dependency, environment problem, or other external condition.

The overall test cycle will be considered successful when:

* At least **95% of the 12 planned test cases pass**.
* **0 Critical defects** remain open.
* All requirements have at least one linked test case in the RTM.
* All failed test cases have a corresponding GitHub Issue.

## 7. Test Deliverables

The test deliverables will include:

* `docs/test-plan.md`
* `docs/test-cases.md`
* `docs/rtm.md`
* Manual test execution results
* GitHub Issues for failed test cases
* Defect and retest evidence where applicable

These artifacts will provide evidence of test coverage, execution, traceability, and defect tracking.

## 8. Environmental Needs

Testing will be performed using Python 3.14.7 and the SQE GradeBook GitHub repository. Tests will be executed against the Python source code using the development environment available to the tester. Pytest will be used for automated verification where appropriate, while the Lab 4 manual execution pass will record individual test results. GitHub will be used to manage the source code, test documentation, and defect issues.

## 9. Schedule

Testing activities will be completed in the following sequence:

1. Review and document GradeBook requirements.
2. Prepare the Test Plan.
3. Create 12 test cases.
4. Build and review the Requirements Traceability Matrix.
5. Execute all 12 test cases manually.
6. Record PASS, FAIL, or BLOCKED results.
7. Create GitHub Issues for failed tests.
8. Fix identified defects where required.
9. Perform regression testing after fixes.
10. Review the final testing artifacts.

## 10. Risks

The main testing risks include incomplete test coverage, defects that are not identified during testing, and environment-related problems that may prevent test execution. Changes made to fix defects may introduce regressions in existing functionality. Limited testing time may also reduce the number of scenarios that can be executed.

These risks will be reduced by using the RTM to track requirements coverage, recording all test results, creating GitHub Issues for defects, and performing regression testing after fixes.