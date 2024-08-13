from fastapi import Depends
from sqlmodel import Session, and_, select

from src.database import get_session
from src.debt.models import Debt
from src.user.models import User


async def find_user_debt(
    user: User, service_id: int, session: Session
):
    debt = session.exec(
        select(Debt).where(and_(Debt.user_id == user.id, Debt.service_id == service_id))
    ).one_or_none()
    return debt
