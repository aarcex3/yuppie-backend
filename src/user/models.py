import uuid
from datetime import datetime, timezone
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel
from uuid_extensions import uuid7


class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid7, default=None, primary_key=True
    )
    fname: str
    lname: str
    full_name: str = Field(index=True)
    password: str
    email: str
    doc_number: str = Field(unique=True)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    payments: List["Payment"] = Relationship(back_populates="user")  # type: ignore
    reports: List["Report"] = Relationship(back_populates="user")  # type: ignore
