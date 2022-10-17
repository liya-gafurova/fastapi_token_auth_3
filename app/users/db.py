from os import environ
from typing import AsyncGenerator, Optional

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from fastapi_users.models import UP
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.users import User
from app.users.models import AccessToken

DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "192.168.88.223")
DB_NAME = "posts"
SQLALCHEMY_DATABASE_URL = (f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5433/{DB_NAME}")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class SQLAlchemyUserDatabaseCustom(SQLAlchemyUserDatabase):
    async def get_by_username(self, username: str) -> Optional[UP]:
        statement = select(self.user_table).where(
            func.lower(self.user_table.username) == func.lower(username)
        )
        return await self._get_user(statement)



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabaseCustom(session, User)

async def get_access_token_db(
        session: AsyncSession = Depends(get_async_session),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)

