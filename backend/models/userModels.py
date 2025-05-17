from database import db,Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer,Column, ForeignKey, Table
from .tagModels import Tag
from typing import List

user_tags = Table(
    'user_tags',
    Base.metadata,
    Column('user_id',Integer, ForeignKey('users.id'),primary_key=True),
    Column('tag_id',Integer, ForeignKey('tags.id'),primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(db.String(255))
    firstName: Mapped[str] = mapped_column(db.String(255),nullable=True)
    lastName: Mapped[str] = mapped_column(db.String(255),nullable=True)
    email: Mapped[str] = mapped_column(db.String(255),nullable=True)
    phone: Mapped[int] = mapped_column(db.Integer,nullable=True)
    tags: Mapped[List[Tag]] = relationship(Tag,secondary=user_tags)

