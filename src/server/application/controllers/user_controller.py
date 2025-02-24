# -*- coding: utf-8 -*-


from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.core.application.dtos.user_dto import (
    CreateUserDto,
    UpdateUserDto,
    UserDto,
)
from src.server.application.services.user_service import UserService
from src.server.infrastructure.di.container import ServerContainer

from typing import List

router = APIRouter()


@router.post("/user", summary="유저 생성", tags=["유저"])
@inject
async def create_user(
    create_data: CreateUserDto,
    user_service: UserService = Depends(
        Provide[ServerContainer.user_service]
    ),
) -> UserDto:
    return await user_service.create_data(create_data=create_data)


@router.post("/users", summary="유저 생성 (복수)", tags=["유저"])
@inject
async def create_users(
    create_datas: List[CreateUserDto],
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserDto:
    return await user_service.create_datas(create_datas=create_datas)


@router.get("/users", summary="유저 정보 모두 조회", tags=["유저"])
@inject
async def get_users(
    page: int = 1,
    page_size: int = 10,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> List[UserDto]:
    return await user_service.get_datas(page=page, page_size=page_size)


@router.get("/user/{user_id}", summary="유저 정보 조회", tags=["유저"])
@inject
async def get_user_by_user_id(
    user_id: int,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserDto:
    return await user_service.get_data_by_data_id(data_id=user_id)


@router.put("/user/{user_id}", summary="유저 수정", tags=["유저"])
@inject
async def update_user_by_user_id(
    user_id: int,
    update_data: UpdateUserDto,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
) -> UserDto:
    user = await user_service.update_data_by_data_id(
        data_id=user_id, update_data=update_data
    )

    return UserDto(**user.model_dump())


@router.delete("/user/{user_id}", summary="유저 삭제", tags=["유저"])
@inject
async def delete_user_by_user_id(
    user_id: int,
    user_service: UserService = Depends(Provide[ServerContainer.user_service]),
):
    await user_service.delete_data_by_data_id(data_id=user_id)
