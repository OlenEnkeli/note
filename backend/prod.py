#!./env/bin/python3
import os

import bjoern

from app import app
from multiprocessing import Process


def bjeorn_process(port):
    pid = os.getpid()
    print('[Run] Bjeorn on pid '+str(pid)+'. Port: '+str(port))
    bjoern.run(app, '127.0.0.1', port, reuse_port=True)


for port in range(8000, 8004):
    proc = Process(target=bjeorn_process, args=(port,))
    proc.start()
