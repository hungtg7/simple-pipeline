from pydantic import BaseModel


class FileProcessingRequest(BaseModel):
    source_name: str
    date: str


class FileProcessingResponse(BaseModel):
    source_name: str
    state: str


class FileLoaderRequest(BaseModel):
    source_name: str
    date: str


class FileLoaderResponse(BaseModel):
    source_name: str
    state: str
