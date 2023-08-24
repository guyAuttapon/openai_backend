import os

URL = "https://api.openai.com/v1"
MODEL_URL = URL + "/models"
FILE_URL = URL + "/files"
FINETUNE_URL = URL + "/fine-tunes"
APIKEY = os.environ.get("OPENAI_API_KEY")
DEFAULT_HEADER = {
    "Authorization": f"Bearer {APIKEY}"
}