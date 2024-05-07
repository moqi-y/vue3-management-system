from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    if x_token != "token":
        raise HTTPException(status_code=400, detail="X-Token 无效")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="没有提供Token")