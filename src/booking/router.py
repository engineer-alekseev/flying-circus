from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Cookie

from typing import List, Annotated

router = APIRouter(
    prefix="/booking",
    tags=["booking"]
)

@router.get("/test")
async def test_api():
    return {
        "status": 200,
        "details": "API IS UP"
    }
