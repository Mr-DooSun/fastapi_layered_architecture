from src.core.infrastructure.database.models.user_model import UserModel
from sqladmin import ModelView


class UserView(ModelView, model=UserModel):
    column_list = [UserModel.id, UserModel.username]