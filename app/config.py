import os

class Config:
    DRIVERNAME="mysql+pymysql"
    USERNAME=os.environ["USERNAME"]
    PASSWORD=os.environ["PASSWORD"]
    PORT=28889
    HOST=os.environ["HOST"]
    DATABASE=os.environ["DATABASE"]