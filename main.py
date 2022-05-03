from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/test_connection")
def test_connection():
    return {"message": "Connection Successful"}
