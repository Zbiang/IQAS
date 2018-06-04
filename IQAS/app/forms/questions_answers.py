from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.question_and_answer import Questions_answers


class Add_change_question(Form):
    question = StringField(validators=[DataRequired(message='问题不能为空，请填写问题'), Length(1, 25, message='问题长度大于5小于25')])
    answer = StringField(validators=[DataRequired(message='答案不能为空，请填写问题对应的答案'), Length(1, 200, message="答案的长度要合理")])

    def validate_question(self, field):
        if Questions_answers.query.filter_by(question=field.data,status=1).first():
            raise ValidationError('相应的问题已存在')