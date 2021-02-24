from marshmallow import Schema, fields

from chalicelib.http_resources.request_control import Pagination
from chalicelib.openapi.schemas import DeletionSchema, RequestControlSchema, MetaSchema, LinkSchema


class StandardSchema(Schema):
    uuid = fields.UUID()
    identification = fields.Str(example="ISO 9001:2015")
    publication_date = fields.Date()
    validity_start = fields.Date()
    title = fields.Str()
    title_global_language = fields.Str()
    comite = fields.Str()
    pages = fields.Int()
    status = fields.Str(example="Arquivado")
    language = fields.Str(example="Portuguese")
    organization = fields.Str(example="ABNT - Associação Brasileira de Normas Técnicas")
    price = fields.Decimal(example=170)
    currency = fields.Str(example="BRL")
    objective = fields.Str()
    url = fields.URL()
    file = fields.Str()


class StandardCreateRequest(Schema):
    identification = fields.Str(example="ISO 9001:2015")
    publication_date = fields.Date()
    validity_start = fields.Date()
    title = fields.Str()
    title_global_language = fields.Str()
    comite = fields.Str()
    pages = fields.Int()
    status = fields.Str()
    language = fields.Str()
    organization = fields.Str()
    price = fields.Decimal()
    currency = fields.Str()
    objective = fields.Str()
    url = fields.URL()
    file = fields.Str()


class StandardUpdateRequest(StandardCreateRequest):
    pass


class StandardListResponseSchema(Schema):
    data = fields.List(fields.Nested(StandardSchema))
    control = fields.Nested(RequestControlSchema)
    meta = fields.Nested(MetaSchema)
    links = fields.List(fields.Nested(LinkSchema))


class StandardGetResponseSchema(Schema):
    data = fields.Nested(StandardSchema)
    control = fields.Nested(RequestControlSchema)
    meta = fields.Nested(MetaSchema)
    links = fields.List(fields.Nested(LinkSchema))


class StandardCreateResponseSchema(StandardGetResponseSchema):
    pass


class StandardUpdateResponseSchema(StandardGetResponseSchema):
    pass


class StandardDeleteResponseSchema(StandardGetResponseSchema):
    data = fields.Nested(DeletionSchema)
