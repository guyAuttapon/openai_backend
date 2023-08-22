from fastapi import APIRouter, HTTPException
from ..configs import openai
from ..services import request

router = APIRouter()
prefix="/finetune"

@router.get("/", tags=["finetune"])
async def get_finetune():
    try:
        response = request.get(url=openai.FINETUNE_URL, headers=openai.DEFAULT_HEADER)
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response
