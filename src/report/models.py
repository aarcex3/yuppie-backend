import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import JSON, Field, Relationship, SQLModel
from uuid_extensions import uuid7

from src.user.models import User


class Report(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid7, default=None, primary_key=True
    )
    user_id: uuid.UUID = Field(foreign_key="user.id")
    data: JSON
    report_date: datetime = Field(default_factory=datetime.now(timezone.utc))
    start_date: datetime
    end_date: datetime
    user: User = Relationship(back_populates="reports")
