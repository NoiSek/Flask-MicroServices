[![Build Status](https://travis-ci.org/NoiSek/Flask-MicroServices.svg?branch=master)](https://travis-ci.org/NoiSek/Flask-MicroServices)
[![Coverage Status](https://coveralls.io/repos/github/NoiSek/Flask-MicroServices/badge.svg?branch=master)](https://coveralls.io/github/NoiSek/Flask-MicroServices?branch=master)
[![PyPI](https://img.shields.io/pypi/v/flask-microservices.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/flask-microservices.svg)]()

# `Flask-MicroServices`

Flask-MicroServices is a simple, lightweight attempt at bringing self contained module hierarchy to Flask. Better project organization through separation of concerns, isolating the different sections of your app into separate modules, or 'microservices'.

An opinionated, but minimal approach to higher maintainability with Flask.


### Features

- Django style route definitions
- Simple, modular, microservices inspired architecture
- Dynamic, overridable resolution of Static / Template directories


### Problems this plugin solves:

- Allow Blueprint defined template folders to override parent templates, rather than the other way around
- Allow Blueprint defined static folders to resolve from and override `/static`, rather than having to define individual `/static_module_name` folders
- Enable modular, but centralized definition of routes with a cleaner syntax so that you aren't forced to hunt for `@app.route()` decorators or use the arcane blueprint syntax in complex projects
- Allow you to drop in / drop out sections of functionality at will just by passing the name of the module for portability, testing, and modularity

Flask-MicroServices is not exceptionally complex. In fact, it is quite small-- 200-ish lines of code, but it can bring a high level of reasonability to the way you write your Flask applications.


### Usage

Check out the example project at [./example](example), or read below for a minimal example use-case.

- [Project Layout](#project-layout)
  - [`__init__.py`](#approot-init)
  - `modules/`
    - `home/`
      - `static/`
        - [`file.txt`](#module-static-file)
      - `templates/`
        - [`main.html`](#module-template)
      - [`__init__.py`](#module-init)
      - [`urls.py`](#module-urls)
      - [`views.py`](#module-views)

#### Project Layout

##### Approot Init

`project_root/appname/__init__.py`


You don't necessarily *have* to define your app within `__init__.py`, but this is how we will initialize our app for the purpose of this example.

```python
from flask_microservices import MicroServicesApp

app = MicroServicesApp(__name__)

enabled_modules = [
    # Normally, we'd define more modules to enable:

    # 'home',
    # 'forum',
    # 'settings',

    # We will enable just one, for now:

    'admin'
]

# By default, this will assume your modules directory is "./modules" if a second argument is not provided.
app.register_urls(enabled_modules)
app.run()
```

#### Module Init

`project_root/appname/admin/__init__.py`


This is the heart of every module, and is required for the app to be able to enable it.

```python
from flask_microservices import Router
from . import urls

MODULE_NAME = 'admin'
IMPORT_NAME = __name__

# These blueprints are what is collected when you run app.register_urls()
blueprint = Router.create_blueprint(MODULE_NAME, IMPORT_NAME)
blueprint.register_urls(urls.urlpatterns)
```

#### Module Urls

`project_root/appname/admin/urls.py`


Your URL definitions for each module go here. Routes defined here follow all the normal patterns of [`@app.route()`](http://flask.pocoo.org/docs/0.12/api/#url-route-registrations), with the exception of `endpoint` being renamed to `name`, and the order of `view_func` and `name` being reversed.

When a name is provided here, as with a normal blueprint it will become namespaced. A value of `name='home'` will become resolveable with `url_for('admin.home')`.

```python
from flask_microservices import url
from . import views

urlpatterns = [
    url('/admin/', view_func=views.admin_panel, name='home'),

    ## Example URLs:

    ### Minimal:
    # url('/admin/simple/', view_func=views.admin_simple)

    ### Advanced
    # url('/admin/roles/add/', view_func=views.admin_panel_roles_add, name='role_add', methods=['GET', 'POST']),
    # url('/admin/roles/edit/', view_func=views.admin_panel_roles_edit, name='role_edit', methods=['GET', 'POST']),
]
```

#### Module Views

`project_root/appname/admin/views.py`

This is where your views are defined. As your project scales farther, you may want to separate your logic into files such as `a.py`, `b.py`, and import them into your `views.py` with `from . import a, b` in order to make them visible to `urls.py`.

```python
from flask import render_template
from ExampleApp.ExampleWrappers import admin_access_required

@admin_access_required
def admin_panel():
    return render_template('admin/main.html')
```

#### Module Template

`project_root/appname/admin/templates/admin/main.html`

Templates folder resolves as normal. The `MicroServicesApp` instance will check all module template directories before trying to resolve from the root template folder. An important caveat to this approach is to remember that when two modules both possess conflicting templates, they will be resolved in the order that they were defined in the `enabled_modules` value that you passed to `app.register_urls()`.

```html
<html>
  <h1> Holy cow! </h1>
  <p> If the router was unable to find this file, then it would try your root level templates folder at `project_root/appname/templates/admin/main.html` before failing.</p>
</html>
```

#### Module Static File

`project_root/appname/admin/static/file.txt`

Static folder resolves as normal. The `MicroServicesApp` instance will behave with respect to static files in an identical manner to how it handles template files. See [above](#module-views) for caveats.

```
I am a file! If I could not be found, the Router would attempt to find `project_root/appname/static/file.txt` before 404'ing.
```
