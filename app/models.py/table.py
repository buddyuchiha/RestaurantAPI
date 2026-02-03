from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base 


class Table(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(nullable=False)
    