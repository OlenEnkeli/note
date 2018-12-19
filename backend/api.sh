#!/usr/bin/env bash

./venv/bin/gunicorn app:app -b 0.0.0.0:8000 --reload