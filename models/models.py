from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class AskQuestion(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(10))
    title = Column(String(50))
    genre = Column(String(20))
    description = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, nickname=none, title=None, genre=none, description=None, date=None):
        self.nickname = nickname
        self.title = title
        self.genre = genre
        self.description = description
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)