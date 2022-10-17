from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import as_declarative, declared_attr, sessionmaker

DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "192.168.88.223")
DB_NAME = "posts"
SQLALCHEMY_DATABASE_URL = (f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5433/{DB_NAME}")



engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)