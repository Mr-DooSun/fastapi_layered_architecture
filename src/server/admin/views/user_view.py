# -*- coding: utf-8 -*-
from sqladmin import ModelView
from sqlalchemy.orm import class_mapper

from src.core.infrastructure.database.models.user_model import UserModel


class UserView(ModelView, model=UserModel):
    category = "유저"
    name = "유저 목록"
    column_list = [attr.key for attr in class_mapper(UserModel).column_attrs]

    column_labels = {
        "id": "ID",
        "username": "이름",
        "email": "이메일",
        "created_at": "가입일",
        "updated_at": "수정일",
    }

    column_searchable_list = ["username", "email"]
    column_filters = ["created_at"]
    column_sortable_list = ["id", "created_at"]
