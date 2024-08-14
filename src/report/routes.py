from datetime import date, datetime

from authx import TokenPayload
from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.auth.dependecies import AUTH
from src.database import get_session
from src.report import services as report_service

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/", dependencies=[Depends(AUTH.access_token_required)])
async def find_all(
    from_date: date,
    to_date: date = datetime.today(),
    payload: TokenPayload = Depends(AUTH.access_token_required),
    session: Session = Depends(get_session),
):
    user_id = int(payload.sub)
    return await report_service.make_report(
        user_id=user_id, from_date=from_date, to_date=to_date, session=session
    )
