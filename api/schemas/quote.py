from api import ma
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema


class QuoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteModel

    id = ma.auto_field()
    text = ma.auto_field()
    author = ma.Nested(AuthorSchema())


# Для единичного экземпляра
quote_schema = QuoteSchema()
# для списка экземпляров
quotes_schema = QuoteSchema(many=True)