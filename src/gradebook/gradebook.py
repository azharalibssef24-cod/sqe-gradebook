
class GradeBookIOError(Exception):
    """Custom exception for file operation errors."""
    pass


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
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be numeric")

        if score < 0:
            raise ValueError("Score cannot be negative")

        if score > 100:
            raise ValueError("Score cannot be greater than 100")

        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        score_count = len(student.scores)

        if score_count < 1 or score_count > 6:
            raise ValueError("Student must have 1 to 6 scores")

        self.students.append(student)
        return True

    def class_average(self):
        if not self.students:
            return 0.0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def save_to_file(self, path):
        try:
            if not self.students:
                content = "GradeBook Roster\n"
            else:
                content = ""

                for student in self.students:
                    content += (
                        f"Name: {student.name}, "
                        f"ID: {student.student_id}, "
                        f"Average: {student.average()}\n"
                    )

            with open(path, "w") as file:
                file.write(content)

        except OSError as error:
            raise GradeBookIOError(
                "Unable to save roster to file"
            ) from error


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


def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")

    if len(name) == 0 or len(name) > 50:
        raise ValueError("Name must be between 1 and 50 characters")

    for char in name:
        if not (char.isalpha() or char in " -"):
            raise ValueError(
                "Name can contain only letters, spaces, and hyphens"
            )

    return True

def percentile(student, roster):
    students = sorted(roster.students, key=lambda s: s.average())
    rank_index = students.index(student)
    total_students = len(students)

    result = (rank_index / total_students) * 100
    return result
