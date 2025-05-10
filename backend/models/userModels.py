from database import db,Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Integer

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(db.String(255))
    email: Mapped[str] = mapped_column(db.String(255))
    phone: Mapped[int] = mapped_column(db.Integer)
