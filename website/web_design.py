from flask import Blueprint, render_template
from flask_login import login_required, current_user

web_design = Blueprint('web_design', __name__)

"""

Add the name of the blueprint as the decorator and include a route which is the URL that will take the user to this application. 
Whatever is inside the defined function called home will run on the main webpage.

"""

@web_design.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)