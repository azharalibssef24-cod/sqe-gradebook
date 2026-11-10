# Code Review Checklist — GradeBook

## 1. Correctness
- [ ] Does the code perform the required functionality correctly?
- [ ] Are boundary conditions and edge cases handled properly?
- [ ] Are calculations and conditions logically correct?

## 2. Testing
- [ ] Are appropriate unit tests provided for the new functionality?
- [ ] Do tests cover normal cases, invalid inputs, and edge cases?
- [ ] Do all existing tests pass without breaking previous functionality?

## 3. Readability
- [ ] Are variable and function names meaningful?
- [ ] Is the code properly formatted and consistently indented?
- [ ] Are docstrings or comments provided where necessary?

## 4. Design
- [ ] Does the new code follow the existing project structure?
- [ ] Is unnecessary code duplication avoided?
- [ ] Is the implementation simple and maintainable?

## 5. Risk
- [ ] Does the code validate user input properly?
- [ ] Could the changes introduce security or performance problems?
- [ ] Could the changes break existing GradeBook functionality?

### Lessons Learned

1. Code reviews help identify incorrect formulas and missing edge-case handling.
2. Empty rosters and single-student rosters require explicit validation.
3. Descriptive variable names and docstrings improve code readability.
4. Unit tests help verify correctness after review feedback.
5. Reviewing student membership prevents invalid input from producing unexpected results.
6. GitHub inline comments provide a clear way to communicate code improvements.
7. Formal review approval was not recorded because the PR author could not formally approve their own pull request.
8. All automated checks passed before merging the pull request.