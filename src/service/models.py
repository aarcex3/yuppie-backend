from datetime import datetime, timezone
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Service(SQLModel, table=True):
    __tablename__: str = "services"
    id: Optional[int] = Field(default=None, primary_key=True)
    service_name: str = Field(unique=True, index=True)
    service_type: str = Field(index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payments: List["Payment"] = Relationship(back_populates="service")
    debts: List["Debt"] = Relationship(back_populates="service")
