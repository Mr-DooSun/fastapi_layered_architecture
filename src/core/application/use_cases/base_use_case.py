# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List, Tuple, Type, TypeVar

from pydantic import BaseModel

from src.core.application.dtos.common.base_request import IdListDto
from src.core.application.dtos.common.base_response import PaginationInfo
from src.core.common.pagination import make_pagination
from src.core.domain.services.base_service import BaseService

CreateDTO = TypeVar("CreateDTO", bound=BaseModel)
UpdateDTO = TypeVar("UpdateDTO", bound=BaseModel)
ResponseDTO = TypeVar("ResponseDTO", bound=BaseModel)


class BaseUseCase(ABC):
    def __init__(
        self,
        base_service: BaseService,
    ) -> None:
        self.base_service = base_service

    @property
    @abstractmethod
    def create_dto(self) -> Type[CreateDTO]:
        pass

    @property
    @abstractmethod
    def response_dto(self) -> Type[ResponseDTO]:
        pass

    @property
    @abstractmethod
    def update_dto(self) -> Type[UpdateDTO]:
        pass

    async def create_data(self, create_data: CreateDTO) -> ResponseDTO:
        return await self.base_service.create_data(create_data=create_data)

    async def create_datas(self, create_datas: List[CreateDTO]) -> List[ResponseDTO]:
        return await self.base_service.create_datas(create_datas=create_datas)

    async def get_datas(
        self, page: int, page_size: int
    ) -> Tuple[List[ResponseDTO], PaginationInfo]:
        datas = await self.base_service.get_datas(page=page, page_size=page_size)

        total_items = await self.base_service.count_datas()
        pagination = make_pagination(
            total_items=total_items, page=page, page_size=page_size
        )

        return datas, pagination

    async def get_data_by_data_id(self, data_id: int) -> ResponseDTO:
        return await self.base_service.get_data_by_data_id(data_id=data_id)

    async def get_datas_by_data_ids(self, payload: IdListDto) -> List[ResponseDTO]:
        return await self.base_service.get_datas_by_data_ids(data_ids=payload.ids)

    async def update_data_by_data_id(
        self, data_id: int, update_data: UpdateDTO
    ) -> ResponseDTO:
        return await self.base_service.update_data_by_data_id(
            data_id=data_id, update_data=update_data
        )

    async def delete_data_by_data_id(self, data_id: int) -> bool:
        return await self.base_service.delete_data_by_data_id(data_id=data_id)
