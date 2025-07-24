# -*- coding: utf-8 -*-
from dependency_injector import containers, providers
from minio import Minio

from src.core.application.messaging.rabbitmq_publisher import RabbitMQPublisher
from src.core.infrastructure.database.database import Database
from src.core.infrastructure.messaging.rabbitmq_manager import RabbitMQManager


class CoreContainer(containers.DeclarativeContainer):
    config = providers.Configuration(strict=True)
    config.from_yaml("./config.yml")

    #########################################################
    # Database
    #########################################################

    database = providers.Singleton(
        Database,
        database_user=config.database.user,
        database_password=config.database.password,
        database_host=config.database.host,
        database_port=config.database.port,
        database_name=config.database.name,
    )

    #########################################################
    # Storage
    #########################################################

    minio_client = providers.Singleton(
        Minio,
        endpoint=config.minio.endpoint,
        access_key=config.minio.access_key,
        secret_key=config.minio.secret_key,
        secure=False,  # HTTPS가 아닌 경우 False 설정
    )

    #########################################################
    # Messaging
    #########################################################

    rabbitmq_manager = providers.Singleton(
        RabbitMQManager,
        host=config.rabbitmq.host,
        port=config.rabbitmq.port,
    )

    rabbitmq_publisher = providers.Factory(
        RabbitMQPublisher, rabbitmq_manager=rabbitmq_manager
    )
