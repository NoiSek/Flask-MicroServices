from Flask_MicroServices import url
from . import views

urlpatterns = [
    url('/', view_func=views.home, name='home')
]
