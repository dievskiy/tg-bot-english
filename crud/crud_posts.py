from models.posts import Post
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func


def create_new_post(db: Session, english: str, russian, example):
    db.execute(
        "insert into posts(english, russian, example) values (\'{}\', \'{}\', \'{}\');".format(
            english.replace("'", "''"), russian,
            example.replace("'", "''")))


def get_random_post(db: Session) -> Post:
    return db.query(Post).order_by(func.random()).first()
