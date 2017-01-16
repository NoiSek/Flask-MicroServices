# `Flask-MicroServices`

Isolated, self contained apps for Flask. A form of the micro-service concept, with Django style routes and app level template resolution.

Alpha.

### Usage

`project_root/appname/__init__.py`

```python
from Flask_MicroServices import MicroServicesApp

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
from Flask_MicroServices import Router
from . import urls

MODULE_NAME = 'admin'
IMPORT_NAME = __name__

# These blueprints are what is collected when you run app.register_urls()
blueprint = Router.create_blueprint(MODULE_NAME, IMPORT_NAME)
blueprint.register_urls(urls.urlpatterns)
```

`project_root/appname/admin/urls.py`

```python
from Flask_MicroServices import url
from . import views

urlpatterns = [
    url('/admin/', view_func=views.admin_panel, name='admin_home'),

    ## Example URLs:

    ### Minimal:
    # url('/admin/simple/', view_func=views.admin_simple)

    ### Advanced
    # url('/admin/roles/add/', view_func=views.admin_panel_roles_add, name='admin_role_add', methods=['GET', 'POST']),
    # url('/admin/roles/edit/', view_func=views.admin_panel_roles_edit, name='admin_role_edit', methods=['GET', 'POST']),
]
```

`project_root/appname/admin/views.py`

```python
from flask import render_template
from ExampleApp.ExampleWrappers import admin_access_required

@admin_access_required
def admin_panel():
    return render_template('admin/main.html')
```

`project_root/appname/admin/templates/main.html`

```html
<html>
  <h1> Holy cow! </h1>
  <p> If the router was unable to find this file, then it would try your root level templates folder at `project_root/appname/templates/main.html` before failing.</p>
</html>
```
