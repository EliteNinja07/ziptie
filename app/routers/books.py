from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.schemas.books import Book, BookCreate, BookList
from app.models import Authors, Books
from app.database import get_db

router = APIRouter(prefix="/book", tags=["book"])


@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_author = db.query(Authors).filter(Authors.AuthorID == book.AuthorID).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    db_book = Books(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("/list/", response_model=List[BookList])
async def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(Books).options(joinedload(Books.authors)).offset(skip).limit(limit).all()
    return books
