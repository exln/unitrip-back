from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.config import config
from app.models import UserCreate, UserAuth, Token, UserInfoWithTokens, RefreshToken
from app.database import get_session
from app.services.RouterServices import AuthService
from app.services.oauth2 import AuthJWT


router = APIRouter(prefix=config.BACKEND_PREFIX)

ACCESS_TOKEN_EXPIRES_IN = config.BACKEND_JWT_ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRES_IN = config.BACKEND_JWT_REFRESH_TOKEN_EXPIRE_MINUTES


@router.post(
    "/register",
    response_model=UserInfoWithTokens,
    response_description="Успешный возврат токена авторизации",
    status_code=status.HTTP_200_OK,
    description="Зарегистирироваться в сервисе и получить токен",
    summary="Регистрация в сервисе",
    # responses={},
)
async def register(model: UserCreate, response: Response, db: AsyncSession = Depends(get_session), auth_service: AuthService = Depends(), Authorize: AuthJWT = Depends()):
    return await auth_service.register(db=db, model=model,Authorize=Authorize, response=response)


@router.post(
    "/login",
    response_model=UserInfoWithTokens,
    response_description="Успешный возврат токена авторизации",
    status_code=status.HTTP_200_OK,
    description="Войти в сервис и получить токен",
    summary="Вход в сервис",
    # responses={},
)
async def login(model: UserAuth, response: Response, db: AsyncSession = Depends(get_session), auth_service: AuthService = Depends(), Authorize: AuthJWT = Depends()):
    return await auth_service.login(db=db, model=model, Authorize=Authorize, response=response)


@router.post(
    "/refresh",
    response_model=Token,
    response_description="Успешный возврат нового токена авторизации",
    status_code=status.HTTP_200_OK,
    description="Получить новый токен",
    summary="Обновления токена доступа",
    # responses={},
)
async def refresh(model: RefreshToken, response: Response, db: AsyncSession = Depends(get_session), auth_service: AuthService = Depends(), Authorize: AuthJWT = Depends()):
    return await auth_service.refresh(model=model.refreshToken, db=db, response=response, Authorize=Authorize)
    

@router.get(
    "/logout",
    response_model=Token,
    response_description="Успешный выход из учётной записи",
    status_code=status.HTTP_200_OK,
    description="Выход из учётной записи и сброс токена доступа",
    summary="Выход",
    # responses={},
)
async def logout(auth_service: AuthService = Depends()):
    return await auth_service.logout()

