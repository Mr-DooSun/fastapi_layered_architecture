# -*- coding: utf-8 -*-
from datetime import datetime

from src.core.domain.entities.entity import Entity


class CoreUserEntity(Entity):
    id: int
    username: str
    full_name: str
    email: str
    password: str
    create_at: datetime
    updated_at: datetime


class CoreCreateUserEntity(Entity):
    username: str
    full_name: str
    email: str
    password: str


class CoreUpdateUserEntity(Entity):
    username: str
    full_name: str
    email: str
    password: str
