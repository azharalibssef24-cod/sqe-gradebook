
import pytest
from src.gradebook.gradebook import Student, Roster, percentile


def test_percentile_for_top_student():
    roster = Roster()

    s1 = Student("Ali", "P101")
    s1.add_score(90)
    roster.add_student(s1)

    s2 = Student("Ahmed", "P102")
    s2.add_score(70)
    roster.add_student(s2)

    assert percentile(s1, roster) == 100.0


def test_percentile_for_bottom_student():
    roster = Roster()

    s1 = Student("Ali", "P103")
    s1.add_score(90)
    roster.add_student(s1)

    s2 = Student("Ahmed", "P104")
    s2.add_score(70)
    roster.add_student(s2)

    assert percentile(s2, roster) == 0.0


def test_percentile_for_single_student():
    roster = Roster()

    s1 = Student("Sara", "P105")
    s1.add_score(85)
    roster.add_student(s1)

    assert percentile(s1, roster) == 100.0


def test_percentile_for_empty_roster():
    roster = Roster()

    with pytest.raises(ValueError):
        percentile(None, roster)
