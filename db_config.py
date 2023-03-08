from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel, Session
from models import *

sqlite_file_name = "notify.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    """Create database."""
    SQLModel.metadata.create_all(engine)

app = FastAPI()

def create_notification(notify_json):
    not_obj = Notification(title=notify_json["title"], description=notify_json["default_message"], category=notify_json["identifier"])

    with Session(engine) as session:
        session.add(not_obj)
        session.commit()

@app.on_event("startup")
def on_startup():
    """Startup."""
    create_db_and_tables()
