
import pytest
from unittest.mock import mock_open, patch
from src.gradebook.gradebook import Student, Roster, GradeBookIOError


# Module-scope fixture: runs once for the entire test module.
@pytest.fixture(scope="module")
def module_setup():
    return {"environment": "GradeBook testing"}


# Function-scope fixture: creates a fresh student for each test.
@pytest.fixture
def student(module_setup):
    Student.student_ids.clear()
    return Student("Ali", "101")


# Task 4: Parametrized testing
@pytest.mark.parametrize(
    "score, expected",
    [
        (0, "valid"),
        (50, "valid"),
        (100, "valid"),
        (-5, "negative"),
        (105, "above"),
        (150, "above"),
    ],
    ids=[
        "zero-score",
        "normal-score",
        "maximum-score",
        "negative-score",
        "above-100-score",
        "high-score",
    ]
)
def test_add_score_parametrized(student, score, expected):
    if expected == "valid":
        student.add_score(score)
        assert score in student.scores

    elif expected == "negative":
        with pytest.raises(ValueError, match="Score cannot be negative"):
            student.add_score(score)

    elif expected == "above":
        with pytest.raises(
            ValueError,
            match="Score cannot be greater than 100"
        ):
            student.add_score(score)


# Other Student tests

def test_empty_average(student):
    assert student.average() == 0.0


def test_single_score_average(student):
    student.add_score(80)
    assert student.average() == 80.0


def test_multiple_scores_average(student):
    student.add_score(80)
    student.add_score(90)
    student.add_score(70)
    assert student.average() == 80.0


def test_duplicate_student_id(student):
    with pytest.raises(ValueError, match="Student ID already exists"):
        Student("Ahmed", "101")


def test_student_name(student):
    assert student.name == "Ali"


def test_student_starts_with_empty_scores(student):
    assert student.scores == []


def test_module_fixture(module_setup):
    assert module_setup["environment"] == "GradeBook testing"


# Roster tests

def test_empty_roster_average():
    roster = Roster()
    assert roster.class_average() == 0.0


def test_single_student_class_average(student):
    student.add_score(80)

    roster = Roster()
    roster.add_student(student)

    assert roster.class_average() == 80.0


def test_multiple_students_class_average(student):
    student.add_score(80)

    student2 = Student("Ahmed", "102")
    student2.add_score(70)

    student3 = Student("Sara", "103")
    student3.add_score(90)

    roster = Roster()
    roster.add_student(student)
    roster.add_student(student2)
    roster.add_student(student3)

    assert roster.class_average() == 80.0


# Mocking tests

def test_save_to_file_success(student):
    student.add_score(80)

    roster = Roster()
    roster.add_student(student)

    mocked_file = mock_open()

    with patch("builtins.open", mocked_file):
        roster.save_to_file("gradebook.txt")

    mocked_file.assert_called_once_with("gradebook.txt", "w")

    handle = mocked_file()
    handle.write.assert_called_once_with(
        "Name: Ali, ID: 101, Average: 80.0\n"
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

    with patch("builtins.open", side_effect=OSError("Disk error")):
        with pytest.raises(GradeBookIOError):
            roster.save_to_file("gradebook.txt")
