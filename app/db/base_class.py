from os import environ

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import as_declarative, declared_attr, sessionmaker




@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

