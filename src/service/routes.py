from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.database import get_session
from src.service import services as services_service

router = APIRouter(prefix="/services", tags=["Services"])


@router.get("/search")
async def find_one_by_query(service_name: str, session: Session = Depends(get_session)):
    return await services_service.find_service_by_query(
        query=service_name.upper(), session=session
    )


@router.get("/{service_id}")
async def find_one_by_id(service_id: int, session: Session = Depends(get_session)):
    return await services_service.find_service_by_id(id=service_id, session=session)
