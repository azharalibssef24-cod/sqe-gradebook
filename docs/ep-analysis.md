# Lab 5 — Equivalence Partitioning Analysis

## 1. Score Input — `letter_grade(score)`

| Equivalence Class | Input Range | Valid/Invalid | Representative |
|---|---|---|---|
| Invalid-low | score < 0 | Invalid | -10 |
| F grade | 0–59 | Valid | 45 |
| D grade | 60–69 | Valid | 65 |
| C grade | 70–79 | Valid | 75 |
| B grade | 80–89 | Valid | 85 |
| A grade | 90–100 | Valid | 95 |
| Invalid-high | score > 100 | Invalid | 150 |

## 2. Number of Scores Per Student

Business rule: A student must have between 1 and 6 scores.

| Equivalence Class | Input Range | Valid/Invalid | Representative |
|---|---|---|---|
| No scores | 0 | Invalid | 0 |
| Valid score count | 1–6 | Valid | 3 |
| Too many scores | 7+ | Invalid | 8 |

## 3. Student Name

Business rule: Name must be non-empty, maximum 50 characters, and contain only letters, spaces, and hyphens.

| Equivalence Class | Example | Valid/Invalid |
|---|---|---|
| Valid typical name | Ali Ahmed | Valid |
| Empty name | "" | Invalid |
| Over 50 characters | A name longer than 50 characters | Invalid |
| Contains digits | Ali123 | Invalid |
| Contains symbols | Ali@Ahmed | Invalid |

## EP Limitation

Equivalence Partitioning reduces the number of test cases by selecting representative values from groups of inputs expected to behave similarly.

However, EP may miss errors at the exact boundaries between classes. For example, it may not detect an error involving scores 59, 60, 69, or 70. Boundary Value Analysis will be used to test such edge cases in Lab 6.
