from flask import render_template, redirect, url_for, request, flash
from flask_login import logout_user, login_user

from app.forms.auth import LoginForm, RegisterForm
from app.models.base import db
from app.models.user import User
from . import web

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('register.html', form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码不正确')
    return render_template('login.html', form=form)

@web.route('/logout', methods=['POST','GET'])
def logout():
    logout_user()
    return redirect(url_for('web.login'))