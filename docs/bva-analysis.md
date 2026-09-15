# Boundary Value Analysis

## 1. Letter Grade Boundaries

The `letter_grade()` function accepts scores from 0 to 100.

| Boundary | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
|---|---:|---|---:|---|---:|---|
| Domain minimum | -1 | Reject | 0 | F | 1 | F |
| F/D cutoff | 59 | F | 60 | D | 61 | D |
| D/C cutoff | 69 | D | 70 | C | 71 | C |
| C/B cutoff | 79 | C | 80 | B | 81 | B |
| B/A cutoff | 89 | B | 90 | A | 91 | A |
| Domain maximum | 99 | A | 100 | A | 101 | Reject |

### Boundary Values

The important boundaries for `letter_grade()` are:

- Minimum valid score: `0`
- F/D cutoff: `60`
- D/C cutoff: `70`
- C/B cutoff: `80`
- B/A cutoff: `90`
- Maximum valid score: `100`

BVA tests the value immediately below, the boundary itself, and the value immediately above each boundary.

---

## 2. Roster Score-Count Boundaries

The `Roster` rule from Lab 5 requires each student to have between 1 and 6 scores.

| Boundary | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
|---|---:|---|---:|---|---:|---|
| Minimum score count | 0 | Reject | 1 | Accept | 2 | Accept |
| Maximum score count | 5 | Accept | 6 | Accept | 7 | Reject |

### Boundary Values

The important boundaries for `Roster` are:

- Minimum valid number of scores: `1`
- Maximum valid number of scores: `6`

---

## 3. Student Name Length Boundaries

The `validate_name()` function requires a name to contain between 1 and 50 characters.

| Boundary | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
|---|---:|---|---:|---|---:|---|
| Minimum name length | 0 | Reject | 1 | Accept | 2 | Accept |
| Maximum name length | 49 | Accept | 50 | Accept | 51 | Reject |

### Boundary Values

The important boundaries for `validate_name()` are:

- Minimum valid length: `1`
- Maximum valid length: `50`

---

## BVA Testing Strategy

Boundary Value Analysis complements Equivalence Partitioning from Lab 5.

Equivalence Partitioning tests representative values from each input class, while Boundary Value Analysis focuses on values immediately below, at, and immediately above important boundaries.

The combined EP and BVA tests provide better coverage and help detect off-by-one errors.
