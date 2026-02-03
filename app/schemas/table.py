from pydantic import BaseModel, ConfigDict


class TableScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int 
    status: str 