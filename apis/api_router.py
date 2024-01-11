from fastapi import APIRouter
from apis.controllers import user

router = APIRouter(prefix='/api')
router.include_router(user.router, prefix='/user', tags=['user'])


