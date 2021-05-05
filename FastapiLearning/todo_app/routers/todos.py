from fastapi import APIRouter

router = APIRouter(
    prefix='/todos',
    tags=['todo']
)


@router.get("/")
async def get_todos():
    return [{}]
