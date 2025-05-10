from database import db,Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer,Column, ForeignKey, Table

class Event(Base):
    __tablename__ = 'events'
    id: Mapped[int] = mapped_column(primary_key=True)
