from sqlalchemy import Boolean, Column, Integer, String
from models.base import Base


class Post(Base):
    _table_name = "posts"
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, index=True, nullable=False)
    russian = Column(String, index=True, nullable=False)
    example = Column(String, index=True, nullable=False)

    def __repr__(self):
        return "id = {}, eng = {}, rus = {}, \n ex = {}".format(self.id, self.english, self.russian, self.example)
