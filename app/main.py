# -*- coding: UTF-8 -*-
from typing import Union
from fastapi import FastAPI
# 从 routers 目录中导入你的路由
from app.routers import items

app = FastAPI()

# 包含并注册你的路由器
app.include_router(items.router)

# 你可以继续在这里定义顶层路由


@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application"}
