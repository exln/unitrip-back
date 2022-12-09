from pydantic import BaseModel, EmailStr, Field
from typing import Tuple

class UserAuth(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    accessToken: str
    refreshToken: str

class RefreshToken(BaseModel):
    refreshToken: str

class UserInfo(BaseModel):
    _id: str
    email = EmailStr
    first_name = str
    last_name = str


class UserInfoWithTokens(BaseModel):
    user: dict = {
        '_id': int,
        'email': EmailStr,
        'first_name': str,
        'last_name': str
    }
    accessToken: str
    refreshToken: str


class UserEmail(BaseModel):
    email: EmailStr = Field(description="Email адрес пользователя")