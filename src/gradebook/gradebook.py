   class Student:
       def __init__(self, name, student_id):
           self.name = name
           self.student_id = student_id
           self.scores = []

       def add_score(self, score):
           """Add a non-negative score to the student's score list."""
           if score < 0:
               raise ValueError("Score cannot be negative")
           self.scores.append(score)
