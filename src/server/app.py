# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.middleware.exception_middleware import ExceptionMiddleware
from src.server.application.controllers import health_check_controller, user_controller
from src.server.infrastructure.di.server_container import ServerContainer

container = None


def create_container():
    container = ServerContainer()
    container.wire(packages=["src.server.application.controllers"])

    return container


def create_app():
    global container
    container = create_container()

    app = FastAPI(docs_url="/docs")
    app.add_middleware(ExceptionMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(router=health_check_controller.router)
    app.include_router(router=user_controller.router)

    return app


app = create_app()
