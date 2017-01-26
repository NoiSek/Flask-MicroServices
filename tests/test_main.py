import pytest

from flask_microservices import (
    MicroServicesLoader,
    exceptions
)


def test_app_initializes_successfully(app):
    # Should be named correctly
    assert app.import_name == "testapp"

    # Should have a MicroServicesLoader instance
    assert isinstance(app.jinja_options['loader'], MicroServicesLoader) == True

    # Should have a brand new `register_urls` function
    assert hasattr(app, 'register_urls')


def test_app_registers_modules_correctly(app):
    enabled_modules = [
        'home'
    ]

    app.register_urls(enabled_modules)

    # Should create a blueprint
    assert 'home' in app.blueprints

    blueprint = app.blueprints['home']

    # Blueprint should match our `conftest.py` schema
    assert blueprint.name == 'home'
    assert blueprint.import_name == 'home'


def test_app_fails_on_invalid_modules(app):
    enabled_modules = [
        'doesntexist'
    ]

    with pytest.raises(ImportError):
        app.register_urls(enabled_modules)

    # Should not create a blueprint
    assert 'doesntexist' not in app.blueprints


def test_app_fails_on_invalid_module_path(app):
    enabled_modules = [
        'home'
    ]

    with pytest.raises(exceptions.InvalidModulePath):
        app.register_urls(enabled_modules, path="fakepath")

    # Should not create a blueprint
    assert 'home' not in app.blueprints
