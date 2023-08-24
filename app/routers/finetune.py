from fastapi import APIRouter, HTTPException

from ..model.finetune_model import Train_model
from ..configs import openai, api
from ..services import request
from ..core import log

router = APIRouter()
prefix="/finetune"

@router.get("/", tags=["finetune"])
async def get_finetune():
    try:
        response = request.get(url=openai.FINETUNE_URL, headers=openai.DEFAULT_HEADER)
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response

@router.post("/train", tags=["finetune"])
async def train(item: Train_model):
    log.info(item.model_dump())
    try:
        response = request.post(
            url=openai.FINETUNE_URL, 
            headers=openai.DEFAULT_HEADER | api.DEFAULT_HEADER,
            json=item.model_dump()
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response