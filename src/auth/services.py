from fastapi import Depends, HTTPException, Response, status
from sqlmodel import Session

from src.auth.dependecies import AUTH
from src.auth.schemas import RegistrationForm
from src.auth.utils import check_password, hash_password
from src.database import get_session
from src.user import services as user_service
from src.user.models import User


async def register_user(
    form: RegistrationForm, session: Session = Depends(get_session)
):
    """
    Register a new user
    """
    user_password = hash_password(form.password.get_secret_value())
    new_user = user_service.create_user(
        fname=form.fname,
        lname=form.lname,
        password=user_password,
        email=form.email,
        doc_number=form.doc_number,
    )
    session.add(new_user)
    try:
        session.commit()
        return Response(status_code=status.HTTP_201_CREATED, content="User created")
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
        ) from ex


def authenticate_user(user: User, password: str):
    """
    Authenticate user and generate access token
    """
    if user and check_password(password, user.password):
        token = AUTH.create_access_token(uid=str(user.email))
        headers = {"Authorization": f"Bearer {token}"}
        return Response(
            status_code=status.HTTP_200_OK,
            headers=headers,
            content="Succesfully logged in",
        )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad credentials"
    )
