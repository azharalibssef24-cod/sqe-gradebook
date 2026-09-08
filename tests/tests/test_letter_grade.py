from src.gradebook.gradebook import letter_grade


@pytest.mark.parametrize('score,expected', [
    (45, 'F'),
    (65, 'D'),
    (75, 'C'),
    (85, 'B'),
    (95, 'A'),
])
def test_letter_grade_valid_classes(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize('score', [-10, 150])
def test_letter_grade_invalid_classes(score):
    with pytest.raises(ValueError):
        letter_grade(score)
