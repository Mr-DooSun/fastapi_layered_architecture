# -*- coding: utf-8 -*-

from src.core.application.dtos.common.base_request import BaseRequest
from src.core.domain.entities.user.users_entity import (
    CoreCreateUsersEntity,
    CoreUpdateUsersEntity,
    CoreUsersEntity,
)


class CoreUsersDto(CoreUsersEntity):
    pass


class CoreCreateUsersDto(BaseRequest, CoreCreateUsersEntity):
    pass


class CoreUpdateUsersDto(BaseRequest, CoreUpdateUsersEntity):
    pass
