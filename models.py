"""Model class."""
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, select

class Notification(SQLModel, table=True):
    """Send Notification Transactions."""
    id: Optional[int] = Field(primary_key=True)

    title: str
    description: str
    category: str
    is_read: bool = Field(default=False)
