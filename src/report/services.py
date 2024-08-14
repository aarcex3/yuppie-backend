from datetime import date
from typing import List

from sqlmodel import Session, select

from src.payment.models import Payment
from src.user.models import User


async def make_report(
    user_id: int, from_date: date, to_date: date, session: Session
) -> List[Payment]:
    payments = session.exec(
        select(Payment)
        .where(Payment.date >= from_date, Payment.date <= to_date)
        .where(Payment.user_id == user_id)
    ).all()
    return payments
