import uuid
from datetime import datetime, timezone
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel
from uuid_extensions import uuid7


class Service(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid7, default=None, primary_key=True
    )
    name: str = Field(unique=True, index=True)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    payments: List["Payment"] = Relationship(back_populates="service")  # type: ignore
