from fastapi import APIRouter
from pydantic import BaseModel

from app.sql_app.curd.user import *
from app.utils.status_code import *

router = APIRouter()


class User(BaseModel):
    name: str
    password: str
    email: str
    mobile: str


#  获取用户列表
@router.get("/list", tags=["users"], summary="获取用户列表")
async def read_users():
    return {
        "code": ResponseSuccess.code,
        "msg": ResponseSuccess.message,
        "data": get_all_users()
    }


# 条件查找用户
@router.get("/search", tags=["users"], summary="条件查找用户")
async def search_user(uid: int):
    if not get_user(uid):
        return {"code": ResponseUserNotExist.code, "msg": ResponseUserNotExist.message}
    return {
        "code": ResponseSuccess.code,
        "msg": ResponseSuccess.message,
        "data": get_user(uid)
    }


# 新增用户
@router.post("/add", tags=["users"], summary="新增用户")
async def add_user(user: User):
    if insert_user(user.name, user.password, user.email, user.mobile):
        return {"code": ResponseSuccess.code, "msg": ResponseSuccess.message}
    else:
        return {"code": ResponseError.code, "msg": ResponseError.message}
