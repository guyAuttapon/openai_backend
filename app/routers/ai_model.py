from fastapi import APIRouter, HTTPException
from ..configs import openai
from ..services import request

router = APIRouter()
prefix="/models"

@router.get("/", tags=["models"])
async def get_models():
    try:
        response = request.get(url=openai.MODEL_URL, headers=openai.DEFAULT_HEADER)
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response
