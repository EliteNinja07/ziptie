from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload

from app.schemas.authors import Author, AuthorCreate
from app.models import Authors
from app.database import get_db

router = APIRouter(prefix="/author", tags=["author"])


@router.post("/", response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Authors(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

