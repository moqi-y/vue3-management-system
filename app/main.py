from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from app.utils.status_code import *
import config
from app.middleware import cors
from app.routers import router_config

app = FastAPI(
    title="FastAPI-Vue3",
    description="vue3-management-system接口文档",
    version="1.0.0",
    # dependencies=[Depends(get_query_token)]  # 全部接口的依赖项
)

#  跨域设置
cors.cors_config(app)

# 路由配置
router_config(app)


# 连通测试
@app.get("/ping", summary="连通测试", description="测试连通性", tags=["测试"])
async def root():
    # 读取.env中的配置
    print(config.APP_NAME)
    return {
        "code": ResponseSuccess.code,
        "message": ResponseSuccess.message,
        "data": {
            "appName": config.APP_NAME,
            "appVersion": config.APP_VERSION
        }
    }


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
