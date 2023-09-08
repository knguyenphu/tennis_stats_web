from flask import Blueprint, render_template
from flask_login import current_user

landing = Blueprint('test', __name__)

@landing.route('/')
def landing_page():
    return render_template("landing.html", user=current_user)