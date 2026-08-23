## Task 4 — Commit Hygiene Audit

**Last 10 commits (`git log --oneline -10`):**
```
9e681b4 docs: add Lab 1 Task 5 workflow notes
24787ba Add notes on merge conflict resolution for roll_no rename
29ff8cd Delete docs
5b2844a Create docs
3e7aac6 Delete docs
5858970 fix(gradebook): clean up broken merge, restore valid Student class
5e086f5 refactor(gradebook): rename roll_no to id_number (#4)
1a1bf78 refactor(gradebook): rename roll_no to student_id (#3)
1914867 Rename student_id to roll_no in Student class
f521844 Rename roll_no to student_id in Student class
```

**Weakest commit messages rewritten:**

1. Original: `Delete docs`
   Rewritten: `chore(docs): remove broken docs folder before recreating workflow-notes.md`
   Why it's better: The original gives no indication of *why* the folder was deleted or *what*
   it was replaced with. The rewritten version follows Conventional Commits format, names the
   type of change (`chore`), the affected scope (`docs`), and explains the reasoning.

2. Original: `Rename student_id to roll_no in Student class`
   Rewritten: `revert(gradebook): restore roll_no on main for Lab 2 Task 3 conflict exercise`
   Why it's better: The original only describes the mechanical change but not the intent. The
   rewritten version uses the `revert` type to signal this undoes a prior change, names the
   scope (`gradebook`), and explains why the revert was needed (to reset main before the
   deliberate conflict exercise).
