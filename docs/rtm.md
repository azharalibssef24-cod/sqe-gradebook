# GradeBook Requirements Traceability Matrix

The Requirements Traceability Matrix (RTM) maps each GradeBook requirement to the test cases that verify it.

| Requirement ID | Requirement | Test Case ID(s) | Coverage Status |
|---|---|---|---|
| REQ-01 | The system shall allow a student to add a valid score from 0 to 100. | TC-01, TC-10 | Covered |
| REQ-02 | The system shall reject negative scores. | TC-02, TC-12 | Covered |
| REQ-03 | The system shall reject non-numeric score input. | TC-03 | Covered |
| REQ-04 | The system shall reject the creation of a student when the student ID already exists. | TC-09 | Covered |
| REQ-05 | The system shall calculate the correct average when a student has one or more scores. | TC-07 | Covered |
| REQ-06 | The system shall return 0.0 when the average is requested for a student with no scores. | TC-08 | Covered |
| REQ-07 | The system shall accept the boundary scores 0 and 100. | TC-04, TC-05, TC-06 | Covered |
| REQ-08 | The system shall compare student names without treating uppercase and lowercase letters as different when name comparison is required. | TC-11 | Blocked |

## Traceability Summary

- Total requirements: 8
- Requirements with linked test cases: 8
- Requirements with zero linked test cases: 0
- Requirements with blocked coverage: 1
- Requirements with covered test cases: 7

## Gap Closure

REQ-08 is linked to TC-11. During manual execution, TC-11 is expected to be BLOCKED because the current GradeBook implementation does not expose a dedicated student-name comparison method. The requirement is therefore traceable but not currently verifiable through the implemented code.