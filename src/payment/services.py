from datetime import datetime, timezone

from authx import TokenPayload
from fastapi import HTTPException, status
from sqlmodel import Session

from src.debt import services as debt_service
from src.payment.schemas import PaymentRequest
from src.payment.utils import (
    create_payment,
    make_payment_proof,
    process_debt_and_user_cash,
)
from src.user import services as user_service


async def make_payment(
    payment_data: PaymentRequest, payload: TokenPayload, session: Session
):
    doc_number = getattr(payload, "doc_number")
    user = await user_service.find_user(doc_number, session)
    debt = await debt_service.find_user_debt(user, payment_data.service_id, session)
    if not debt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No debts for this service"
        )
    if not user_service.check_user_cash(payment_data.amount, user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds"
        )

    proof = make_payment_proof(
        payment_date=datetime.now(timezone.utc),
        user=user,
        service_id=payment_data.service_id,
        reference=payment_data.reference,
    )

    payment = create_payment(payment_data, user, debt, proof)
    session.add(payment)

    try:
        await process_debt_and_user_cash(debt, payment_data.amount, user, session)
        session.commit()
        session.refresh(payment)
        return {"message": "Payment successful", "payment_proof": payment.proof}

    except Exception as ex:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Payment processing failed",
        ) from ex
