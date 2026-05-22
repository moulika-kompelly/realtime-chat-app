from fastapi import FastAPI, WebSocket
from app.websockets import websocket_endpoint

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Chat App Running"}

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):

    await websocket_endpoint(websocket)