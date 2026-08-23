class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number=id_number
        self.scores = []
       def add_score(self, score):
            """Add a non-negative score to the student's score list."""
    if score < 0:
        raise ValueError("Score cannot be negative")
    self.scores.append(score)
