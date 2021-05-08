from fastapi import APIRouter
from routers import todos

api_router = APIRouter()
# router注册
api_router.include_router(todos.router, prefix='/api', tags=['todo api'])
