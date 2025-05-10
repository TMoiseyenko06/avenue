from database import db,Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String

class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255))
    description: Mapped[str] = mapped_column(db.String(255))
    color: Mapped[int] = mapped_column(db.Integer)