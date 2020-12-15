from .model import ENGINE, Todo
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=ENGINE)
session = Session()


class todoRepository:
    def __init__(self, title, note):
        self.title = title
        self.note = note

    def create(self):
        todo = Todo(title=self.title, notes=self.note, isDone=False)
        session.add(todo)
        session.commit()
        return "Todo Created"

    def selectAllNotDone(self):
        result = session.Query(Todo).filter(isDone=False)
        session.commit()
        return result

    def selectAllDone(self):
        result = session.Query(Todo).filter(isDone=True)
        session.commit()
        return result
