from pydantic import BaseModel, ConfigDict


class UserScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    login: str 
    password: str  
    real_name: str 
    mail: str 
    phone_number: str | None
    
    
class UserSchemeResponse(BaseModel):   
    model_config = ConfigDict(from_attributes=True)
          
    id: int 
    login: str 
    real_name: str 
    mail: str 
    phone_number: str | None


class UserCreateScheme(UserSchemeResponse):
    login: str 
    password: str


class UserLoginScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    login: str 
    password: str