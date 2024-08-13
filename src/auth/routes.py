"""
Authentication Routes
"""

from authx import AuthXDependency
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlmodel import Session

from src.auth import schemas
from src.auth import services as auth_service
from src.auth.dependecies import AUTH
from src.database import get_session
from src.user import services as user_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(
    form: schemas.RegistrationForm, session: Session = Depends(get_session)
):
    return await auth_service.register_user(form=form, session=session)


@router.post("/login")
async def login(
    credentials: HTTPBasicCredentials = Depends(HTTPBasic()),
    session: Session = Depends(get_session),
):

    user = await user_service.find_user(credentials.username, session=session)
    return auth_service.authenticate_user(user, credentials.password)


@router.post("/logout", dependencies=[Depends(AUTH.access_token_required)])
async def logout(
    deps: AuthXDependency = Depends(AUTH.get_dependency),
):

    deps.unset_access_cookies()
    return Response(content="Logout successful", status_code=status.HTTP_200_OK)
