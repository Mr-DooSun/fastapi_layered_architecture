# -*- coding: utf-8 -*-
from typing import Generic, Optional, TypeVar

from src.core.application.dtos.common.base_config import ApiConfig


class PaginationInfo(ApiConfig):
    current_page: int
    page_size: int
    total_items: int
    total_pages: int
    has_previous: bool
    has_next: bool
    next_page: Optional[int] = None
    previous_page: Optional[int] = None


class ExistsData(ApiConfig):
    exists: bool


ReturnType = TypeVar("ReturnType")


class SuccessResponse(ApiConfig, Generic[ReturnType]):
    success: bool = True
    message: str = "Request processed successfully"
    data: Optional[ReturnType] = None
    pagination: Optional[PaginationInfo] = None


class ErrorResponse(ApiConfig):
    success: bool = False
    message: str = "Request failed"
    error_code: Optional[str] = None
    error_details: Optional[dict] = None
