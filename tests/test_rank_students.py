from src.gradebook.gradebook import Roster, rank_students


def test_rank_students_empty_roster_returns_empty_list():
    roster = Roster()

    assert rank_students(roster) == []