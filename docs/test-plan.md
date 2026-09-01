# Test Plan — SQE GradeBook
## 1. Introduction

This test plan defines the testing approach for the SQE GradeBook project.
The purpose of testing is to verify that student records, scores, and grade statistics behave correctly and that invalid inputs are handled appropriately.
Testing will identify defects and provide evidence that the implemented functionality meets the defined requirements.
## 2. Test Items

The primary test item is the SQE GradeBook software, with focus on the Student class and its student record, score management, and average calculation functionality. The tests will verify valid operations, invalid input handling, duplicate student ID handling, and correct grade statistics.
## 3. Features to be Tested

The following features will be tested:

- Student creation with a valid name and unique student ID.
- Rejection of duplicate student IDs.
- Adding valid student scores.
- Rejection of negative scores.
- Handling of invalid or non-numeric score input.
- Calculation of the average for students with multiple scores.
- Calculation of the average for a student with a single score.
- Handling of the average for a student with no scores.
- ## 4. Features Not to be Tested

The following features are outside the scope of this lab:

- User interface testing, because the project is being tested through Python code.
- Database or external storage integration.
- Performance and load testing.
- Security and authentication testing.
- Deployment and production environment testing.
- ## 5. Test Approach

Testing will use manual functional testing of the GradeBook Python code. Each test case will be executed using defined preconditions and numbered steps, and the actual result will be compared with the expected result. Both positive tests using valid inputs and negative tests using invalid inputs or error conditions will be included. At least three negative/error-path test cases will be used to verify that the software handles invalid conditions correctly. Regression checks will be performed after defects are fixed to ensure that existing functionality continues to work.
- Correct handling of score boundary values such as 0 and 100.
- Case-insensitive student name comparison where applicable
- ## 6. Pass/Fail Criteria

A test case will be marked PASS when the actual result matches the expected result and the required functionality behaves correctly. A test case will be marked FAIL when the actual result differs from the expected result or the required behavior is not achieved. A test case will be marked BLOCKED when it cannot be executed because of an unavailable dependency, environment problem, or other external condition. All test results will include a brief note explaining the observed outcome.
## 7. Test Deliverables

The test deliverables will include the completed test plan, twelve documented test cases, a requirements traceability matrix (RTM), manual test execution results, and GitHub Issues for any failed test cases. These artifacts will provide evidence of test coverage, test execution, and defect tracking.
## 8. Environmental Needs

Testing will be performed using Python 3.14.7 and the SQE GradeBook GitHub repository. The tests will be executed against the Python source code using the development environment available to the tester. GitHub will be used to manage the test documentation and to track any defects discovered during testing.
## 9. Schedule

Testing activities will be completed in the following sequence:

1. Prepare the test plan and define the requirements.
2. Create twelve test cases covering the required GradeBook functionality.
3. Build and review the requirements traceability matrix.
4. Execute all test cases manually and record PASS, FAIL, or BLOCKED results.
5. Create GitHub Issues for any failed test cases.
6. Perform regression testing after defects are fixed.
7. Review the final test results and testing artifacts for completeness.
8. ## 10. Risks

The main testing risks include incomplete test coverage, defects that are not identified during manual testing, and environment-related problems that may prevent test execution. Changes made to fix defects may introduce regressions in existing functionality. Limited testing time may also reduce the number of scenarios that can be executed. These risks will be reduced by using the RTM to track coverage, recording all test results, and performing regression checks after fixes.
