# from question_model import Question
# from data import question_data
#
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question("answer")
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

class QuizBrain:

    def __init__ (self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_nuumber += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
