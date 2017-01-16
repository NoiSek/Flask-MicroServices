from Flask_MicroServices import Router
from . import urls

MODULE_NAME = 'forum'
IMPORT_NAME = __name__

# These blueprints are what is collected when you run app.register_urls()
blueprint = Router.create_blueprint(MODULE_NAME, IMPORT_NAME)
blueprint.register_urls(urls.urlpatterns)
