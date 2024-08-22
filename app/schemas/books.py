from typing import List

from pydantic import BaseModel

from app.schemas.authors import Author


class BookBase(BaseModel):
    Title: str
    Genre: str
    PublicationYear: int

class BookCreate(BookBase):
    AuthorID: int

class Book(BookBase):
    BookID: int

    class Config:
        from_attributes = True

class BookList(BookBase):
    BookID: int
    authors: Author
    
    class Config:
        from_attributes = True
