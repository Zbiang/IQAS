from flask_login import UserMixin
from sqlalchemy import Integer, Column, String
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from app.models.base import Base

class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
# @login_manager.user_loader
# def get_user(user_id):
#     return User.query.get(int(uid))



