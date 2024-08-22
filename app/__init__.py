from fastapi import FastAPI

from app import models, schemas
from app.database import Base, engine
from app.routers import authors, books

Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(authors.router)
app.include_router(books.router)
