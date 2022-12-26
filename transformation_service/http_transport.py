"""Module contains implementation for sqs transport"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from common.processing import FileProcessingRequest, FileProcessingResponse
from .service import TransformationService


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping/")
async def ping():
    return "Hello"


@app.post("/app/")
async def load(req: FileProcessingRequest):
    try:
        logger.info(f"start processing req: {req}")
        TransformationService(req.source_name, req.date).processing_file()
        return FileProcessingResponse(
            source_name=req.source_name, state="Success")
    except Exception as e:
        logger.error(e)
        return FileProcessingResponse(
            source_name=req.source_name, state="Failed")
