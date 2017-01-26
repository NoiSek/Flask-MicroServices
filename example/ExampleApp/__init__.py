from flask_microservices import MicroServicesApp

app = MicroServicesApp(__name__)

enabled_modules = [
    'admin',
    'forum',
    'home'
]

# By default, this will assume your modules directory is "./modules"
# if a second argument is not provided.
app.register_urls(enabled_modules)

app.config['DEBUG'] = True
#app.config['EXPLAIN_TEMPLATE_LOADING'] = True
