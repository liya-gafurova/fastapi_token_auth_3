from typing import Optional

from pydantic import BaseModel
from pydantic.schema import datetime


class PostRead(BaseModel):
    title: Optional[str]
    text: str
    created: datetime

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: Optional[str]
    text: str


class PostDB(PostCreate):
    pass
