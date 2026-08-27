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
        """Add a non-negative score to the student's score list."""
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
