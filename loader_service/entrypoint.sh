#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
uvicorn loader_service.http_transport:app --reload --port 8001
