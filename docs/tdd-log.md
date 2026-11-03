# Lab 8 – Test-Driven Development (TDD) Log

## Feature: Student Ranking

**Branch:** `feature/rank-students-tdd`

**Description:** Implemented `rank_students(roster)` to return students ordered by average score in descending order. Students with equal averages are sorted alphabetically by name.

---

## TDD Cycle 1: Empty Roster

**Requirement:** An empty roster should return an empty list.

- **RED:** The test failed because `rank_students()` did not exist.
- **RED Commit:** `eb8097b` – `test(rank): red - empty roster returns empty list`
- **GREEN:** Added a basic implementation returning an empty list.
- **GREEN Commit:** `0c212ad` – `feat(rank): green - stub rank_students returning empty list`
- **Result:** Empty roster test passed.

## TDD Cycle 2: Single Student

**Requirement:** A roster containing one student should return that student in a list.

- **RED:** The test failed because the function returned an empty list.
- **RED Commit:** `5c51eba` – `test(rank): red - single student returns that student`
- **GREEN:** Updated the function to return the single student.
- **GREEN Commit:** `9eb4ef5` – `feat(rank): green - return single student`
- **Result:** Single student test passed.

## TDD Cycle 3: Descending Average

**Requirement:** Students should be sorted from the highest average to the lowest.

- **RED:** The test failed because the function returned only the first student.
- **RED Commit:** `b9a71e3` – `test(rank): red - sort students by average descending`
- **GREEN:** Implemented sorting based on student average in descending order.
- **GREEN Commit:** `44c9f25` – `feat(rank): green - sort students by average descending`
- **Result:** Students were correctly sorted by average.

## TDD Cycle 4: Alphabetical Tie-Breaking

**Requirement:** Students with equal averages should be sorted alphabetically by name.

- **RED:** The test failed because equal-average students were not alphabetically ordered.
- **RED Commit:** `7797737` – `test(rank): red - sort equal averages alphabetically`
- **GREEN:** Updated the sorting logic to use average and student name.
- **GREEN Commit:** `2d0cffd` – `feat(rank): green - alphabetical tie breaking`
- **Result:** Equal-average students were correctly sorted alphabetically.

## TDD Cycle 5: Zero-Average Edge Case

**Requirement:** A student with a zero average should appear after students with higher averages.

- **Test:** Added a test with students having averages of 90, 50, and 0.
- **Result:** The test passed using the existing sorting implementation.
- **Test Commit:** `26fc62f` – `test(rank): green - zero average student edge case`
- **Implementation Change:** No additional implementation change was required.

---

## Final Test Results

The complete project test suite was executed using:

`py -m pytest -v`

**Result: 80 passed in 0.52 seconds.**

All existing tests and the five new ranking tests passed.

## Retrospective

The TDD approach helped us develop the student ranking feature step by step. We wrote tests before implementing the required functionality and observed failures during the RED phase. We then added the minimum implementation needed to make each test pass during the GREEN phase. The tests helped us identify and handle important cases, including empty rosters, single students, descending averages, equal averages, and zero averages. Finally, all 80 project tests passed, showing that the new feature works without breaking existing functionality.