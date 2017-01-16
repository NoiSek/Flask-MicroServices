from Flask_MicroServices import url
from . import views

urlpatterns = [
    url('/forum/', view_func=views.forum_home, name='forum_home'),
    url('/forum/board/<board_id>', view_func=views.forum_board),

    # We'll add our own admin page to the admin module.
    url('/admin/forum/', view_func=views.forum_admin, name='forum_admin')
]
