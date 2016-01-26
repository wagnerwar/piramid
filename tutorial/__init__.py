from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def videos_include(config):
    config.add_route('cadastrar', '/cadastrar')
    config.add_route('consulta', '/')
    config.add_route('edicao', '/editar')
    config.add_route('exclusao', '/excluir')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.include(videos_include, route_prefix='/videos')
    config.scan()
    return config.make_wsgi_app()
