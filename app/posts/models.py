from sqlalchemy import String, Column, Integer, Text, DateTime, func

from app.db.base_class import Base


class Posts(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200))
    text = Column(Text)
    created = Column(DateTime(timezone=True), server_default=func.now())


