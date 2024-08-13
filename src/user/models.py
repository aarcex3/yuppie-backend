from datetime import datetime, timezone
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__: str = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    fname: str = Field(index=True)
    lname: str = Field(index=True)
    full_name: str = Field(index=True)
    password: str
    email: str
    doc_number: int = Field(unique=True, index=True)
    cash: float = Field(default=0.0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payments: List["Payment"] = Relationship(back_populates="user")
    debts: List["Debt"] = Relationship(back_populates="user")
