from flask import Blueprint, render_template

web_design = Blueprint('web_design', __name__)

"""

Add the name of the blueprint as the decorator and include a route which is the URL that will take the user to this application. 
Whatever is inside the defined function called home will run on the main webpage.

"""

@web_design.route('/')

def home():
    return render_template("home.html")