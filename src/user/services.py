from typing import Union

from fastapi import Depends
from sqlmodel import Session, select

from src.database import get_session
from src.user.models import User


async def find_user(
    email: str, session: Session = Depends(get_session)
) -> Union[User, None]:
    """
    Find the user for the given username
    """
    user = session.exec(select(User).where(User.email == email)).one()
    return user


def create_user(fname: str, lname: str, password: str, email: str, doc_number: str):
    return User(
        fname=fname,
        lname=lname,
        password=password,
        email=email,
        doc_number=doc_number,
    )
