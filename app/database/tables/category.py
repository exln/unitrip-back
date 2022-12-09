from sqlalchemy import Column, ForeignKey, Integer, String
from app.database.connection import Base

class Category(Base):
    __tablename__ = "category"

    _id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey(_id))
    title = Column(String(75), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)

    meta_title = Column(String(100), nullable=False, server_default="")
    meta_description = Column(String(1000), nullable=False, server_default="")