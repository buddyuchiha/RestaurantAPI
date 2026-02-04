from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.core import BookingStatus


class BookingScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: int 
    table_id: int 
    datetime: datetime
    status: BookingStatus
    
    
class BookingSchemeInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    table_id: int 
    datetime: datetime
    status: BookingStatus
    
    
class BookingSchemeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int    
    user_id: int 
    table_id: int 
    datetime: datetime
    status: BookingStatus