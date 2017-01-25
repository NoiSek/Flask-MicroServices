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


def test_app_initializes_successfully(app):
    # Should be named correctly
    assert app.import_name == "testapp"

    # Should have a MicroServicesLoader instance
    assert isinstance(app.jinja_options['loader'], MicroServicesLoader) == True

    # Should have a brand new `register_urls` function
    assert hasattr(app, 'register_urls')
