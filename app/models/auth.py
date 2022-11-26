from pydantic import BaseModel, EmailStr, Field
from typing import Tuple

class UserAuth(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    accessToken: str
    refreshToken: str

class UserInfo(BaseModel):
    _id: str
    email = EmailStr
    firstName = str
    lastName = str


class UserInfoWithTokens(BaseModel):
    user: dict
    accessToken: str
    refreshToken: str


class UserEmail(BaseModel):
    email: EmailStr = Field(description="Email адрес пользователя")