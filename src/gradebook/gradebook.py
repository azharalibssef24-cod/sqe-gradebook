class Student:
    student_ids = set()

    def __init__(self, name, student_id):
        if student_id in Student.student_ids:
            raise ValueError("Student ID already exists")

        self.name = name
        self.student_id = student_id
        self.scores = []

        Student.student_ids.add(student_id)

    def add_score(self, score):
        """Add a score between 0 and 100 to the student's score list."""
        if score < 0:
            raise ValueError("Score cannot be negative")
        if score > 100:
            raise ValueError("Score cannot be greater than 100")
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score <= 59:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"
        
class Roster:
    def add_student(self, student):
        score_count = len(student.scores)

        if score_count < 1 or score_count > 6:
            raise ValueError("Student must have 1 to 6 scores")

        return True
