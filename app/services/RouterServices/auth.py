from __future__ import annotations
import datetime
from datetime import timedelta
import time
from fastapi import Depends, HTTPException, Response, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
import base64
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession


from app.config import config
from app.models import Token, UserAuth, UserCreate, UserGet, UserInfoWithTokens, RefreshToken, UserMetaCreate
from app.repositories import UsersRepository

from ..hash_utils import verify_password, hash_password
from ..oauth2 import AuthJWT, JWTSettings

ACCESS_TOKEN_EXPIRES_IN = config.BACKEND_JWT_ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRES_IN = config.BACKEND_JWT_REFRESH_TOKEN_EXPIRE_MINUTES

bearer_scheme = HTTPBearer()

def verify_token(access_token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    print(access_token)

    jwt.decode(
        access_token.credentials,
        config.BACKEND_JWT_SECRET,
        algorithms=[config.BACKEND_JWT_ALGORITHM],
        options={"verify_aud": False},
    )




class AuthService:
    async def login(self, db: AsyncSession, model: UserAuth, response: Response, Authorize: AuthJWT = Depends()) -> UserInfoWithTokens:
        user = await UsersRepository.get_user_by_email(db=db, email=model.email)
        
        if not user:
            raise HTTPException(401, "Неверный логин или пароль")

        if not verify_password(model.password, user.password):
            raise HTTPException(401, "Неверный логин или пароль")
        user_meta = await UsersRepository.get_user_meta(db=db, user_guid=user.guid)
        access_token = Authorize.create_access_token(subject=str(
            user.guid), fresh=True, expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))
        refresh_token = Authorize.create_refresh_token(subject=str(
            user.guid), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))

        return UserInfoWithTokens(user = {'_id': user_meta.user_id, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}, accessToken=access_token, refreshToken=refresh_token)

    async def register(self, db: AsyncSession, model: UserCreate, response: Response, Authorize: AuthJWT = Depends()) -> UserInfoWithTokens:
        if config.BACKEND_DISABLE_REGISTRATION:
            raise HTTPException(403, "Регистрация отключена")
        user = await UsersRepository.get_user_by_email(db=db, email=model.email)
        if user:
            raise HTTPException(
                409, "Пользователь с таким email уже существует")

        hashed_password = hash_password(model.password)
        model.password = hashed_password
        model.email = EmailStr(model.email.lower())
    
        user = await UsersRepository.create(db, model)
        user_meta = await UsersRepository.create_user_meta(db, guid = user.guid)

        access_token = Authorize.create_access_token(subject=str(
            user.guid), fresh=True, expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))

        refresh_token = Authorize.create_refresh_token(subject=str(
            user.guid), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))

        return UserInfoWithTokens(user = {'_id': user_meta.user_id, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}, accessToken=access_token, refreshToken=refresh_token)

    async def refresh(self, model: str, db: AsyncSession, response: Response, Authorize) -> Token:
        try:
            decoded = jwt.decode(model, base64.b64decode(config.BACKEND_JWT_PUBLIC_KEY).decode('utf-8'), algorithms=['RS256'])
            now = datetime.datetime.now().timestamp()
            if decoded['exp'] < now:
                raise HTTPException(401, detail=' Время действия токена истекло')

            user_guid = decoded['sub']

            if not user_guid:
                raise HTTPException(401, detail='Неверный токен')

            user = await UsersRepository.get(db=db, guid=user_guid)

            if not user:
                raise HTTPException(401, detail='Неверный токен')

            access_token = Authorize.create_access_token(subject=str(
                user.guid), fresh=False, expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))

            refresh_token = Authorize.create_refresh_token(subject=str(
                user.guid), expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN))
            return Token(accessToken=access_token, refreshToken=refresh_token)
        except Exception as e:
            raise HTTPException(401, detail='Неверный токен') from e

    async def logout(self, Authorize: AuthJWT = Depends()) -> Token:
        
        return Token(accessToken='', refreshToken='')
