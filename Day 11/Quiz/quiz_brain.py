class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_questions(self, question_number):
        total = len(self.question_list)
        return not question_number == total


    def next_question(self):
        while self.still_has_questions(self.question_number):
            current = self.question_list[self.question_number]
            self.question_number += 1
            choice = input(f"Q{self.question_number}. {current.text} (True/False): ")
            self.check_answer(choice, current.answer)

    def check_answer(self,choice, correct):
        if choice.lower() == correct.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was {correct}")
        print(f"Your score: {self.score}/{len(self.question_list)}")



