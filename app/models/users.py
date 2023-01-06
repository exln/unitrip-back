from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, Field

from app.models.utilities import optional

print("users.py loaded")

class UserBase(BaseModel):
    email: EmailStr = Field(description="Email адрес пользователя")
    first_name: str = Field(description="Имя пользователя", min_length=2)
    last_name: str = Field(description="Фамилия пользователя", min_length=2)

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(description="Пароль пользователя", min_length=8)

class UserMetaCreate(BaseModel):
    # userGuid: UUID4 = Field(description="Уникальный идентификатор пользователя")
    # isEmailConfirmed: bool = Field(description="Подтвержден ли email пользователя")
    # isPhoneConfirmed: bool = Field(description="Подтвержден ли телефон пользователя")
    # isTwoFactorEnabled: bool = Field(description="Включен ли двухфакторный вход пользователя")
    # isUserBlocked: bool = Field(description="Заблокирован ли пользователь")
    # isUserDeleted: bool = Field(description="Удален ли пользователь")
    # isUserEmailSubscribed: bool = Field(description="Подписан ли пользователь на рассылку")
    # isUserPhoneSubscribed: bool = Field(description="Подписан ли пользователь на рассылку по телефону")
    user_guid: UUID4 = Field(description="Уникальный идентификатор пользователя")
    nickname: str = Field(description="Никнейм пользователя", min_length=5, max_length=20, default=None)
    pfp_full_url: str = Field(description="Полный URL аватарки пользователя")
    pfp_thumb_url: str = Field(description="Полный URL миниатюры аватарки пользователя")
    
    
    class Config:
        orm_mode = True


class UserGet(UserBase):
    guid: UUID4 = Field(description="Уникальный идентификатор пользователя")
    _id: str = Field(description="ID пользователя")
    password: str = Field(description="Пароль пользователя")
    createdAt: datetime = Field(description="Время создания пользователя")
    updatedAt: datetime = Field(description="Время последнего обновления пользователя")

    class Config:
        orm_mode = True


class UserGetByEmail(BaseModel):
    isUser: bool = Field(description="Наличие пользователя в базе")
    email: Optional[EmailStr] = Field(description="Email адрес пользователя")
    first_name: Optional[str] = Field(description="Имя пользователя", min_length=2)

    class Config:
        orm_mode = True

@optional
class UserPatch(UserCreate):
    pass
