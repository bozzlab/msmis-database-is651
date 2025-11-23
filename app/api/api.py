from fastapi import APIRouter

from app.api.api_v1.endpoints import health, category, user, transaction, user_goal


api_router = APIRouter()


api_router.include_router(health.router, tags=["health"])
api_router.include_router(category.router)
api_router.include_router(user.router)
api_router.include_router(transaction.router)
api_router.include_router(user_goal.router)
