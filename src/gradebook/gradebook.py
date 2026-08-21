class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []
       def add_score(self, score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    self.scores.append(score)
