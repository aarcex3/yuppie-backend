from datetime import datetime, timezone
from typing import Dict, Optional

from sqlmodel import JSON, Column, Field, Relationship, SQLModel

from src.service.models import Service
from src.user.models import User


class Payment(SQLModel, table=True):
    __tablename__: str = "payments"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    service_id: int = Field(foreign_key="services.id")
    reference: str
    total_debt: float
    amount_paid: float
    proof: str
    date: datetime = datetime.now(timezone.utc)
    additional_info: Dict = Field(default_factory=dict, sa_column=Column(JSON))
    user: User = Relationship(back_populates="payments")
    service: Service = Relationship(back_populates="payments")

    class Config:
        arbitrary_types_allowed = True
