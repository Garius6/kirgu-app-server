from sqlalchemy import Column, Integer, String, Enum

from .database import Base
from .schemas import Status


class Task(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    responsible = Column(String, index=True)
    status = Column(Enum(Status))
