from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from loguru import logger
import os
import datetime
import time
import sys
from openai import OpenAI

app = FastAPI()

@app.get("/health")
def health_check():
    health_data = {
        "message": "Github Multi LLMs API is running",
        "status": "OK",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": os.environ.get("FLASK_ENV", "dev"),
        "version": "1.0.0"
    }
    return JSONResponse(content=health_data)
