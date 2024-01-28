from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for q in question_data:
  new_question = q["question"]
  new_answer = q["correct_answer"]
  new_q = Question(new_question, new_answer)
  question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()



