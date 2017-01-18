import colander

from cornice import Service
from cornice.service import get_services
from cornice.validators import colander_body_validator
from cornice_swagger.swagger import CorniceSwagger
from pyramid.view import view_config


_VALUES = {}


# Create a simple service that will store and retrieve values
values = Service(name="foo",
                 path="/values/{value}",
                 description="Cornice Demo")


# Create a body schema for our requests
class BodySchema(colander.MappingSchema):
    value = colander.SchemaNode(colander.String(),
                                description="My precious value")


# Create a response schema for our 200 responses
class OkResponseSchema(colander.MappingSchema):
    body = BodySchema()


# Aggregate the response schemas for get requests
response_schemas = {
    "200": OkResponseSchema(description="Return value")
}


# Create our cornice service views
class MyValueApi(object):
    """My precious API."""

    @values.get(response_schemas=response_schemas)
    def get_value(request):
        """Returns the value."""
        key = request.matchdict["value"]
        return {"value": _VALUES.get(key)}

    @values.put(validators=(colander_body_validator, ),
                schema=BodySchema(),
                response_schemas=response_schemas)
    def set_value(request):
        """Set the value and returns *True* or *False*."""

        key = request.matchdict["value"]
        _VALUES[key] = request.json_body
        return _VALUES.get["key"]


# Create a service to serve our OpenAPI spec
swagger = Service(name="OpenAPI",
                  path="/__api__",
                  description="OpenAPI documentation")


@swagger.get()
def openAPI_spec(request):
    my_generator = CorniceSwagger(get_services())
    my_spec = my_generator("MyAPI", "1.0.0")
    return my_spec


@view_config(route_name="swagger", renderer="templates/index.pt")
def swagger_ui(request):
    return {"request": request}
