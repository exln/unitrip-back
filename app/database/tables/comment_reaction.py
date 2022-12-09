from sqlalchemy import Column, ForeignKey, BigInteger, String, Integer, SmallInteger, DateTime, func
from app.database.connection import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class CommentReaction(Base):
    __tablename__ = "comment_reaction"
    _id = Column(BigInteger, primary_key=True, index=True, nullable=False, unique=True)
    comment_guid = Column(UUID(as_uuid=True), ForeignKey("comment.guid"))
    comment = relationship("Comment")
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    type = Column(SmallInteger, ForeignKey("reaction._id"),nullable=False)
    reaction = relationship("Reaction")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())