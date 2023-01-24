from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True, error_messages={'required': {
        'message': 'name is requided', 'code': 400
    }})
    email = fields.Email(required=True, error_messages={
        'required': 'email is required'})
    # surname = fields.Str()
