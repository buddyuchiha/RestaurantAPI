from app.api.handlers.booking import router as booking_router
from app.api.handlers.table import router as table_router
from app.api.handlers.user import router as user_router
from app.api.handlers.auth import router as auth_router


routers = [booking_router, table_router, user_router, auth_router]