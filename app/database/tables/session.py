import uuid
from sqlalchemy import Column, ForeignKey, BigInteger, DateTime, func, String
from sqlalchemy.dialects.postgresql import UUID
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Session(Base):
    __tablename__ = "session"
    _id = Column(BigInteger, primary_key=True, index=True)
    guid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    user_ip = Column(String(32), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())