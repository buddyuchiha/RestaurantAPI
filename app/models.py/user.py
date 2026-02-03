from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base


class User(Base):
    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=True)
    real_name: Mapped[str] = mapped_column(nullable=False)
    default_email: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=True)