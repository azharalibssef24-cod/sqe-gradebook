class Student:
 feature/rename-field-b
    def __init__(self, name, id_number):
        self.name = name
        self.id_number=id_number

    def __init__(self, name, student_id):
        self.name = name
feature/rename-field-a
        self.student_id = student_id

        self.roll_no= roll_no
 main
 main
        self.scores = []
       def add_score(self, score):
            """Add a non-negative score to the student's score list."""
    if score < 0:
        raise ValueError("Score cannot be negative")
    self.scores.append(score)
