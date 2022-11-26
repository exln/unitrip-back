import uuid

from sqlalchemy import Column, DateTime, String, func, Integer
from sqlalchemy.dialects.postgresql import UUID

from app.database.connection import Base
from app.services import generate_random_string

class User(Base):
    __tablename__ = "users"

    guid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True, unique=True)
    _id = Column(Integer, default=generate_random_string(7), unique=True)
    nickname = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

