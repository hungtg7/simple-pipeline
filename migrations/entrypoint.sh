#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
cd migrations
alembic upgrade head
