from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Tag(Base):
    __tablename__ = "tag"

    _id = Column(Integer, primary_key=True, index=True)
    title = Column(String(75), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)

    meta_title = Column(String(100), nullable=False, server_default="")
    meta_description = Column(String(1000), nullable=False, server_default="")