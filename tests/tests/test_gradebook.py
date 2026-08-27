import pytest
from src.gradebook.gradebook import Student


def test_add_score_rejects_negative_score():
    student = Student("Test Student", "001")

    with pytest.raises(ValueError):
        student.add_score(-10)
        def test_add_score_rejects_negative_score():
    student = Student("Ali", 101)

    with pytest.raises(ValueError):
        student.add_score(-10)
def test_average_calculates_accurately():
    student = Student("Ali", 102)
    student.add_score(80)
    student.add_score(81)
    student.add_score(82)

    assert student.average() == 81.0
