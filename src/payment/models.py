import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import JSON, Field, Relationship, SQLModel
from uuid_extensions import uuid7

from src.service.models import Service
from src.user.models import User


class Payment(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid7, default=None, primary_key=True
    )
    user_id: uuid.UUID = Field(foreign_key="user.id")
    entity_id: uuid.UUID = Field(foreign_key="entity.id")
    reference_number: str
    total_debt: int
    amount_paid: int
    date: datetime = Field(default_factory=datetime.now(timezone.utc))
    additional_info: JSON = Field(default="{}")
    user: User = Relationship(back_populates="payments")
    service: Service = Relationship(back_populates="payments")
