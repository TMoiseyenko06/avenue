from database import db,Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer,Column, ForeignKey, Table, List

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(db.String(255))
    email: Mapped[str] = mapped_column(db.String(255))
    phone: Mapped[int] = mapped_column(db.Integer)

user_tags = Table(
    'user_tags',
    Base.metadata,
    Column('user_id',Integer, ForeignKey('users.id'),primary_key=True),
    Column('tag_id',Integer, ForeignKey('tags.id'),primary_key=True)
)