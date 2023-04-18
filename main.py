from question_model import Questions
from data import question_data

question_data = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text,question_answer)
    question_data.append(new_question)

print(question_data[0].answer)
