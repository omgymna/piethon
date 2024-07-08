from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


score = 0
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Your final score is: {quiz.score}/{len(question_bank)} \n")



# while len(question_bank) > 0:
    
#     random_question = random.choice(question_bank)

#     print(random_question.text)
#     guess = input("True or False? ")

#     if guess == random_question.answer:
#         score += 1
#         print("That's correct!")
#         question_bank.remove(random_question)
#     else:
#         print("That's not correct.")
#         question_bank.remove(random_question)

# print(f"Quiz over. Your final score is {score}.")