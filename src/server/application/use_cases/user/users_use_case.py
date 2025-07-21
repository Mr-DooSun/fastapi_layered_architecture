# -*- coding: utf-8 -*-


from src.core.application.use_cases.base_use_case import BaseUseCase
from src.core.domain.entities.user.users_entity import (
    CoreCreateUsersEntity,
    CoreUpdateUsersEntity,
    CoreUsersEntity,
)
from src.server.domain.services.user.users_service import UsersService


class UsersUseCase(
    BaseUseCase[CoreCreateUsersEntity, CoreUsersEntity, CoreUpdateUsersEntity]
):
    def __init__(self, users_service: UsersService) -> None:
        super().__init__(
            base_service=users_service,
            create_entity=CoreCreateUsersEntity,
            return_entity=CoreUsersEntity,
            update_entity=CoreUpdateUsersEntity,
        )
