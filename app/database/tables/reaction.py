from sqlalchemy import Column, SmallInteger, String
from app.database.connection import Base

class Reaction(Base):
    __tablename__ = "reaction"

    _id = Column(SmallInteger, primary_key=True, index=True)
    title = Column(String(20), nullable=False)