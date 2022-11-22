from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, Field

from app.models.utilities import optional


class UserBase(BaseModel):
    email: EmailStr = Field(description="Email адрес пользователя")
    first_name: str = Field(description="Имя пользователя", min_items=2)
    last_name: str = Field(description="Фамилия пользователя", min_length=2)

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(description="Пароль пользователя", min_length=8)
    role: str = Field(description="Роль пользователя", min_length=8)


class UserGet(UserBase):
    guid: UUID4 = Field(description="Уникальный идентификатор пользователя")
    password: str = Field(description="Пароль пользователя")
    created_at: datetime = Field(description="Время создания пользователя")
    updated_at: datetime = Field(description="Время последнего обновления пользователя")

    class Config:
        orm_mode = True


@optional
class UserPatch(UserCreate):
    pass
