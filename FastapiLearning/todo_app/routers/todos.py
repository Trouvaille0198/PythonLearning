from fastapi import APIRouter

router = APIRouter(
    prefix='/home',
    tags=['home!']
)


@router.get("/")
async def get_todos():
    return [{'a': 1}]
