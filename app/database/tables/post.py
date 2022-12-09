import uuid 

from sqlalchemy import Column, DateTime, String, Integer, func, Boolean, ForeignKey, Identity, Text
from sqlalchemy.dialects.postgresql import UUID

from app.database.connection import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"

    guid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, unique=True, nullable=False)
    _id = Column(Integer, Identity(start=100000000, cycle=True), nullable=False, unique=True)
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    title = Column(String(75), nullable=False)
    meta_title = Column(String(100), nullable=False)
    summary = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    is_published = Column(Boolean, default=False, nullable=False)
    is_reported = Column(Boolean, default=False, nullable=False)
    is_banned = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()