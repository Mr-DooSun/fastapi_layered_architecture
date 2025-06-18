# -*- coding: utf-8 -*-

from typing import List

from src.core.application.dtos.base_request import BaseRequest


class IdListDto(BaseRequest):
    ids: List[int]
