from sqlalchemy import Column, ForeignKey, Integer, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.connection import Base

class CommentMeta(Base):
    __tablename__ = "comment_meta"
    _id = Column(BigInteger, primary_key=True, index=True, unique=True, nullable=False) 
    comment_guid = Column(UUID(as_uuid=True), ForeignKey("comment.guid"))
    comment = relationship("Comment")
    attachment_full_url = Column(BigInteger, default = 0, nullable=False)
    attachment_thumb_url = Column(BigInteger, default = 0, nullable=False)