from flask import Blueprint, render_template
from flask_login import current_user

plan = Blueprint('test', __name__)

@plan.route('/plan')
def plan_page():
    return render_template("plan.html", user=current_user)