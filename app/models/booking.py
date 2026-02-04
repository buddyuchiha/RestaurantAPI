from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, DateTime, Enum


from app.core import BookingStatus
from app.database import Base


class BookingORM(Base):
    __tablename__ = "bookings"
    
    id: Mapped[int] = mapped_column(
        primary_key=True, 
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    table_id: Mapped[int] = mapped_column(
        ForeignKey("tables.id"), 
        nullable=False
    )
    datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        nullable=False
        )
    status: Mapped[str] = mapped_column(
        Enum(BookingStatus), 
        default=BookingStatus.ACTIVE
    )  