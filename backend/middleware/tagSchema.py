from schema import ma
from marshmallow import fields

class Tag(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    description = fields.String(required=True)
    color = fields.Integer(required=True)

    class Meta():
        fields = ("id","name","description","color")

tag_schema = Tag()
tags_schmea = Tag(many=True)