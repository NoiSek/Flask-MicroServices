import pytest


from flask_microservices import (
    MicroServicesApp,
    Router,
    url,
    exceptions
)


@pytest.fixture
def app():
    return MicroServicesApp("testapp")


@pytest.fixture
def blueprint():
    return Router.create_blueprint('home', 'module_home')


def test_router_returns_expected(blueprint):
    from flask import Blueprint

    assert isinstance(blueprint, Blueprint)

    assert blueprint.name == 'home'
    assert blueprint._static_url_path == '/static_home'
    assert blueprint.import_name == 'module_home'


def test_router_registers_correctly(app, blueprint):
    urlpatterns = [
      url('/', view_func=lambda x: x, name='home'),
      url('/test', view_func=lambda x: x, name='test')
    ]

    blueprint.register_urls(urlpatterns)

    # Blueprint should queue two separate routes to be added
    assert len(blueprint.deferred_functions) == 2

    blueprint.deferred_functions[0](app)
    blueprint.deferred_functions[1](app)

    # Functions should register correctly within the app
    assert 'home' in app.view_functions
    assert 'test' in app.view_functions

    # Rules should be added to the app's url map
    assert list(app.url_map.iter_rules())[0].rule == '/test'
    assert list(app.url_map.iter_rules())[1].rule == '/'


def test_router_fails_correctly(app, blueprint):
    urlpatterns = [
      url('/', view_func=lambda x: x, name='home'),
      'not a pattern',
      url('/test', view_func=lambda x: x, name='test')
    ]

    with pytest.raises(exceptions.InvalidURLPattern):
      blueprint.register_urls(urlpatterns)
