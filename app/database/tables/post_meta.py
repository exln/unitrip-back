import uuid
from sqlalchemy import Column, DateTime, String, func, Boolean, BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database.connection import Base
from sqlalchemy.orm import relationship

class PostMeta(Base):

    __tablename__ = "post_meta"

    _id = Column(BigInteger, primary_key=True, index=True)
    post_guid = Column(UUID(as_uuid=True), ForeignKey("post.guid"))
    post = relationship("Post")    
    attachment_full_url = Column(BigInteger, default = 0, nullable=False)
    attachment_thumb_url = Column(BigInteger, default = 0, nullable=False)

    
    def __repr__(self) -> str:
        return super().__repr__()