from flask import Blueprint, render_template
from flask_login import current_user

stats = Blueprint('test', __name__)

@stats.route('/stats')
def stats_page():
    return render_template("stats.html", user=current_user)