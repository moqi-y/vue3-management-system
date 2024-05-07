# 定义数据表模型
from sqlalchemy import *

from app.sql_app.database import Base


# 定义user表模型
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(255))
    email = Column(String(100))
    mobile = Column(String(11))


# 定义role表模型
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # 角色权限
    permissions = Column(String(255))
    remark = Column(String(255))
