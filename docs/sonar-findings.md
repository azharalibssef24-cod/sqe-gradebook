# SonarCloud Findings Report

## 1. Project Information

- **Project:** GradeBook
- **Repository:** azharalibssef24-cod/sqe-gradebook
- **Analysis Tool:** SonarCloud
- **Branch:** main
- **Analysis Type:** Static Code Analysis

## 2. Initial Analysis Findings

The initial SonarCloud analysis reported four Medium-severity security issues in the GitHub Actions workflow.

| No. | File | Location | Severity | Finding | Resolution |
|---|---|---|---|---|---|
| 1 | `.github/workflows/tests.yml` | Line 22 | Medium | Pip installation did not use `--only-binary :all:`. | Added `--only-binary :all:`. |
| 2 | `.github/workflows/tests.yml` | Line 22 | Medium | Dependency version was not locked. | Pinned pytest to version 9.1.1. |
| 3 | `.github/workflows/tests.yml` | Line 23 | Medium | Pip installation did not use `--only-binary :all:`. | Added `--only-binary :all:`. |
| 4 | `.github/workflows/tests.yml` | Line 23 | Medium | Dependency version was not locked. | Pinned pytest to version 9.1.1. |

These findings were addressed by securing the dependency installation commands in the GitHub Actions workflow.

## 3. Initial Analysis Warnings

SonarCloud also reported two configuration warnings:

1. **Python version configuration:** SonarCloud recommended specifying the Python version. This was addressed by setting `sonar.python.version=3.12`.
2. **Test directory configuration:** SonarCloud recommended configuring the test directory. This was addressed using `sonar.tests=tests` and `sonar.test.inclusions=tests/**/*.py`.

These were configuration warnings, not additional code issues.

## 4. Coverage Configuration

Initially, SonarCloud reported 0.0% coverage because no coverage report was being imported.

This was resolved by:

- Installing the Coverage Python package.
- Running pytest with coverage measurement.
- Generating `coverage.xml`.
- Configuring `sonar.python.coverage.reportPaths=coverage.xml`.
- Updating GitHub Actions to generate the report