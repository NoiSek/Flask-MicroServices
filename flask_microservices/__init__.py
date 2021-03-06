from flask import Blueprint, Flask, __version__
from flask.globals import _request_ctx_stack
from flask.helpers import send_from_directory
from flask.templating import DispatchingJinjaLoader

from .exceptions import (
    InvalidModulePath,
    InvalidURLFunction,
    InvalidURLName,
    InvalidURLPattern,
    InvalidURLRule,
    UnspecifiedURLMethods
)

from collections import namedtuple
from importlib import import_module

import os
import sys

from packaging.version import parse as parse_version

FLASK_VERSION = __version__


class MicroServicesApp(Flask):
    """Extends the default Flask app to attempt to locate static
    files from Blueprints before 404'ing.
    """

    def __init__(self, name, *args, **kwargs):
        super(MicroServicesApp, self).__init__(name, *args, **kwargs)
        self.jinja_options = self.jinja_options.copy()
        self.jinja_options['loader'] = MicroServicesLoader(self)

    def register_urls(self, modules, path="modules"):
        """Resolves a given app, module list, and module path into
        usable blueprints.
        """

        cwd = self.root_path
        path = os.path.normpath(path)
        module_dir = os.path.join(cwd, path)

        # Firstly, Does this path actually exist?

        if not os.path.exists(module_dir):
            exception_message = "Invalid module path provided. With the given path, your modules should be located at {}".format(module_dir)
            raise InvalidModulePath(exception_message)

        # Let's add it to the syspath.
        sys.path.append(module_dir)

        # Register each module's blueprints to the app instance
        for module_name in modules:
            formatted_module = "{}".format(module_name)
            __module = import_module(formatted_module)
            self.register_blueprint(__module.blueprint)

        # Clean up after ourselves, because we're nice, suave gentlemen.
        sys.path.remove(module_dir)

    def send_static_file(self, filename):
        for blueprint_name, blueprint in self.blueprints.items():
            filepath = os.path.join(blueprint.static_folder, filename)

            if os.path.exists(filepath):
                return send_from_directory(blueprint.static_folder, filename)

        return super(MicroServicesApp, self).send_static_file(filename)


class Router(Blueprint):
    """URL Routing syntas xugar."""

    @classmethod
    def create_blueprint(cls, module_name, import_name):
        return cls(
            module_name,
            import_name,
            static_folder='static',
            template_folder='templates',
            static_url_path='/static_{}'.format(module_name),
            url_prefix=None
        )

    def register_urls(self, urls):
        for _url in urls:
            if 'flask_microservices.url' not in str(_url.__class__).lower():
                raise InvalidURLPattern("URLPattern not an instance of `flask_microservices.url`.")

            self.add_url_rule(
                rule=_url.rule,
                endpoint=_url.name,
                view_func=_url.view_func,
                methods=_url.methods
            )


class MicroServicesLoader(DispatchingJinjaLoader):
    """Prevent template namespace collisions between modules.

    Additionally, prefer local templates to global templates.
    This means that global templates will no longer override local templates.
    """
    def _iter_loaders(self, template):
        blueprint = _request_ctx_stack.top.request.blueprint
        if blueprint is not None and blueprint in self.app.blueprints:
            loader = self.app.blueprints[blueprint].jinja_loader
            if loader is not None:
                # Depending on the version, we must return different things.
                if parse_version(FLASK_VERSION) <= parse_version('0.10'): # pragma: no cover
                    yield loader, template
                else:
                    yield blueprint, loader

        loader = self.app.jinja_loader
        if loader is not None:
            if parse_version(FLASK_VERSION) <= parse_version('0.10'): # pragma: no cover
                yield loader, template
            else:
                yield self.app, loader


def url(rule, view_func, name=None, methods=["GET"]):
    """Simple URL wrapper for `flask_microservices.Router`.

    Usage:
    ```
    from . import views

    url('/explore/', view_func=views.explore_home, name='explore_home', methods=['GET'])
    url('/explore/', view_func=views.explore_home, name='explore_home')
    url('/explore/', views.explore_home, 'explore_home')
    url('/explore/', views.explore_home)
    ```

    # Note that 'endpoint' is now 'name'.
    # Note also that the name and view_func parameters are reversed from that
    of a normal flask URL.
    """

    if not isinstance(rule, str) or not rule:
        raise InvalidURLRule(
            "Received an invalid urlpattern `rule`: {}.".format(rule)
        )

    if not callable(view_func):
        raise InvalidURLFunction(
            "Received an invalid `view_func`: {}.".format(view_func)
        )

    if (not isinstance(name, str) and name is not None) or (isinstance(name, str) and not name):
        raise InvalidURLName(
            "Received an invalid URL `name`: {}.".format(name)
        )

    if (not isinstance(methods, list)) or len(list(filter(None, methods))) < 1:
        raise UnspecifiedURLMethods(
            "Received an empty list, or list of null strings."
        )

    __url = namedtuple('Url', ['rule', 'name', 'view_func', 'methods'])
    return __url(rule, name, view_func, methods)
