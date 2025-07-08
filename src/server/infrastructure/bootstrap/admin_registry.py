from fastapi import FastAPI
from src.server.admin.views.user_view import UserView
from src.core.infrastructure.database.database import Database

from sqladmin import Admin


def setup_admin_views(app: FastAPI, database: Database):
    admin = Admin(app=app, engine=database.engine)

    admin.add_view(UserView)