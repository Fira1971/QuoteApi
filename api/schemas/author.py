from api import ma
from api.models.author import AuthorModel
from api.models.quote import QuoteModel


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel


# Для единичного экземпляра
author_schema = AuthorSchema()
# для списка экземпляров
authors_schema = AuthorSchema(many=True)
