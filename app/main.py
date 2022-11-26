from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.config import config
from app.models.exceptions import add_exception_handlers, catch_unhandled_exceptions
from app.routers.auth import router as auth_router
from app.routers.user import router as users_router

tags_metadata = [
    {"name": "auth", "description": "Авторизация"},
    {"name": "users", "description": "Работа с пользователями"},
]

app = FastAPI(
    debug=config.BACKEND_DEBUG,
    openapi_tags=tags_metadata,
    openapi_url=f"{config.BACKEND_PREFIX}/openapi.json",
    title=config.BACKEND_TITLE,
    description=config.BACKEND_DESCRIPTION,
    docs_url='/api/docs'
)

# app.middleware("http")(catch_unhandled_exceptions)
# add_exception_handlers(app)

# backend_origins = [
#     config.BACKEND_CORS_ORIGINS,
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# app.mount("/static", StaticFiles(directory="./app/docs"), name="static")
app.include_router(auth_router, tags=["auth"])
app.include_router(users_router, tags=["users"])