#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn transformation_service.http_transport:app --reload --host 0.0.0.0 --port 8000 --workers 2
