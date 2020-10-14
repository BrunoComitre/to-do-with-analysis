from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .api.api_v1.api import router as api_router

from .core.config import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
from .core.errors import setup_exception_handlers
from .db.mongodb_utils import connect_to_mongo, disconnect_to_mongo


app = FastAPI(title=PROJECT_NAME)


if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup",connect_to_mongo)
app.add_event_handler("shutdown",disconnect_to_mongo)

setup_exception_handlers(app)

app.include_router(api_router, prefix=API_V1_STR, tags=["todo"])
