import json

from flask import request

from app.libs.helper import get_all_questions, get_all_answers
from app.libs.nlp import nlp
from app.models.question_and_answer import Questions_answers
from . import web

messages = [
    {
        'message': "你想了解什么",
        'index': 're'
    }
]

re_messages = []

@web.route('/send_message', methods=['POST'])
def send_message():
    form = request.form
    form.index = 'send'
    questions = Questions_answers.query.filter_by(status=1).all()
    questions = get_all_questions(questions)
    answers = Questions_answers.query.filter_by(status=1).all()
    answers = get_all_answers(answers)
    question = form['message']
    r_question = nlp(question, questions, answers)
    re_message = {
        'message': r_question,
        'index': 're'
    }
    # re_messages.append(re_message)
    messages.append(form)
    for i in range(len(messages)):
        if i % 2 == 1 and (i + 4) == len(messages)-1:
            if messages[i] == messages[i+2] and messages[i+4] == messages[i]:
                m = {
                    'message': "怎么老是问同一个问题呀_(:з)∠)_...",
                    'index': 're'
                }
                messages.append(m)
    if type(messages[-1]) != dict:
        messages.append(re_message)
    return json.dumps(re_message)

# @web.route('/revie_message', methods=['POST', 'GET'])
# @login_required
# def revie_message():
#     form = request.form
#     print('提交的：', form)
#     print("messages:", messages)
#     form = "问题过于智障，不愿意回答"
#     messages.append(form)
#     print('智障聊天记录：', messages)
#     return redirect(url_for('web.index'))

"""
jieba库调用问题
聊天框的移动问题
flash问题
# 问题的可编辑性
# 界面问题的缩略性
"""