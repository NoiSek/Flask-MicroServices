from flask import render_template
from ExampleApp.ExampleWrappers import admin_access_required

@admin_access_required
def forum_admin():
    return render_template('admin/forum.html')


def forum_home():
    return render_template('main.html')


def forum_board(board_id):
    return render_template("board.html", board_id=board_id)
