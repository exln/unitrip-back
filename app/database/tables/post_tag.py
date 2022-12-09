import uuid
from sqlalchemy import Column, BigInteger, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database.connection import Base
from sqlalchemy.orm import relationship

class PostTag(Base):

    __tablename__ = "post_tag"

    _id = Column(BigInteger, primary_key=True, index=True)
    post_guid = Column(UUID(as_uuid=True), ForeignKey("post.guid"))
    post = relationship("Post")    
    tag_guid = Column(Integer, ForeignKey("tag._id"))
    tag = relationship("Tag")
    
    def __repr__(self) -> str:
        return super().__repr__()