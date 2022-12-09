from sqlalchemy import Column, ForeignKey, BigInteger, String, Integer, SmallInteger, DateTime, func
from app.database.connection import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class PostReaction(Base):
    __tablename__ = "post_reaction"
    _id = Column(BigInteger, primary_key=True, index=True)
    post_guid = Column(UUID(as_uuid=True), ForeignKey("post.guid"))
    post = relationship("Post")
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    type = Column(SmallInteger, ForeignKey("reaction._id"),nullable=False)
    reaction = relationship("Reaction")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    