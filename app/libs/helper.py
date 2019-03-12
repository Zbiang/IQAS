def get_all_questions(questions_and_answers):
    questions = []
    for question_and_answer in questions_and_answers:
        questions.append(question_and_answer.question)
    return questions

def get_all_answers(questions_and_answers):
    answers = []
    for question_and_answer in questions_and_answers:
        answers.append(question_and_answer.answer)
    return answers