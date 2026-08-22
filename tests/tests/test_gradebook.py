import pytest
from src.gradebook.gradebook import Student


def test_add_score_rejects_negative_score():
    student = Student("Test Student", "001")

    with pytest.raises(ValueError):
        student.add_score(-10)
