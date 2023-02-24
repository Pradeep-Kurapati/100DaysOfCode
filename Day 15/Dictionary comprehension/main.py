import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score > 40}
print(passed_students)
