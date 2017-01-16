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
