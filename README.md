# To run application normally
cd websocket_notification_fastapi
uvicorn main:app --reload

Visit Home page for list of receiving notifications.
http://localhost:8000

To send notifications and receive it on home page.
http://localhost:8000/send/

All notifications stored in database.
http://localhost:8000/notifications
