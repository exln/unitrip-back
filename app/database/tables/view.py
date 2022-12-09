from sqlalchemy import Column, ForeignKey, BigInteger, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from app.database.connection import Base
from sqlalchemy.orm import relationship

class View(Base):
    __tablename__ = "view"
    _id = Column(BigInteger, primary_key=True, index=True)
    post_guid = Column(UUID(as_uuid=True), ForeignKey("post.guid"))
    post = relationship("Post")
    session_guid = Column(UUID(as_uuid=True), ForeignKey("session.guid"))
    session = relationship("Session")
    viewed_at = Column(DateTime, server_default=func.now())
    reviewed_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
