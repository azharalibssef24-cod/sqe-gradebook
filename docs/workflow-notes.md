## Task 3 — Merge Conflict: roll_no Rename

**What caused the conflict:**
Two branches, `feature/rename-field-a` and `feature/rename-field-b`, were both created to rename
the `roll_no` field in the `Student` class. `feature/rename-field-a` renamed it to `student_id`,
while `feature/rename-field-b` renamed it to `id_number`. Since both branches modified the exact
same lines in `src/gradebook/gradebook.py`, Git could not automatically decide which version to
keep when the second branch was merged after the first.

**How it was resolved:**
The first PR (`feature/rename-field-a`) was merged into `main`, updating the field to `student_id`.
When the second PR (`feature/rename-field-b`) was merged, GitHub flagged a conflict on the same
lines. The conflict markers were resolved by keeping a single consistent version of the `Student`
class using `student_id` as the field name, since that was the version already merged into `main`.
The file was cleaned up and committed directly to `main` to restore a valid, working state.

**Lesson learned:**
When two branches independently rename the same field, only one naming decision can survive the
merge. Conflicts like this are best avoided by coordinating naming decisions before branching, or
by keeping renames to short-lived branches merged in quick succession.
