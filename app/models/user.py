from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(45),nullable=False)
    password: Mapped[str] = mapped_column(String(45),nullable=False)
    email: Mapped[str] = mapped_column(String(45),nullable=False)
    address: Mapped[str] = mapped_column(String(45),nullable=False)
