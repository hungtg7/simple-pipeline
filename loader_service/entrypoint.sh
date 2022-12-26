#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn loader_service.http_transport:app --reload --host 0.0.0.0 --port 8001 --workers 2
