import logging
from fastapi import FastAPI
from .routers import ai_model, file, finetune

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(debug=True)
app.include_router(ai_model.router, prefix=ai_model.prefix)
app.include_router(file.router, prefix=file.prefix)
app.include_router(finetune.router, prefix=finetune.prefix)
