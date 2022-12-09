import uuid
from sqlalchemy import Column, ForeignKey, BigInteger, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database.connection import Base
from sqlalchemy.orm import relationship

class PostCategory(Base):

    __tablename__ = "post_category"

    _id = Column(BigInteger, primary_key=True, index=True)
    post_guid = Column(UUID(as_uuid=True), ForeignKey("post.guid"))
    post = relationship("Post")
    category_id = Column(Integer, ForeignKey("category._id"))
    category = relationship("Category")
