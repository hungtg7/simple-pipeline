"""Module contains implementation for sqs transport"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from common.processing import FileLoaderRequest, FileLoaderResponse
from .service import LoaderService


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/app/")
async def load(req: FileLoaderRequest) -> FileLoaderResponse:
    try:
        logger.info(f"start loading req: {req}")
        LoaderService(req.source_name, req.date).load()
        return FileLoaderResponse(source_name=req.source_name, state="Success")
    except Exception as e:
        logger.error(e)
        return FileLoaderResponse(source_name=req.source_name, state="Failed")
