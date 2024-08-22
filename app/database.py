from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

SQLALCHEMY_DB_URL = URL.create(
    drivername="mysql+pymysql",
    username="avnadmin",
    password="AVNS_sCPT6B5CBcW2RX4E7qM",
    port=28889,
    host="mysql-338b5148-anthony-4f9a.g.aivencloud.com",
    database="defaultdb"
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
