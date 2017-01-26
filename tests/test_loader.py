import pytest

from flask import render_template
from flask_microservices import (
    MicroServicesLoader,
    exceptions
)


def test_loader_returns_valid_module_template(app):
    enabled_modules = [
        'home'
    ]

    app.register_urls(enabled_modules)

    # Application should respond with the proper child module template.
    with app.test_request_context('/help'):
        app.preprocess_request()
        response = app.dispatch_request()

        assert 'Help!' in response


def test_loader_returns_valid_root_template(app):
    enabled_modules = [
        'home'
    ]

    app.register_urls(enabled_modules)

    # Application should respond with the proper root template.
    @app.route('/about')
    def index():
        return render_template('about.html')

    with app.test_request_context('/about'):
        app.preprocess_request()
        response = app.dispatch_request()

        assert 'About!' in response


def test_loader_fails_correctly(app):
    enabled_modules = [
        'home'
    ]

    app.register_urls(enabled_modules)

    # Application should still fail when provided with an invalid route.
    from werkzeug.exceptions import NotFound

    with pytest.raises(NotFound):
      with app.test_request_context('/notexists'):
          app.preprocess_request()
          response = app.dispatch_request()


def test_loader_overrides_correctly(app):
    enabled_modules = [
        'home'
    ]

    app.register_urls(enabled_modules)

    # Application should respond with the proper child module template.
    with app.test_request_context('/'):
        app.preprocess_request()
        response = app.dispatch_request()

        assert 'Home!' in response
        assert 'Root!' not in response
