#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from fastapi import FastAPI
from routers import rumour_verif

# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logger to log messages
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = 0

# console logger with high level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

# file logger with low level
fh = logging.FileHandler('server.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)


app = FastAPI()

app.include_router(rumour_verif.router)


@app.get('/')
async def root():
    return {
        'name': 'coinform-content-analysis',
        'docs': '/docs'
    }
