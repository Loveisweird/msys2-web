# Copyright 2016-2020 Christoph Reiter
# SPDX-License-Identifier: MIT

import os
import asyncio

from fastapi import FastAPI, Request

from .web import webapp, check_is_ready
from .api import api
from .fetch import update_loop


app = FastAPI(openapi_url=None)
webapp.mount("/api", api, name="api")
app.mount("/", webapp)


# https://github.com/tiangolo/fastapi/issues/1472
if not os.environ.get("NO_MIDDLEWARE"):
    app.middleware("http")(check_is_ready)


# https://github.com/tiangolo/fastapi/issues/1480
@app.on_event("startup")
async def startup_event() -> None:
    if not os.environ.get("NO_UPDATE_THREAD"):
        asyncio.create_task(update_loop())


@webapp.exception_handler(Exception)
async def webapp_exception_handler(request: Request, exc: Exception) -> None:
    import traceback
    print(''.join(traceback.format_tb(exc.__traceback__)))
    raise exc


@api.exception_handler(Exception)
async def api_exception_handler(request: Request, exc: Exception) -> None:
    import traceback
    print(''.join(traceback.format_tb(exc.__traceback__)))
    raise exc
