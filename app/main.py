from fastapi import FastAPI

from app.posts.api import router
from app.users.auth_logic import fastapi_users, auth_backend
from app.users.schemas import UserRead, UserCreate, UserUpdate

app = FastAPI()

app.include_router(router=router, prefix='/posts')

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/token", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)