# -*- coding: utf-8 -*-
from abc import ABC
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

dto_model_config = ConfigDict(
    extra="ignore",
    frozen=True,
    populate_by_name=True,
    loc_by_alias=True,
    alias_generator=to_camel,
    ser_json_timedelta="iso8601",
    ser_json_bytes="utf8",
)


class PaginationInfo(BaseModel):
    current_page: int
    page_size: int
    total_items: int
    total_pages: int
    has_previous: bool
    has_next: bool
    next_page: int
    previous_page: int


class BaseResponse(ABC, BaseModel):
    success: bool = True
    message: str = "Request processed successfully"
    data: Optional[Any] = None
    pagination: Optional[PaginationInfo] = None

    model_config = dto_model_config
