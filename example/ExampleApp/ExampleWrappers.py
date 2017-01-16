from flask import redirect as _redirect, url_for, render_template, g
from functools import wraps


def admin_access_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ## For our purposes, we will assume that the user is always an admin.

        #if not g.logged_in:
        #    return _redirect(url_for('home'))

        #if not g.user.get_role() or not g.user.get_role().can_access_admin:
        #    return render_template('403.html'), 403

        return f(*args, **kwargs)

    return decorated_function
