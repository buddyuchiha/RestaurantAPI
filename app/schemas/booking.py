from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.core import BookingStatus


class BookingSchemeInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    table_id: int 
    datetime: datetime
    status: BookingStatus
    
    
class BookingScheme(BookingSchemeInput): 
    user_id: int 
    

class BookingSchemeResponse(BookingScheme):
    id: int    