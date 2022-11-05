from data import question_data
from question_model import Question
from quizeBrain import QuizBrain

question_store = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_store.append(new_question)

quiz = QuizBrain(question_store)

while quiz.still_has_question():
    quiz.next_question()
    print("You have completed the quiz")
    print(f"You final score is: {quiz.score}/{quiz.question_number}")

