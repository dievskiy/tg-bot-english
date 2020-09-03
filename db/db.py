from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.session import close_all_sessions

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://admin:pass@127.0.0.1:5432/idioms"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(bind=engine)


def close_sessions():
    close_all_sessions()
