from enum import Enum


class TableStatus(Enum):
    FREE = "free"
    BOOKED = "booked"
    
    
class BookingStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    
