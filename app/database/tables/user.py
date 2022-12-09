import uuid

from sqlalchemy import Column, DateTime, String, func, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.database.connection import Base

class User(Base):
    __tablename__ = "user"

    guid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)

    is_active = Column(Boolean, default=False, nullable=False)
    is_reported = Column(Boolean, default=False, nullable=False)
    is_banned = Column(Boolean, default=False, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    


