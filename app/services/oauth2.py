import base64
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import config

from app.database.tables import user as userModel


class JWTSettings(BaseModel):
    authjwt_algorithm: str = config.BACKEND_JWT_ALGORITHM
    authjwt_decode_algorithms: List[str] = [config.BACKEND_JWT_ALGORITHM]
    authjwt_token_location: set = {'cookies', 'headers'}
    authjwt_access_cookie_key: str = 'accessToken'
    authjwt_refresh_cookie_key: str = 'refreshToken'
    # authjwt_cookie_csrf_protect: bool = False
    authjwt_public_key: str = base64.b64decode(
        config.BACKEND_JWT_PUBLIC_KEY).decode('utf-8')
    authjwt_private_key: str = base64.b64decode(
        config.BACKEND_JWT_PRIVATE_KEY).decode('utf-8')


@AuthJWT.load_config
def get_config():
    return JWTSettings()


class UserNotFound(Exception):
    pass


def require_user(db: AsyncSession, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        user_guid = Authorize.get_jwt_subject()
        user = db.query(userModel).filter(userModel.guid == user_guid).first()

        if not user:
            raise UserNotFound("Пользователь не найден")

    except Exception as e:
        error = e.__class__.__name__
        print(error)
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Вход не выполнен")
        if error == 'UserNotFound':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не найден")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный токен авторизации")
    return user_guid
