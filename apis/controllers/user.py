from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_all_users():
    return 'all_users'
