# GradeBook Defect Triage Log

## Sprint Triage Ranking

| Rank | Defect | Severity | Priority | Decision |
|------|--------|----------|----------|----------|
| 1 | average() crashes when Student has no scores | High | P1 | Fix this sprint |
| 2 | Student allows duplicate roll numbers | High | P1 | Fix this sprint |
| 3 | add_score() accepts negative scores | Medium | P1 | Fix this sprint |
| 4 | average() calculates incorrect rounded result | Medium | P2 | Won't fix this sprint |
| 5 | Student name comparison is case-sensitive | Low | P3 | Won't fix this sprint |

## Triage Rationale

### 1. Empty Score List Crash

This is ranked first because the application crashes when a basic gradebook operation is performed on a student with no scores. It has High severity and P1 priority, so it requires immediate attention.

### 2. Duplicate Roll Numbers

This is ranked second because duplicate roll numbers can cause incorrect student identification and unreliable records. It has High severity and P1 priority, making it important to fix during this sprint.

### 3. Negative Scores Accepted

This is ranked third because invalid negative scores can enter the gradebook and affect grade calculations. It has Medium severity but P1 priority because incorrect grade data should be corrected promptly.

### 4. Incorrect Average Rounding

This issue has Medium severity and P2 priority. Although it can produce inaccurate grade information, it does not prevent the system from operating, so it can be deferred to a later sprint.

### 5. Case-Sensitive Name Comparison

This issue has Low severity and P3 priority. It has limited impact on the core gradebook functionality and can therefore be deferred.

## Severity vs Priority Trade-offs

The negative-score defect demonstrates that severity and priority are independent. Its technical impact is Medium because it allows invalid data, but its P1 priority means it should still be fixed promptly because incorrect scores can affect grades.

The average-rounding defect is also Medium severity, but it has P2 priority because it affects numerical accuracy without preventing the gradebook from operating. Therefore, it can be scheduled after more urgent defects.

## Sprint Decision

The three highest-priority defects selected for this sprint are:

1. Empty score list crash
2. Duplicate roll numbers
3. Negative scores accepted

The following two defects will not be fixed during this sprint:

- Incorrect average rounding
- Case-sensitive name comparison
