import pytest

from src.gradebook.gradebook import Student, Roster


def test_roster_accepts_valid_student(student_with_scores):
    # Arrange
    student = student_with_scores
    roster = Roster()

    # Act
    result = roster.add_student(student)

    # Assert
    assert result is True


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (3, False),
    (8, True),
])
def test_roster_score_classes(score_count, expected_error):
    # Arrange
    student = Student("Ali", f"student{score_count}")

    for score in range(score_count):
        student.add_score(50)

    roster = Roster()

    # Act + Assert
    if expected_error:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        assert roster.add_student(student) is True


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (1, False),
    (2, False),
    (5, False),
    (6, False),
    (7, True),
])
def test_roster_score_count_boundaries(score_count, expected_error):
    # Arrange
    student = Student("BVA Student", f"bva_student_{score_count}")

    for score in range(score_count):
        student.add_score(50)

    roster = Roster()

    # Act + Assert
    if expected_error:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        assert roster.add_student(student) is True
