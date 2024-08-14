from typing import Union

from sqlmodel import Session, select

from src.user.models import User


async def find_user(doc_number: int, session: Session) -> Union[User, None]:
    user = session.exec(select(User).where(User.doc_number == doc_number)).one_or_none()
    return user


def create_user(
    fname: str, lname: str, password: str, email: str, doc_number: int
) -> User:
    return User(
        fname=fname,
        lname=lname,
        full_name=f"{lname}, {fname}",
        password=password,
        email=email,
        doc_number=doc_number,
    )


def check_user_cash(total_to_pay: int, user: User) -> bool:
    return user.cash >= total_to_pay


async def deduct_user_cash(user: User, amount: int, session: Session) -> None:
    user.cash -= amount
    session.add(user)
    session.commit()
