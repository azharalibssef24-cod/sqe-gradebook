
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


def test_rank_students_sorts_by_average_descending():
    roster = Roster()

    ali = Student("Ali", 102)
    ali.add_score(90)

    sara = Student("Sara", 103)
    sara.add_score(80)

    ahmed = Student("Ahmed", 104)
    ahmed.add_score(70)

    roster.add_student(ali)
    roster.add_student(sara)
    roster.add_student(ahmed)

    expected = [ali, sara, ahmed]

    assert rank_students(roster) == expected


def test_rank_students_sorts_equal_averages_alphabetically():
    roster = Roster()

    sara = Student("Sara", 105)
    sara.add_score(80)

    ali = Student("Ali", 106)
    ali.add_score(80)

    ahmed = Student("Ahmed", 107)
    ahmed.add_score(80)

    roster.add_student(sara)
    roster.add_student(ali)
    roster.add_student(ahmed)

    expected = [ahmed, ali, sara]

    assert rank_students(roster) == expected


def test_rank_students_places_zero_average_student_last():
    roster = Roster()

    ali = Student("Ali", 108)
    ali.add_score(90)

    sara = Student("Sara", 109)
    sara.add_score(50)

    ahmed = Student("Ahmed", 110)
    ahmed.add_score(0)

    roster.add_student(ahmed)
    roster.add_student(ali)
    roster.add_student(sara)

    expected = [ali, sara, ahmed]

    assert rank_students(roster) == expected
def test_rank_students_places_zero_average_student_last():
    roster = Roster()

    ali = Student("Ali", 108)
    ali.add_score(90)

    sara = Student("Sara", 109)
    sara.add_score(50)

    ahmed = Student("Ahmed", 110)
    ahmed.add_score(0)

    roster.add_student(ahmed)
    roster.add_student(ali)
    roster.add_student(sara)

    expected = [ali, sara, ahmed]

    assert rank_students(roster) == expected