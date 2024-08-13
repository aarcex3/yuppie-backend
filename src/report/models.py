# from datetime import datetime
# from typing import Dict, Optional

# from sqlmodel import JSON, Column, Field, Relationship, SQLModel


# class Report(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="user.id")
#     data: Dict = Field(default_factory=dict, sa_column=Column(JSON))
#     report_date: datetime
#     start_date: datetime
#     end_date: datetime
#     user: "User" = Relationship(back_populates="reports")
