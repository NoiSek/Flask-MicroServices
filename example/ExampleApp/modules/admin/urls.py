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
