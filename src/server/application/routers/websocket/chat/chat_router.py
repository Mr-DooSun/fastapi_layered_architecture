# -*- coding: utf-8 -*-
from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket(path="/chat")
async def chat_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"서버 응답: {data}")
