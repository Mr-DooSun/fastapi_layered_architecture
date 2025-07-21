# -*- coding: utf-8 -*-
from abc import ABC
from typing import Generic, List, Type, TypeVar

from src.core.domain.entities.entity import Entity
from src.core.infrastructure.repositories.base_repository import BaseRepository

CreateEntity = TypeVar("CreateEntity", bound=Entity)
ReturnEntity = TypeVar("ReturnEntity", bound=Entity)
UpdateEntity = TypeVar("UpdateEntity", bound=Entity)


class BaseService(Generic[CreateEntity, ReturnEntity, UpdateEntity], ABC):
    def __init__(
        self,
        base_repository: BaseRepository,
        *,
        create_entity: Type[CreateEntity],
        return_entity: Type[ReturnEntity],
        update_entity: Type[UpdateEntity],
    ) -> None:
        self.base_repository = base_repository
        self.create_entity = create_entity
        self.return_entity = return_entity
        self.update_entity = update_entity

    async def create_data(self, create_data: CreateEntity) -> ReturnEntity:
        data = await self.base_repository.create_data(create_data=create_data)
        return self.return_entity.model_validate(data, from_attributes=True)

    async def create_datas(
        self, create_datas: List[CreateEntity]
    ) -> List[ReturnEntity]:
        datas = await self.base_repository.create_datas(create_datas=create_datas)
        return [
            self.return_entity.model_validate(data, from_attributes=True)
            for data in datas
        ]

    async def get_datas(self, page: int, page_size: int) -> List[ReturnEntity]:
        datas = await self.base_repository.get_datas(page=page, page_size=page_size)
        return [
            self.return_entity.model_validate(data, from_attributes=True)
            for data in datas
        ]

    async def get_data_by_data_id(self, data_id: int) -> ReturnEntity:
        data = await self.base_repository.get_data_by_data_id(data_id=data_id)
        return self.return_entity.model_validate(data, from_attributes=True)

    async def get_datas_by_data_ids(self, data_ids: List[int]) -> List[ReturnEntity]:
        datas = await self.base_repository.get_datas_by_data_ids(data_ids=data_ids)
        return [
            self.return_entity.model_validate(data, from_attributes=True)
            for data in datas
        ]

    async def count_datas(self) -> int:
        return await self.base_repository.count_datas()

    async def update_data_by_data_id(
        self, data_id: int, update_data: UpdateEntity
    ) -> ReturnEntity:
        data = await self.base_repository.update_data_by_data_id(
            data_id=data_id, update_data=update_data
        )
        return self.return_entity.model_validate(data, from_attributes=True)

    async def delete_data_by_data_id(self, data_id: int) -> bool:
        return await self.base_repository.delete_data_by_data_id(data_id=data_id)
