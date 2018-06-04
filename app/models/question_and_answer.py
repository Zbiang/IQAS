from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Questions_answers(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(15), nullable=False)
    answer = Column(String(200), nullable=False)
    update = Column(String(20))
    image = Column(String(50))