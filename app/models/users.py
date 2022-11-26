from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, Field

from app.models.utilities import optional


class UserBase(BaseModel):
    email: EmailStr = Field(description="Email адрес пользователя")
    firstName: str = Field(description="Имя пользователя", min_length=2)
    lastName: str = Field(description="Фамилия пользователя", min_length=2)

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(description="Пароль пользователя", min_length=8)


class UserGet(UserBase):
    guid: UUID4 = Field(description="Уникальный идентификатор пользователя")
    _id: str = Field(description="ID пользователя")
    password: str = Field(description="Пароль пользователя")
    createdAt: datetime = Field(description="Время создания пользователя")
    updatedAt: datetime = Field(
        description="Время последнего обновления пользователя")

    class Config:
        orm_mode = True


class UserGetByEmail(BaseModel):
    isUser: bool = Field(description="Наличие пользователя в базе")
    email: Optional[EmailStr] = Field(description="Email адрес пользователя")
    firstName: Optional[str] = Field(description="Имя пользователя", min_length=2)

    class Config:
        orm_mode = True

@optional
class UserPatch(UserCreate):
    pass
