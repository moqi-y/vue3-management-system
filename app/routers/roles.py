from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_token_header
from app.sql_app.curd.role import *
from app.utils.status_code import *

router = APIRouter()


class Role(BaseModel):
    name: str
    permissions: str
    remark: str


@router.get("/list", tags=["role"], summary="获取角色列表")
async def read_item():
    if get_all_roles():
        return {
            "code": ResponseSuccess.code,
            "msg": ResponseSuccess.message,
            "data": get_all_roles()
        }
    else:
        return {
            "code": ResponseError.code,
            "msg": ResponseError.message
        }


# 新增角色接口
@router.post("/add", tags=["role"], summary="新增角色", dependencies=[Depends(get_token_header)])
async def create_item(role: Role):
    if insert_role(role.name, role.permissions, role.remark):
        return {
            "code": ResponseSuccess.code,
            "msg": ResponseSuccess.message
        }
    else:
        return {
            "code": ResponseError.code,
            "msg": ResponseError.message
        }
