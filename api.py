from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from loguru import logger
import os
import datetime
import time
import sys
from openai import OpenAI
from azure.ai.inference import EmbeddingsClient
from azure.core.credentials import AzureKeyCredential
########################################################
app = FastAPI()
########################################################
logger.add(sys.stderr, format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> | <level>{level: <8}</level> | <cyan>{message}</cyan>", level="INFO")
########################################################
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN is not set as an environment variable.")
########################################################
class QuestionRequest(BaseModel):
    question: str

class EmbeddingRequest(BaseModel):
    phrases: list[str]
########################################################
azure_endpoint = "https://models.inference.ai.azure.com"

OpenAIclient = OpenAI(
    base_url=azure_endpoint,
    api_key=token,
)

OpenAIEmbeddingsClient = EmbeddingsClient(
    endpoint=azure_endpoint,
    credential=AzureKeyCredential(token)
)
########################################################
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Response: {response.status_code} - Duration: {duration:.2f}s")
    return response
########################################################
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
########################################################
@app.post("/openai/{model}")
async def ask_question(model: str, request: QuestionRequest):
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
        response = OpenAIclient.chat.completions.create(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model  # Usar el modelo de la ruta
        )
        success = True
        return {
            "response": response.choices[0].message.content,
            "success": success,
            "duration": time.time() - start_time,
            "model": model  # Retornar el modelo utilizado
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        logger.info({
            "success": success,
            "duration": time.time() - start_time,
            "model": model
        })
