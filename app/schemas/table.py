from pydantic import BaseModel, ConfigDict

from app.core import TableStatus 


class TableScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int 
    status: TableStatus