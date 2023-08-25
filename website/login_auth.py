from flask import Blueprint, render_template

login_auth = Blueprint('login_auth', __name__)

"""

The function named login, logout and sign up is used to direct the user to the following URL or route specified by the 
python decorator.  

"""

@login_auth.route('/login')
def login():
    return render_template("login.html", text="Testing")

@login_auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@login_auth.route('/signup')
def signup():
    return render_template("signup.html")


