from app.schemas import TableScheme
from app.repositories import TableRepository


class TableService:
    def __init__(self, table_repository: TableRepository) -> None:
        self.table_repository = table_repository 
    
    async def create_table(self) -> TableScheme:
        table = await self.table_repository.create()
        
        return TableScheme(id=table.id, status=table.status)