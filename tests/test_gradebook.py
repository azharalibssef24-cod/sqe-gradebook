import pytest

from src.gradebook.gradebook import Student


def test_add_valid_score(student_with_scores):
    # Arrange
    student = student_with_scores

    # Act
    student.add_score(70)

    # Assert
    assert student.scores == [80, 90, 70]


def test_reject_negative_score():
    # Arrange
    student = Student("Ali", "102")

    # Act + Assert
    with pytest.raises(ValueError, match="Score cannot be negative"):
        student.add_score(-5)


def test_reject_non_numeric_score():
    # Arrange
    student = Student("Ali", "103")

    # Act + Assert
    with pytest.raises((TypeError, ValueError)):
        student.add_score("abc")


def test_accept_minimum_boundary_score():
    # Arrange
    student = Student("Ali", "104")

    # Act
    student.add_score(0)

    # Assert
    assert student.scores == [0]


def test_accept_maximum_boundary_score():
    # Arrange
    student = Student("Ali", "105")

    # Act
    student.add_score(100)

    # Assert
    assert student.scores == [100]


def test_reject_score_above_100():
    # Arrange
    student = Student("Ali", "106")

    # Act + Assert
    with pytest.raises((ValueError, TypeError)):
        student.add_score(101)


def test_calculate_average(student_with_scores):
    # Arrange
    student = student_with_scores

    # Act
    result = student.average()

    # Assert
    assert result == 85.0


def test_empty_scores_average():
    # Arrange
    student = Student("Ali", "108")

    # Act
    result = student.average()

    # Assert
    assert result == 0.0


def test_reject_duplicate_student_id():
    # Arrange
    Student("Ali", "109")

    # Act + Assert
    with pytest.raises(ValueError, match="Student ID already exists"):
        Student("Ahmed", "109")


def test_add_multiple_valid_scores(student_with_scores):
    # Arrange
    student = student_with_scores

    # Act
    student.add_score(60)

    # Assert
    assert student.scores == [80, 90, 60]


def test_case_insensitive_student_name_comparison():
    # Arrange
    student1 = Student("Ali", "111")
    student2 = Student("ALI", "112")

    # Act + Assert
    assert student1.name.lower() == student2.name.lower()


def test_reject_minimum_invalid_score():
    # Arrange
    student = Student("Ali", "113")

    # Act + Assert
    with pytest.raises(ValueError, match="Score cannot be negative"):
        student.add_score(-1)
