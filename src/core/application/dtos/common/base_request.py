# -*- coding: utf-8 -*-
from typing import List

from src.core.application.dtos.common.base_config import BaseConfig


class BaseRequest(BaseConfig):
    pass


class IdListDto(BaseRequest):
    ids: List[int]
