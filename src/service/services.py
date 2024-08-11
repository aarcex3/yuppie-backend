from typing import Union

from fastapi import Depends
from sqlmodel import Session, select

from src.database import get_session
from src.service.models import Service


async def find_service(
    name: str, session: Session = Depends(get_session)
) -> Union[Service, None]:
    service = session.exec(select(Service).where(Service.name == name)).one()
    return service
