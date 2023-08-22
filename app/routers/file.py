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


@router.post("/uploadfiles/", tags=["files"])
async def create_upload_files(file: UploadFile):
    try:
        response = request.post(
            url=openai.FILE_URL, 
            headers=openai.DEFAULT_HEADER,
            data = {
                "purpose": "fine-tune"
            },
            files = {
                "file": file.file.read
            }
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
    return response


@router.get("/upload", tags=["files"])
async def upload():
    content = """
<body>
<form action="/files/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
