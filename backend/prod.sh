#!/usr/bin/env bash

echo "
import bjoern
from app import app
bjoern.run(app, '127.0.0.1', 8000, reuse_port=True)
" | ./env/bin/python3 