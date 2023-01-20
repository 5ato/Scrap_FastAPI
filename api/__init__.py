from fastapi import APIRouter

from .material import router as rt_material


router = APIRouter()
router.include_router(rt_material)
