import logging
import logging.config
from os import path

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, Response
from starlette.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.core.settings import settings


# Uncomment to see SqlAlchemy log
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
LOGGER = logging.getLogger("AppLogger")
LOGGER.info("Initialized AppLogger")

app = FastAPI(title=settings.PROJECT_NAME, openapi_url="/api/v1/openapi.json")


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception) -> Response:
    """
    The generic_exception_handler ensures unhandled exceptions are returned
    as HTTP 500 responses with structured JSON error details, leveraging
    Starlette's exception system and FastAPI's decorator pattern.
    """
    LOGGER.error(exc, exc_info=1)

    return JSONResponse(
        {"detail": "Unable to process request"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


app.include_router(api_router, prefix=settings.API_PATH_STR)
