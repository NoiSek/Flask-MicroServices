from flask_microservices import url
from . import views

urlpatterns = [
    url('/', view_func=views.home, name='home')
]
