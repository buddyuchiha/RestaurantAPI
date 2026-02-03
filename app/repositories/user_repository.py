from sqlalchemy.orm import Session
from sqlalchemy import select


from app.models import TableORM


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
