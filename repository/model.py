from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Boolean

ENGINE = create_engine(
    'postgresql+psycopg2://postgres:root@localhost/todo')
BASE = declarative_base()


class Todo(BASE):
    __tablename__ = 'Todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    notes = Column(String(200))
    isDone = Column(Boolean)

    def __str__(self):
        return self.title, self.notes


BASE.metadata.create_all(ENGINE)
