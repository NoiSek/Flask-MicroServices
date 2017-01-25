from flask import render_template
from ExampleApp.ExampleWrappers import admin_access_required

@admin_access_required
def admin_panel():
    return render_template('main.html')
