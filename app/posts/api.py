import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.posts.schemas import PostRead, PostCreate
from app.posts.models import Posts
from app.users.auth_logic import current_active_user

router = APIRouter()


@router.get('', response_model=List[PostRead])
async def posts(user = Depends(current_active_user), db: Session = Depends(get_db)):
    posts_db = db.query(Posts).offset(0).limit(10).all()
    return posts_db


@router.post('/create', response_model=PostRead)
async def create_post(post: PostCreate, user = Depends(current_active_user), db: Session = Depends(get_db)):
    print(user)
    db_obj = Posts(**post.dict())  # type: ignore
    db.add(db_obj)
    db.commit()

    db.refresh(db_obj)
    return db_obj
