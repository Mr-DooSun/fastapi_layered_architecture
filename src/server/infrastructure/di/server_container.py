# -*- coding: utf-8 -*-
from dependency_injector import containers, providers

from src.core.infrastructure.di.core_container import CoreContainer
from src.server.infrastructure.di.containers.storage_container import StorageContainer
from src.server.infrastructure.di.containers.user_container import UserContainer


class ServerContainer(containers.DeclarativeContainer):
    core_container = providers.Container(CoreContainer)

    user_container = providers.Container(UserContainer, core_container=core_container)
    storage_container = providers.Container(
        StorageContainer, core_container=core_container
    )
