from app.api.handlers.booking import router as booking_router
from app.api.handlers.table import router as table_router
from app.api.handlers.user import router as user_router


routers = [booking_router, table_router, user_router]