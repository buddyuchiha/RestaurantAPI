from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_one_user():
    pass 

@router.get("/")
async def get_users():
    pass 

@router.post("/")
async def create_user():
    pass 

@router.put("/")
async def delete_user():
    pass 