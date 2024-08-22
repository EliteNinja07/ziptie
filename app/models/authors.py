from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.database import Base

class Authors(Base):
    __tablename__ = "authors"

    AuthorID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(50), nullable=False)
    BirthDate = Column(Date, nullable=False)
    Country = Column(String(50), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)

    books = relationship("Books", back_populates="authors")
