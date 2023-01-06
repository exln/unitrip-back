from dataclasses import dataclass
from pydantic import BaseModel, EmailStr, Field
from typing import Tuple, Dict, Union


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

class UserModel(BaseModel):
    _id: int = Field(description="Идентификатор пользователя")
    email: EmailStr = Field(description="Email адрес пользователя")
    first_name: str = Field(description="Имя пользователя")
    last_name: str = Field(description="Фамилия пользователя")

class UserInfoWithTokens(BaseModel):
    user: UserModel = Field(description="Информация о пользователе")
    accessToken: str = Field(description="JWT access-токен")
    refreshToken: str = Field(description="JWT refresh-токен")


class UserEmail(BaseModel):
    email: EmailStr = Field(description="Email адрес пользователя")
