"""main page."""
from typing import Optional, List

from fastapi.exceptions import HTTPException
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from sqlmodel import Session

from models import *
from db_config import create_notification, app, engine
from constants import NOTIFICATION_FORMAT
from html_content import *
from notifier import *

@app.get("/")
async def get():
    return HTMLResponse(notification_display_html)

@app.get("/send/")
async def get():
    return HTMLResponse(notification_send_html)





notifier = Notifier()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await notifier.connect(websocket)
    try:
        while True:
            notify_for = await websocket.receive_text()
            notify_json = NOTIFICATION_FORMAT[notify_for]
            create_notification(notify_json=notify_json)
            await notifier.push(f'Identifier: {notify_json["identifier"]}, Title: {notify_json["title"]}, Message: {notify_json["default_message"]}')
    except WebSocketDisconnect:
        notifier.remove(websocket)


@app.get("/notification/")
def read_notifications():
    """Get notifications."""
    with Session(engine) as session:
        notifications = session.exec(select(Notification)).all()
        return notifications


@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await notifier.generator.asend(None)
