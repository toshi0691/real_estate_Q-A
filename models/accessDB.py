from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'realestate'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

ENGINE = None
SESSION = None

def read_data(name):
    local_session = SESSION()
    try:
        questions = local_session.query(AskQuestion).filter(AskQuestion.nickname=="pochi").all()

        for question in questions:
            print(question)

    finally:
        local_session.close()


if __name__ == "__main__":
    ENGINE = create_engine(CONNECT_STR)
    SESSION = sessionmaker(ENGINE)
    print('--------------- before select 1 ------------------------')
    print('  session:{}'.format(ENGINE.pool.status()))

    read_data('pochi')
    print('--------------- after select 1 ------------------------')
    print('  session:{}'.format(ENGINE.pool.status()))

    print('--------------- before select 2 ------------------------')
    print('  session:{}'.format(ENGINE.pool.status()))
    read_data('tama')




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