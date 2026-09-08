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
