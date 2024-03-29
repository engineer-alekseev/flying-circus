from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Cookie
from typing import List, Annotated
from settings import settings
router = APIRouter(
    prefix="/booking",
    tags=["booking"]
)

@router.get("/test")
async def test_api():
    print(settings)
    print(type(settings))
    return {
        "status": 200,
        "details": "API IS UP",
        "settings": settings
    }
