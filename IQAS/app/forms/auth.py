from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.user import User


class RegisterForm(Form):
    username = StringField(validators=[DataRequired(message="用户名不能为空，请输入用户名"), Length(2, 7, message="昵称至少两个字符，最多七个字符")])
    password = PasswordField(validators=[DataRequired(message="密码名不能为空，请输入密码"), Length(5, 16)])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经被注册')

class LoginForm(Form):
    username = StringField(validators=[DataRequired(message="用户名不能为空，请输入你的用户名"), Length(2, 64)])
    password = PasswordField(validators=[DataRequired(message="密码不可以为空，请输入你的密码"), Length(3, 32)])