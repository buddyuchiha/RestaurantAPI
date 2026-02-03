from sqlalchemy.orm import mapped_column, Mapped 
from sqlalchemy import Enum

from app.core import TableStatus
from app.database import Base 


class TableORM(Base):
    __tablename__ = "tables"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(
        Enum(TableStatus), 
        default=TableStatus.FREE
    )