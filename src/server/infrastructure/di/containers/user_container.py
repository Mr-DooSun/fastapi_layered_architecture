# -*- coding: utf-8 -*-

from dependency_injector import containers, providers

from src.server.application.use_cases.user.users_use_case import UsersUseCase
from src.server.domain.services.user.users_service import UsersService
from src.server.infrastructure.repositories.user.users_repository import UsersRepository


class UserContainer(containers.DeclarativeContainer):
    core_container = providers.DependenciesContainer()

    users_repository = providers.Singleton(
        UsersRepository,
        database=core_container.database,
    )

    users_service = providers.Factory(
        UsersService,
        users_repository=users_repository,
    )

    users_use_case = providers.Factory(
        UsersUseCase,
        users_service=users_service,
    )
