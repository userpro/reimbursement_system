from fastapi import APIRouter

from app.api.endpoints import admin, subadmin, user

api_router = APIRouter()
api_router.include_router(admin.router)
api_router.include_router(subadmin.router)
api_router.include_router(user.router)
