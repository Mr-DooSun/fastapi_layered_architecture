# -*- coding: utf-8 -*-


from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from src.core.applications.dtos.user_dto import CreateUserDto, UpdateUserDto
from src.core.applications.responses.base import BaseResponse
from src.core.applications.responses.user_response import UserResponse
from src.server.domain.services.user_service import UserService
from src.server.infrastructure.di.container import ServerContainer

router = APIRouter()


@router.post("/user", summary="유저 생성", tags=["유저"])
@inject
async def create_user(
    create_data: CreateUserDto,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> BaseResponse:
    await user_service.create_data(create_data=create_data)
    return BaseResponse()


@router.post("/users", summary="유저 생성 (복수)", tags=["유저"])
@inject
async def create_users(
    create_datas: List[CreateUserDto],
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> BaseResponse:
    await user_service.create_datas(create_datas=create_datas)
    return BaseResponse()


@router.get("/users", summary="유저 정보 모두 조회", tags=["유저"])
@inject
async def get_users(
    page: int = 1,
    page_size: int = 10,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserResponse:
    datas = await user_service.get_datas(page=page, page_size=page_size)
    encoded_data = jsonable_encoder(datas)
    return UserResponse(data=encoded_data)


@router.get("/user/{user_id}", summary="유저 정보 조회", tags=["유저"])
@inject
async def get_user_by_user_id(
    user_id: int,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserResponse:
    data = await user_service.get_data_by_data_id(data_id=user_id)
    encoded_data = jsonable_encoder(data)
    return UserResponse(data=encoded_data)


@router.put("/user/{user_id}", summary="유저 수정", tags=["유저"])
@inject
async def update_user_by_user_id(
    user_id: int,
    update_data: UpdateUserDto,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserResponse:
    user = await user_service.update_data_by_data_id(
        data_id=user_id, update_data=update_data
    )
    encoded_data = jsonable_encoder(user)

    return UserResponse(data=encoded_data)


@router.delete("/user/{user_id}", summary="유저 삭제", tags=["유저"])
@inject
async def delete_user_by_user_id(
    user_id: int,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> BaseResponse:
    await user_service.delete_data_by_data_id(data_id=user_id)
    return BaseResponse()
