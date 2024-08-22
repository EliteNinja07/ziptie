from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.models import Authors

class Books(Base):
    __tablename__ = "books"

    BookID = Column(Integer, primary_key=True, index=True)
    Title = Column(String(100), nullable=False)
    Genre = Column(String(50), nullable=False)
    PublicationYear = Column(Integer, nullable=False)
    AuthorID = Column(Integer, ForeignKey('authors.AuthorID'))

    authors = relationship("Authors", back_populates="books")
