from typing import List, Union

from sqlmodel import Session, col, or_, select

from src.service.models import Service


async def find_service_by_query(
    query: str, session: Session
) -> Union[List[Service], None]:
    service = session.exec(
        select(Service).filter(
            or_(
                col(Service.service_name).contains(query),
                col(Service.service_type).contains(query),
            )
        )
    ).all()
    return service


async def find_service_by_id(id: int, session: Session) -> Union[Service, None]:
    service = session.exec(select(Service).where(Service.id == id)).one_or_none()
    return service
