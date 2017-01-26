[![Build Status](https://travis-ci.org/NoiSek/Flask-MicroServices.svg?branch=master)](https://travis-ci.org/NoiSek/Flask-MicroServices)
[![Coverage Status](https://coveralls.io/repos/github/NoiSek/Flask-MicroServices/badge.svg?branch=master)](https://coveralls.io/github/NoiSek/Flask-MicroServices?branch=master)

# `Flask-MicroServices`

Isolated, self contained apps for Flask. A form of the microservices concept, with Django style routes and app level template and static file resolution.

Beta.

### Usage

`project_root/appname/__init__.py`

```python
from flask_microservices import MicroServicesApp

app = MicroServicesApp(__name__)

enabled_modules = [
    'admin',
    'forum',
    'home',
    'settings'
]

# By default, this will assume your modules directory is "./modules" if a second argument is not provided.
app.register_urls(enabled_modules)
app.run()
```

`project_root/appname/admin/__init__.py`

```python
from flask_microservices import Router
from . import urls

MODULE_NAME = 'admin'
IMPORT_NAME = __name__

# These blueprints are what is collected when you run app.register_urls()
blueprint = Router.create_blueprint(MODULE_NAME, IMPORT_NAME)
blueprint.register_urls(urls.urlpatterns)
```

`project_root/appname/admin/urls.py`

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

`project_root/appname/admin/views.py`

```python
from flask import render_template
from ExampleApp.ExampleWrappers import admin_access_required

@admin_access_required
def admin_panel():
    return render_template('main.html')
```

`project_root/appname/admin/templates/admin/main.html`

```html
<html>
  <h1> Holy cow! </h1>
  <p> If the router was unable to find this file, then it would try your root level templates folder at `project_root/appname/templates/admin/main.html` before failing.</p>
</html>
```
