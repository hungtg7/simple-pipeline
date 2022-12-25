from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel


class ProcessingState(Enum):
    """Processing state of the current file"""
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


@dataclass
class FileProcessingRequest(BaseModel):
    source_name: str
    date: str


@dataclass
class FileProcessingResponse(BaseModel):
    source_name: str
    state: ProcessingState


@dataclass
class FileLoaderRequest(BaseModel):
    source_name: str
    date: str


@dataclass
class FileLoaderResponse(BaseModel):
    source_name: str
    state: ProcessingState
