from enum import Enum


class TableStatus(Enum):
    FREE = "free"
    BOOKED = "booked"
    
    
class BookingStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    

class UserUpdateField(Enum):
    NAME = "real_name"
    MAIL = "mail"
    PHONE = "phone_number"
    
    
class BookingUpdateField(Enum):
    USER = "user_id"
    TABLE = "table_id"
    DATETTIME = "datetime"