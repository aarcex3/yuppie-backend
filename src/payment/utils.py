import hashlib
from datetime import datetime

from fastapi import HTTPException, status
from sqlmodel import Session

from src.debt.models import Debt, Status
from src.payment.models import Payment
from src.payment.schemas import PaymentRequest
from src.user import services as user_service
from src.user.models import User


def make_payment_proof(
    payment_date: datetime, user: User, service_id: int, reference: str
):
    text: bytes = (
        f"{payment_date.isoformat()}_{user.id}_{user.doc_number}_{service_id}_{reference}".encode(
            "utf-8"
        )
    )
    return hashlib.sha256(text).hexdigest().upper()


def verify_proof(
    payment_date: datetime, user: User, service_id: int, reference: str, proof: str
) -> bool:
    return (
        make_payment_proof(
            payment_date=payment_date,
            user=user,
            service_id=service_id,
            reference=reference,
        )
        == proof
    )


def create_payment(
    payment_data: PaymentRequest, user: User, debt: Debt, proof: str
) -> Payment:
    return Payment(
        user_id=user.id,
        service_id=payment_data.service_id,
        reference=payment_data.reference,
        amount_paid=payment_data.amount,
        total_debt=debt.total_debt,
        proof=proof,
    )


async def process_debt_and_user_cash(
    debt: Debt, amount_paid: float, user: User, session: Session
):
    debt.remaining_debt -= amount_paid

    if debt.remaining_debt < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Overpayment is not allowed",
        )

    debt.status = Status.PAID if debt.remaining_debt == 0 else Status.IN_PROGRESS
    session.add(debt)

    await user_service.deduct_user_cash(user=user, amount=amount_paid, session=session)
