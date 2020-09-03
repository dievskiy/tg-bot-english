import sqlalchemy

posts_metadata = sqlalchemy.MetaData()

posts_table = sqlalchemy.Table(
    "posts",
    posts_metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("english", sqlalchemy.String(), nullable=False),
    sqlalchemy.Column("russian", sqlalchemy.String(), nullable=False),
    sqlalchemy.Column("example", sqlalchemy.String(), nullable=False),
)
