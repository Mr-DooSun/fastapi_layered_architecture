# -*- coding: utf-8 -*-

from src.core.domain.entities.user_entity import (
    CoreCreateUserEntity,
    CoreUpdateUserEntity,
    CoreUserEntity,
)
from src.core.infrastructure.database.database import Database
from src.core.infrastructure.database.models.user.users_model import UsersModel
from src.core.infrastructure.repositories.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    def __init__(self, database: Database) -> None:
        super().__init__(database=database)

    @property
    def model(self):
        return UsersModel

    @property
    def create_entity(self):
        return CoreCreateUserEntity

    @property
    def return_entity(self):
        return CoreUserEntity

    @property
    def update_entity(self):
        return CoreUpdateUserEntity
