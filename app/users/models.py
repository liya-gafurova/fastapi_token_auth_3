from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from sqlalchemy import Column, String, DateTime, func
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyBaseUserTableUUID

from app.db.base import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    email = Column(String(length=320), unique=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass