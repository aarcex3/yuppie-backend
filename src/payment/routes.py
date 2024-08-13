from authx import TokenPayload
from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.auth.dependecies import AUTH
from src.database import get_session
from src.payment import services as payment_service
from src.payment.schemas import PaymentRequest

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", dependencies=[Depends(AUTH.access_token_required)])
async def pay_service(
    payment_data: PaymentRequest,
    payload: TokenPayload = Depends(AUTH.access_token_required),
    session: Session = Depends(get_session),
):
    return await payment_service.make_payment(
        payment_data=payment_data, payload=payload, session=session
    )
