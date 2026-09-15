import pytest

from src.gradebook.gradebook import validate_name


@pytest.mark.parametrize('name', [
    'Ali Khan',
    'Ali-Khan',
    'A'
])
def test_validate_name_valid_classes(name):
    assert validate_name(name) is True


@pytest.mark.parametrize('name', [
    '',
    'A' * 51,
    'Ali123',
    'Ali@Khan'
])
def test_validate_name_invalid_classes(name):
    with pytest.raises(ValueError):
        validate_name(name)
@pytest.mark.parametrize('length,expected_error', [
    (0, True),
    (1, False),
    (49, False),
    (50, False),
    (51, True),
])
def test_validate_name_length_boundaries(length, expected_error):
    name = 'A' * length

    if expected_error:
        with pytest.raises(ValueError):
            validate_name(name)
    else:
        assert validate_name(name) is True
