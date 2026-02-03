from app.schemas import TableScheme
from app.repositories import TableRepository


class TableService:
    def __init__(self, table_repository: TableRepository) -> None:
        self.table_repository = table_repository 
    
    async def create_table(self) -> TableScheme:
        table = await self.table_repository.create()
        
        return TableScheme.model_validate(table)
    
    async def get_table(self, id: int) -> TableScheme:
        table = await self.table_repository.get_one(id)
        
        return TableScheme.model_validate(table)
    
    async def get_tables(self) -> list[TableScheme]:
        tables = await self.table_repository.get_all()
        
        return [TableScheme.model_validate(table) for table in tables]

    async def update_table(self, id: int, status: str) -> TableScheme:
        table = await self.table_repository.update(id, status)
        
        return TableScheme.model_validate(table)
    
    async def delete_table(self, id: int) -> bool:
        return await self.table_repository.delete(id)