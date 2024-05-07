import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# 连接数据库
# engine = create_engine("mysql+pymysql://root:123456@localhost:3306/fastapi_web_temp", echo=False)
# sqlite
engine = create_engine("sqlite:////./sql_app.db", echo=False)
Base = sqlalchemy.orm.declarative_base()
