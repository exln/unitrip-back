from sqlalchemy import Column, ForeignKey, BigInteger, String
from app.database.connection import Base

class S3(Base):
    __tablename__ = "s3"
    _id = Column(BigInteger, primary_key=True, index=True, nullable=False, unique=True)
    url = Column(String(255), nullable=False, unique=True)