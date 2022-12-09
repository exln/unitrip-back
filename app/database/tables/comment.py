import uuid
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, Boolean, DateTime, Identity, func
from sqlalchemy.dialects.postgresql import UUID
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comment"

    _id = Column(BigInteger, primary_key=True, index=True)
    guid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    comment_id = Column(Integer, Identity(start=100000000, cycle=True), nullable=False, unique=True)
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    post_guid = Column(UUID(as_uuid=True), ForeignKey("post.guid"))
    post = relationship("Post")
    parent_guid = Column(UUID(as_uuid=True), ForeignKey(guid))
    content = Column(String(1000), nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    published_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    

    def __repr__(self) -> str:
        return super().__repr__()