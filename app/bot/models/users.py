from app.core.models.base import Base
from sqlalchemy import Column, Integer


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
