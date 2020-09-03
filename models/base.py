from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically if has not defined table name
    @declared_attr
    def __tablename__(cls) -> str:
        if not hasattr(cls, '_table_name'):
            return cls.__name__.lower()
        return cls._table_name
