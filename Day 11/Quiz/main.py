from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    text = x["question"]
    answer = x["correct_answer"]
    question_bank.append(Question(text, answer))

new_method = QuizBrain(question_bank)
new_method.next_question()


