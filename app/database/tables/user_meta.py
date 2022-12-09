import uuid

from sqlalchemy import Column, String, func, Boolean, Identity, Integer, Text, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID

from app.database.connection import Base
from sqlalchemy.orm import relationship

class UserMeta(Base):
    __tablename__ = "user_meta"

    _id = Column(Integer, primary_key=True, index=True)
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    user_id = Column(Integer, Identity(start=100000000, cycle=True), nullable=False, unique=True)
    nickname = Column(String(20), nullable=True)

    pfp_full_url = Column(BigInteger, default=0, nullable=True)
    pfp_thumb_url = Column(BigInteger, default=0, nullable=True)
    
    bio = Column(Text, server_default='Пользователь ещё не написал о себе.', nullable=False)
    last_seen = Column(String, server_default='Никогда', nullable=False)
    location = Column(String, server_default='Неуказано', nullable=False)
    website = Column(String, server_default='Неуказано', nullable=False)
    birthday = Column(String, server_default='Неуказано', nullable=False)
