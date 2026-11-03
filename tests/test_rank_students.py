
from src.gradebook.gradebook import Roster, Student, rank_students


def test_rank_students_empty_roster_returns_empty_list():
    roster = Roster()

    assert rank_students(roster) == []


def test_rank_students_single_student_returns_that_student():
    roster = Roster()

    student = Student("Ali", 101)
    student.add_score(85)
    roster.add_student(student)

    assert rank_students(roster) == [student]
