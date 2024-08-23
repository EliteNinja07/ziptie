from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from config import Config

SQLALCHEMY_DB_URL = URL.create(
    drivername=Config.DRIVERNAME,
    username=Config.USERNAME,
    password=Config.PASSWORD,
    port=Config.PORT,
    host=Config.HOST,
    database=Config.DATABASE
)

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
