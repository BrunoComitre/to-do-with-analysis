from collections.abc import Iterable

from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import (
    validation_error_definition,
    validation_error_response_definition,
)
from fastapi import HTTPException, Request, status, FastAPI
from fastapi.responses import UJSONResponse, JSONResponse
from bson.errors import InvalidId


async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": [exc.detail]})

async def http_422_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """ Handler for 422 error to transform default pydantic error object to gothinkster format """

    errors = {"body": []}

    if isinstance(exc.detail, Iterable) and not isinstance(exc.detail, str):  # check if error is pydantic's model error
        for error in exc.detail:
            error_name = ".".join(
                error["loc"][1:]
            )  # remove 'body' from path to invalid element
            errors["body"].append({error_name: error["msg"]})
    else:
        errors["body"].append(exc.detail)

    return JSONResponse({"errors": errors}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


async def objectid_invalid_exception_handler(request: Request, exec: InvalidId)-> UJSONResponse:
    return UJSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Note not found"})

validation_error_definition["properties"] = {
    "body": {"title": "Body", "type": "array", "items": {"type": "string"}}
}

validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": REF_PREFIX + "ValidationError"},
    }
}

def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidId, objectid_invalid_exception_handler)
    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(status.HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)
