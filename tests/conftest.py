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

    # Create Template dirs
    root_templates = root.mkdir('templates')
    module_templates = module.mkdir('templates')

    # Create Static dirs
    root_static = root.mkdir('static')
    module_static = module.mkdir('static')

    # Initialize our module file layout
    init = module.join('__init__.py')
    urls = module.join('urls.py')
    views = module.join('views.py')

    # Initialize our templates
    module_home = module_templates.join('home.html')
    module_help = module_templates.join('help.html')
    root_home = root_templates.join('home.html')
    root_about = root_templates.join('about.html')

    # Initialize our static files
    root_static_a = root_static.join('a.txt')
    module_static_b = module_static.join('b.txt')

    root_static_c = root_static.join('c.txt')
    module_static_c = module_static.join('c.txt')

    # Make sure our imports will function properly.
    root.join('__init__.py').write("\n")
    module_root.join('__init__.py').write("\n")

    # Setup our module files

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
        "    url('/', view_func=views.home, name='home'),",
        "    url('/help', view_func=views.help)",
        "]"
    ]))

    views.write("\n".join([
        "from flask import render_template",

        "def home():",
        "    return render_template('home.html')",

        "def help():",
        "    return render_template('help.html')"
    ]))

    # Write root templates

    root_home.write("\n".join([
        "<html>",
        "  <h1> Root! </h1>",
        "</html>"
    ]))

    root_about.write("\n".join([
        "<html>",
        "  <h1> About! </h1>",
        "</html>"
    ]))

    # Write module templates

    module_home.write("\n".join([
        "<html>",
        "  <h1> Home! </h1>",
        "</html>"
    ]))

    module_help.write("\n".join([
        "<html>",
        "  <h1> Help! </h1>",
        "</html>"
    ]))

    # Write static files

    root_static_a.write('root_a')
    module_static_b.write('module_b')

    root_static_c.write('root_c')
    module_static_c.write('module_c')

    return root


@pytest.fixture
def app(example_hierarchy):
    import os
    os.chdir(str(example_hierarchy))
    return MicroServicesApp("testapp", root_path=str(example_hierarchy))


@pytest.fixture
def blueprint():
    return Router.create_blueprint('home', 'module_home')
