"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.include("pyramid_chameleon")
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("swagger", "/swagger")
    config.add_route("swagger_json", "/swagger_json")
    config.scan("{{cookiecutter.repo_name}}.views")
    return config.make_wsgi_app()