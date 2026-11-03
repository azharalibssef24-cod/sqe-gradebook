
import pytest
from unittest.mock import mock_open, patch

from src.gradebook.gradebook import (
    Student,
    Roster,
    GradeBookIOError,
)


# Module-scope fixture: runs once for this module.
@pytest.fixture(scope="module")
def module_setup():
    return {"course": "Software Quality Engineering"}


# Function-scope fixture: creates a fresh student for each test.
@pytest.fixture
def student():
    Student.student_ids.clear()
    return Student("Ali", "101")


@pytest.fixture
def student_with_scores(student):
    student.add_score(80)
    student.add_score(90)
    return student


def test_module_fixture(module_setup):
    assert module_setup["course"] == "Software Quality Engineering"


@pytest.mark.parametrize(
    "score, expected_error",
    [
        (0, False),
        (50, False),
        (100, False),
        (-5, True),
        (101, True),
        ("abc", True),
    ],
    ids=[
        "zero-score",
        "normal-score",
        "maximum-score",
        "negative-score",
        "above-100-score",
        "high-score",
    ],
)
def test_add_score_parametrized(score, expected_error, student):
    if expected_error:
        with pytest.raises((ValueError, TypeError)):
            student.add_score(score)
    else:
        student.add_score(score)
        assert student.scores == [score]


def test_empty_average(student):
    assert student.average() == 0.0


def test_single_score_average(student):
    student.add_score(80)
    assert student.average() == 80.0


def test_multiple_scores_average(student_with_scores):
    assert student_with_scores.average() == 85.0


def test_duplicate_student_id(student):
    with pytest.raises(ValueError, match="Student ID already exists"):
        Student("Ahmed", "101")


def test_student_name(student):
    assert student.name == "Ali"


def test_student_starts_with_empty_scores(student):
    assert student.scores == []


def test_empty_roster_average():
    roster = Roster()
    assert roster.class_average() == 0.0


def test_single_student_class_average(student_with_scores):
    roster = Roster()
    roster.add_student(student_with_scores)

    assert roster.class_average() == 85.0


def test_multiple_students_class_average(student_with_scores):
    roster = Roster()
    roster.add_student(student_with_scores)

    second_student = Student("Sara", "102")
    second_student.add_score(70)
    roster.add_student(second_student)

    assert roster.class_average() == 77.5


def test_save_to_file_success(student_with_scores):
    roster = Roster()
    roster.add_student(student_with_scores)

    fake_file = mock_open()

    with patch("builtins.open", fake_file):
        roster.save_to_file("test.txt")

    fake_file.assert_called_once_with("test.txt", "w")

    fake_file().write.assert_called_once_with(
        "Name: Ali, ID: 101, Average: 85.0\n"
    )


def test_save_to_file_error(student_with_scores):
    roster = Roster()
    roster.add_student(student_with_scores)

    with patch(
        "builtins.open",
        side_effect=OSError("File error")
    ):
        with pytest.raises(GradeBookIOError):
            roster.save_to_file("test.txt")
