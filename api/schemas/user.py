from api import ma
# from api.models.author import AuthorModel
# from api.models.quote import QuoteModel
from api.models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("password_hash",)


# Для единичного экземпляра
user_schema = UserSchema()
# для списка экземпляров
users_schema = UserSchema(many=True)
