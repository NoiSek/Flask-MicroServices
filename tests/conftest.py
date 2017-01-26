import pytest

from flask_microservices import (
    MicroServicesApp,
    MicroServicesLoader,
    Router,
    url,
    exceptions
)


@pytest.fixture(scope='session')
def example_hierarchy(tmpdir_factory):
    root = tmpdir_factory.mktemp('approot', numbered=False)

    module_root = root.mkdir('modules')
    module = module_root.mkdir('home')
    templates = module.mkdir('templates')

    init = module.join('__init__.py')
    urls = module.join('urls.py')
    views = module.join('views.py')

    home = templates.join('home.html')

    root.join('__init__.py').write("\n")
    module_root.join('__init__.py').write("\n")

    init.write("\n".join([
        "from flask_microservices import Router",
        "from . import urls",

        "MODULE_NAME = 'home'",
        "IMPORT_NAME = __name__",

        "blueprint = Router.create_blueprint(MODULE_NAME, IMPORT_NAME)",
        "blueprint.register_urls(urls.urlpatterns)"
    ]))

    urls.write("\n".join([
        "from flask_microservices import url",
        "from . import views",

        "urlpatterns = [",
        "    url('/', view_func=views.home, name='home')",
        "]"
    ]))

    views.write("\n".join([
        "from flask import render_template",

        "def home():",
        "    return render_template('home.html')",
    ]))

    home.write("\n".join([
        "<html>",
        "  <h1> Home! </h1>",
        "</html>"
    ]))

    return root


@pytest.fixture
def app(example_hierarchy):
    import os
    os.chdir(str(example_hierarchy))
    return MicroServicesApp("testapp", root_path=str(example_hierarchy))


@pytest.fixture
def blueprint():
    return Router.create_blueprint('home', 'module_home')
