import pytest

from src.gradebook.gradebook import Student


@pytest.fixture
def student_with_scores():
    # Function scope is the default.
    # A new student is created for each test, which keeps tests independent.
    student = Student("Test Student", "fixture_student")
    student.add_score(80)
    student.add_score(90)
    return student


@pytest.fixture(scope="module")
def shared_test_names():
    # Module scope is useful for expensive setup that can safely
    # be shared by all tests in one test module.
    return ["Ali", "Sara", "Ahmed"]
