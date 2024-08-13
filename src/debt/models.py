import enum
from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Status(enum.Enum):
    PAID = "PAID"
    IN_PROGRESS = "IN_PROGRESS"


class Debt(SQLModel, table=True):
    __tablename__: str = "debts"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    service_id: int = Field(foreign_key="services.id")
    total_debt: float
    remaining_debt: float
    due_date: datetime
    status: Status
    user: Optional["User"] = Relationship(back_populates="debts")
    service: Optional["Service"] = Relationship(back_populates="debts")
