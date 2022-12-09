from sqlalchemy import Column, ForeignKey, Integer, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.connection import Base

class UserTag(Base):
    __tablename__ = "user_tag"
    _id = Column(BigInteger, primary_key=True, index=True)
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    tag_guid = Column(Integer, ForeignKey("tag._id"))
    tag = relationship("Tag")