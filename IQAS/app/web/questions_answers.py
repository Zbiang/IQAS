from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required

from app.forms.questions_answers import Add_change_question
from app.models.base import db
from app.models.question_and_answer import Questions_answers
from . import web

@web.route('/questions_answers', methods=['GET', 'POST'])
@login_required
def questions_answers():
    questions = Questions_answers.query.filter_by(status=1).all()
    return render_template('questions_answers.html', questions=questions)

@web.route('/questions_answers/add', methods=['GET', 'POST'])
@login_required
def add_question():
    form = Add_change_question(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            question = Questions_answers()
            question.set_attrs(form.data)
            db.session.add(question)
    return redirect(url_for('web.questions_answers'))

@web.route('/questions_answers/delete/<question_id>', methods=['GET', 'POST'])
@login_required
def delete_question(question_id):
    question = Questions_answers.query.filter_by(id=question_id).first()
    if not question:
        flash('该问题已经不存在，删除失败')
    with db.auto_commit():
        question.delete()
    return redirect(url_for('web.questions_answers'))

@web.route('/questions_answers/change', methods=['GET', 'POST'])
@login_required
def change_question():
    return redirect(url_for('web.questions_answers'))