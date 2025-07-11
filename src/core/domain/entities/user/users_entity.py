# -*- coding: utf-8 -*-
from datetime import datetime

from src.core.domain.entities.entity import Entity


class CoreUsersEntity(Entity):
    id: int
    username: str
    full_name: str
    email: str
    password: str
    create_at: datetime
    updated_at: datetime


class CoreCreateUsersEntity(Entity):
    username: str
    full_name: str
    email: str
    password: str


class CoreUpdateUsersEntity(Entity):
    username: str
    full_name: str
    email: str
    password: str
