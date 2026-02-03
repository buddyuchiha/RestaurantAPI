from app.repositories import BaseRepository


class BookingRepository(BaseRepository):
    def __init__(self, session):
        self.session = session