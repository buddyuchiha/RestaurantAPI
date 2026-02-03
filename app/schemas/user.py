from pydantic import BaseModel, ConfigDict, Field


class UserScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
     
    real_name: str 
    mail: str 
    phone_number: str | None
    
class UserSchemeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
     
    id: int
    real_name: str 
    mail: str 
    phone_number: str | None