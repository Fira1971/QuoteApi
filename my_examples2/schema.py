from marshmallow import Schema, fields


class LearnerSchema(Schema):
    uid = fields.Integer()
    name = fields.Str(required=True, error_messages={'required': {
        'message': 'name is requided', 'code': 400
    }})
    final_test = fields.Boolean(required=True, error_messages={
        'required': 'final_test is required'})
