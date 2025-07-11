# -*- coding: utf-8 -*-


from src.core.application.dtos.user.users_dto import (
    CoreCreateUsersDto,
    CoreUpdateUsersDto,
    CoreUsersDto,
)
from src.core.application.use_cases.base_use_case import BaseUseCase
from src.server.domain.services.user.users_service import UsersService


class UsersUseCase(BaseUseCase):
    def __init__(self, users_service: UsersService) -> None:
        super().__init__(base_service=users_service)

    @property
    def create_dto(self):
        return CoreCreateUsersDto

    @property
    def response_dto(self):
        return CoreUsersDto

    @property
    def update_dto(self):
        return CoreUpdateUsersDto
