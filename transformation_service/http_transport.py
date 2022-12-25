"""Module contains implementation for sqs transport"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from common.processing import FileProcessingRequest, FileProcessingResponse
from .service import TransformationService


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/app/")
async def load(req: FileProcessingRequest):
    try:
        logger.info(f"start processing req: {req}")
        TransformationService(req.source_name, req.date).load()
        return FileProcessingResponse(
            source_name=req.source_name, state="Success")
    except Exception as e:
        logger.Exception(e)
        return FileProcessingResponse(
            source_name=req.source_name, state="Failed")
