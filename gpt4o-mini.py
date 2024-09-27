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

logger.add(sys.stderr, format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> | <level>{level: <8}</level> | <cyan>{message}</cyan>", level="INFO")

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN is not set as an environment variable.")

class QuestionRequest(BaseModel):
    question: str

azure_endpoint = "https://models.inference.ai.azure.com"
gpt4o_mini_id = "gpt-4o-mini"

client = OpenAI(
    base_url=azure_endpoint,
    api_key=token,
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    logger.info(f"Response: {response.status_code} - Duration: {duration:.2f}s")
    
    return response

@app.post("/gpt4o-mini")
async def ask_question(request: QuestionRequest):
    start_time = time.time()
    success = False

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": request.question,
        }
    ]
    
    try:
        response = client.chat.completions.create(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=gpt4o_mini_id
        )
        success = True
        return {
            "response": response.choices[0].message.content,
            "success": success,
            "duration": time.time() - start_time
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        logger.info({
            "success": success,
            "duration": time.time() - start_time
        })
