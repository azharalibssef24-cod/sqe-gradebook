# GradeBook Test Cases

## TC-01 — Add Valid Score

**Requirement:** REQ-01 — Valid Score

**Objective:** Verify that a student can successfully add a valid score.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 101.
2. Call `add_score(80)`.
3. Check the student's scores list.

**Expected Result:** The score 80 is successfully added to the student's scores list.

**Test Type:** Functional — Positive

**Priority:** High

## TC-02 — Reject Negative Score

**Requirement:** REQ-02 — Negative Score Rejection

**Objective:** Verify that the system rejects a negative score.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 102.
2. Call `add_score(-5)`.
3. Check whether the score was added.

**Expected Result:** A `ValueError` is raised with the message "Score cannot be negative", and the negative score is not added to the student's scores list.

**Test Type:** Functional — Negative

**Priority:** High

## TC-03 — Reject Non-Numeric Score

**Requirement:** REQ-03 — Non-Numeric Score Rejection

**Objective:** Verify that the system rejects non-numeric score input.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 103.
2. Call `add_score("abc")`.
3. Check whether the score was added.

**Expected Result:** The system rejects the non-numeric input by raising an error, and the value "abc" is not added to the student's scores list.

**Test Type:** Functional — Negative

**Priority:** High

## TC-04 — Accept Minimum Boundary Score

**Requirement:** REQ-07 — Score Boundaries

**Objective:** Verify that the system accepts the minimum valid boundary score of 0.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 104.
2. Call `add_score(0)`.
3. Check the student's scores list.

**Expected Result:** The score 0 is successfully added to the student's scores list.

**Test Type:** Functional — Positive / Boundary

**Priority:** High

## TC-05 — Accept Maximum Boundary Score

**Requirement:** REQ-07 — Score Boundaries

**Objective:** Verify that the system accepts the maximum valid boundary score of 100.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 105.
2. Call `add_score(100)`.
3. Check the student's scores list.

**Expected Result:** The score 100 is successfully added to the student's scores list.

**Test Type:** Functional — Positive / Boundary

**Priority:** High

## TC-06 — Reject Score Above 100

**Requirement:** REQ-01 — Valid Score

**Objective:** Verify that the system rejects a score greater than 100.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 106.
2. Call `add_score(101)`.
3. Check whether the score was added.

**Expected Result:** The system rejects the score 101, and the score is not added to the student's scores list.

**Test Type:** Functional — Negative / Boundary

**Priority:** High

## TC-07 — Calculate Average Score

**Requirement:** REQ-05 — Average Calculation

**Objective:** Verify that the system correctly calculates the average of one or more scores.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 107.
2. Add scores 80, 70, and 90.
3. Call the `average()` method.

**Expected Result:** The system returns an average score of 80.0.

**Test Type:** Functional — Positive

**Priority:** High

## TC-08 — Return Zero for Empty Scores

**Requirement:** REQ-06 — Empty Score Average

**Objective:** Verify that the system returns 0.0 when a student has no scores.

**Precondition:** A Student object exists with a unique student ID and no scores.

**Steps:**

1. Create a Student with name "Ali" and student ID 108.
2. Do not add any scores.
3. Call the `average()` method.

**Expected Result:** The system returns `0.0`.

**Test Type:** Functional — Positive / Boundary

**Priority:** High

## TC-09 — Reject Duplicate Student ID

**Requirement:** REQ-04 — Duplicate Student ID

**Objective:** Verify that the system rejects creation of a student when the student ID already exists.

**Precondition:** A Student object already exists with student ID 109.

**Steps:**

1. Create a Student with name "Ali" and student ID 109.
2. Attempt to create another Student with name "Ahmed" and student ID 109.
3. Observe the result.

**Expected Result:** A `ValueError` is raised with the message "Student ID already exists", and the duplicate student is not created.

**Test Type:** Functional — Negative

**Priority:** High

## TC-10 — Add Multiple Valid Scores

**Requirement:** REQ-01 — Valid Score

**Objective:** Verify that a student can successfully add multiple valid scores.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 110.
2. Add scores 60, 80, and 90.
3. Check the student's scores list.

**Expected Result:** All three valid scores are successfully added to the student's scores list.

**Test Type:** Functional — Positive

**Priority:** Medium

## TC-11 — Case-Insensitive Student Name Comparison

**Requirement:** REQ-08 — Student Name Comparison

**Objective:** Verify that student names are compared without treating uppercase and lowercase letters as different.

**Precondition:** Two Student objects exist with unique student IDs.

**Steps:**

1. Create a Student with name "Ali" and student ID 111.
2. Create another Student with name "ALI" and student ID 112.
3. Compare the two student names using the required name-comparison functionality.

**Expected Result:** The system considers "Ali" and "ALI" equal because the comparison is case-insensitive.

**Test Type:** Functional — Positive / Case-Insensitive

**Priority:** High

## TC-12 — Reject Minimum Invalid Score

**Requirement:** REQ-02 — Negative Score Rejection

**Objective:** Verify that the system rejects a score immediately below the minimum valid boundary.

**Precondition:** A Student object exists with a unique student ID.

**Steps:**

1. Create a Student with name "Ali" and student ID 112.
2. Call `add_score(-1)`.
3. Check whether the score was added.

**Expected Result:** A `ValueError` is raised with the message "Score cannot be negative", and the score -1 is not added to the student's scores list.

**Test Type:** Functional — Negative / Boundary

**Priority:** High
