# To run application normally
uvicorn main:app --reload

Visit
  http://localhost:8000 Home page for list of receiving notifications
  http://localhost:8000/send/ To send notifications and receive it on home page.
  http://localhost:8000/notifications All notifications stored in database
