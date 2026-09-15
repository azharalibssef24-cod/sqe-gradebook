import pytest

from src.gradebook.gradebook import letter_grade


@pytest.mark.parametrize('score,expected', [
    (-1, None),
    (0, 'F'),
    (1, 'F'),
    (59, 'F'),
    (60, 'D'),
    (61, 'D'),
    (69, 'D'),
    (70, 'C'),
    (71, 'C'),
    (79, 'C'),
    (80, 'B'),
    (81, 'B'),
    (89, 'B'),
    (90, 'A'),
    (91, 'A'),
    (99, 'A'),
    (100, 'A'),
    (101, None),
])
def test_letter_grade_boundaries(score, expected):
    if expected is None:
        with pytest.raises(ValueError):
            letter_grade(score)
    else:
        assert letter_grade(score) == expected
