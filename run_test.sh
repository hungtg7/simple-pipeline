#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pip3 install -r dev_requirements.txt 
python scripts/test.py $1 $2
