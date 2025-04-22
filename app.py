import os
os.system("pip install git+https://github.com/j-kirsch/watermark")

from fastapi import FastAPI
from pydantic import BaseModel
from detector import detector

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/check")
def check_text(input: TextInput):
    verdict = detector.detect(input.text)
    return {"verdict": verdict}
