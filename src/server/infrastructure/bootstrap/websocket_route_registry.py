# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.server.application.routers.websocket.chat import chat_router


def register_websocket_routes(app: FastAPI):
    app.include_router(router=chat_router.router, prefix="/v1/ws")
