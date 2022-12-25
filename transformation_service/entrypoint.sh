#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn transformation_service.http_transport:app --reload --port 8000
