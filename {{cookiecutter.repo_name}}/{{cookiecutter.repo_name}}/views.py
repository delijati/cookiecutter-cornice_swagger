""" Cornice services.
"""
from cornice import Service
from cornice.service import get_services
from cornice_swagger.swagger import generate_swagger_spec
from pyramid.view import view_config
from cornice.resource import resource
from cornice.resource import view
from cornice.validators import colander_validator

import colander


USERS = {1: {"name": "gawel"}, 2: {"name": "tarek"}}


class Integers(colander.SequenceSchema):
    integer = colander.SchemaNode(colander.Integer())


class Body(colander.MappingSchema):
    # {{cookiecutter.repo_name}} and bar are required, baz is optional
    {{cookiecutter.repo_name}} = colander.SchemaNode(colander.String())
    ipsum = colander.SchemaNode(colander.Integer(), missing=1,
                                validator=colander.Range(0, 3))
    integers = Integers(missing=())


class Query(colander.MappingSchema):
    yeah = colander.SchemaNode(colander.String())
    mau = colander.SchemaNode(colander.String())


class RequestSchema(colander.MappingSchema):
    body = Body(description="Defines a cornice body schema")
    querystring = Query()


hello = Service(name="hello",
                path="/{hans}",
                description="Complex app")
person = Service(name="person",
                 path="/{pers_id}/bla/{car_id}",
                 description="Complex ** 2")


@hello.post(validators=(colander_validator, ), schema=RequestSchema())
def post_info(request):
    """Returns Hello in JSON."""
    return {"Hello": "World"}


@resource(collection_path="/users", path="/users/{id}",
          name="user_service")
class User(object):

    def __init__(self, request, context=None):
        self.request = request
        self.context = context

    def collection_get(self):
        return {"users": list(USERS.keys())}

    @view(renderer="json")
    def get(self):
        return USERS.get(int(self.request.matchdict["id"]))

    @view(renderer="json", content_type="application/json",
          validators=(colander_validator, ),
          schema=RequestSchema())
    def collection_post(self):
        return {"test": "yeah"}

    def patch(self):
        return {"test": "yeah"}

    def collection_patch(self):
        return {"test": "yeah"}

    def put(self):
        return dict(type=repr(self.context))


@view_config(route_name="swagger", renderer="templates/index.pt")
def swagger(request):
    return {"request": request}


@view_config(route_name="swagger_json", renderer="json")
def swagger_json(request):
    info = {"title": "Joes API", "version": "0.1", "contact": {
            "name": "Joe Smith",
            "email": "joe.cool@swagger.com"}
            }
    base_path = "/"
    services = get_services()
    spec = generate_swagger_spec(services, info["title"],
                                 info["version"], info=info,
                                 base_path=base_path, head=False)
    return spec
