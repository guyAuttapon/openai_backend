from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
from ..configs import openai
from ..services import request

router = APIRouter()
prefix="/files"

@router.get("/", tags=["files"])
async def get_files():
    try:
        response = request.get(url=openai.FILE_URL, headers=openai.DEFAULT_HEADER)
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response

@router.delete("/{item_id}", tags=["files"])
async def delete_files(item_id: str):
    try:
        url = openai.FILE_URL + f"/{item_id}"
        response = request.delete(url=url, headers=openai.DEFAULT_HEADER)
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response

@router.post("/uploadfiles/", tags=["files"])
async def create_upload_files(file: UploadFile):
    file_content = await file.read()
    try:
        response = request.post(
            url=openai.FILE_URL, 
            headers=openai.DEFAULT_HEADER,
            data = {
                "purpose": "fine-tune"
            },
            files = {
                "file": file_content.decode('utf-8')
            }
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response