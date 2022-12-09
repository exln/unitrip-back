from sqlalchemy import Column, ForeignKey, BigInteger, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.connection import Base

class UserCategory(Base):
    __tablename__ = "user_category"

    _id = Column(BigInteger, primary_key=True, index=True)
    user_guid = Column(UUID(as_uuid=True), ForeignKey("user.guid"))
    user = relationship("User")
    category_guid = Column(Integer, ForeignKey("category._id"))
    category = relationship("Category")
