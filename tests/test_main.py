import pytest

from flask_microservices import (
    MicroServicesApp,
    MicroServicesLoader,
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


def test_app_initializes_successfully(app):
    # Should be named correctly
    assert app.import_name == "testapp"

    # Should have a MicroServicesLoader instance
    assert isinstance(app.jinja_options['loader'], MicroServicesLoader) == True

    # Should have a brand new `register_urls` function
    assert hasattr(app, 'register_urls')


def test_url_returns_valid_simple():
    from collections import namedtuple

    _url = url(rule='/', view_func=lambda x: x)

    # Should return a namedtuple
    assert isinstance(_url, tuple)
    assert hasattr(_url, '_fields')

    # Should default to GET as a method
    assert _url.methods == ['GET']

    # Should not provide a name if not given one.
    assert _url.name is None


def test_url_returns_valid_complex():
    # Should still return correct values when provided unnamed arguments
    _url = url('/', lambda x: x)

    assert _url.view_func(1) == 1
    assert _url.methods == ['GET']
    assert _url.name is None

    # Should return correct values when provided a full list of unnamed arguments.
    _url = url('/', lambda x: x, 'home', ['GET', 'POST'])

    assert _url.view_func(3) == 3
    assert _url.methods == ['GET', 'POST']
    assert _url.name == 'home'

    # Should return correct values when provided a full list of named arguments.
    _url = url(rule='/', view_func=lambda x: x, name='_home', methods=['GET', 'POST', 'PUT'])

    assert _url.view_func(5) == 5
    assert _url.methods == ['GET', 'POST', 'PUT']
    assert _url.name == '_home'

    # Should return correct values when provided a mixture of named and unnamed arguments.
    _url = url('/', lambda x: x, name='home', methods=['GET', 'PUT'])

    assert _url.view_func(7) == 7
    assert _url.methods == ['GET', 'PUT']
    assert _url.name == 'home'


def test_router_returns_expected(blueprint):
    from flask import Blueprint
    assert isinstance(blueprint, Blueprint)


