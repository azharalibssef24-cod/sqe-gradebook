import pytest

from src.gradebook.gradebook import Student, Roster


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (3, False),
    (8, True),
])
def test_roster_score_classes(score_count, expected_error):
    student = Student("Ali", f"student{score_count}")
    
    for score in range(score_count):
        student.add_score(50)

    roster = Roster()

    if expected_error:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        assert roster.add_student(student) is True
