from pydantic import BaseModel


class TableScheme(BaseModel):
    id: int 
    status: str 