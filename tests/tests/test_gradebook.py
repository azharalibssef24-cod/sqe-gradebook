import pytest
from src.gradebook.gradebook import Student


def test_add_valid_score():
    student = Student("Ali", "101")
    student.add_score(80)

    assert student.scores == [80]


def test_reject_negative_score():
    student = Student("Ali", "102")

    with pytest.raises(ValueError, match="Score cannot be negative"):
        student.add_score(-5)


def test_reject_non_numeric_score():
    student = Student("Ali", "103")

    with pytest.raises((TypeError, ValueError)):
        student.add_score("abc")


def test_accept_minimum_boundary_score():
    student = Student("Ali", "104")
    student.add_score(0)

    assert student.scores == [0]


def test_accept_maximum_boundary_score():
    student = Student("Ali", "105")
    student.add_score(100)

    assert student.scores == [100]


def test_reject_score_above_100():
    student = Student("Ali", "106")

    with pytest.raises((ValueError, TypeError)):
        student.add_score(101)


def test_calculate_average():
    student = Student("Ali", "107")
    student.add_score(80)
    student.add_score(70)
    student.add_score(90)

    assert student.average() == 80.0


def test_empty_scores_average():
    student = Student("Ali", "108")

    assert student.average() == 0.0


def test_reject_duplicate_student_id():
    Student("Ali", "109")

    with pytest.raises(ValueError, match="Student ID already exists"):
        Student("Ahmed", "109")


def test_add_multiple_valid_scores():
    student = Student("Ali", "110")
    student.add_score(60)
    student.add_score(80)
    student.add_score(90)

    assert student.scores == [60, 80, 90]


def test_case_insensitive_student_name_comparison():
    student1 = Student("Ali", "111")
    student2 = Student("ALI", "112")

    assert student1.name.lower() == student2.name.lower()


def test_reject_minimum_invalid_score():
    student = Student("Ali", "113")

    with pytest.raises(ValueError, match="Score cannot be negative"):
        student.add_score(-1)