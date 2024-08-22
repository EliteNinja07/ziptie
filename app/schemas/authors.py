from pydantic import BaseModel, EmailStr
from datetime import date

class AuthorBase(BaseModel):
    Name: str
    BirthDate: date
    Country: str
    Email: EmailStr

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    AuthorID: int

    class Config:
        from_attributes = True
