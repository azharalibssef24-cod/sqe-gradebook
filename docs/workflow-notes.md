# Workflow Notes

## Lab 1 Task 5 — Idea to Release Workflow

The flow of a change through the project, from idea to release, follows these stages:

1. **Issue** — A new requirement or bug is logged as a GitHub Issue, describing the problem and
   expected outcome.
2. **Branch** — A feature or fix branch is created from `main`, named after its purpose
   (e.g. `feature/add-score`).
3. **Commits** — The change is implemented in small, atomic commits following Conventional
   Commits format.
4. **Pull Request (PR)** — The branch is pushed and a PR is opened, linking back to the original
   issue with "Closes #<n>".
5. **Review** — A reviewer (or self-review, for solo work) examines the diff, leaves comments,
   and requests changes if needed.
6. **Merge** — Once approved and checks pass, the PR is squash-merged into `main`, keeping
   history linear.
7. **CI** — Automated checks (tests, linting) run against the merged code to catch regressions.
8. **Release** — The verified `main` branch is tagged/released for use.

**Where QA typically intervenes:**
- At the **Issue** stage, to clarify acceptance criteria.
- At the **Review** stage, checking correctness, edge cases, and test coverage.
- At the **CI** stage, verifying automated checks catch regressions before merge.
- Before **Release**, doing a final sanity check that the build is stable.

---
