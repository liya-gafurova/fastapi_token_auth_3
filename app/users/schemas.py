import uuid
from typing import Optional, Generic

from fastapi_users import models as models
from fastapi_users.schemas import BaseUserCreate, BaseUser, BaseUserUpdate, CreateUpdateDictModel
from pydantic import BaseModel


class UserRead(CreateUpdateDictModel):
    username: str


    id: uuid.UUID
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(CreateUpdateDictModel):
    username: str
    password: str
    is_superuser: Optional[bool] = False


class UserUpdate( BaseUserUpdate):
    pass
