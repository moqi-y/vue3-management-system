from app.dependencies import get_query_token, get_token_header
from app.routers import users, roles
from fastapi import Depends


def router_config(app):
    app.include_router(
        users.router,
        prefix="/users",  # 路径名
        tags=["users"],  # 文档标签名
        dependencies=[Depends(get_token_header)],  # 依赖项
        responses={418: {"msg": "未知错误"}},
    )

    app.include_router(
        roles.router,
        prefix="/role",  # 路径名
        tags=["role"],  # 文档标签名
        responses={418: {"msg": "未知错误"}},
    )
