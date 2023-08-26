from flask import Blueprint, render_template, request, flash

login_auth = Blueprint('login_auth', __name__)

"""

The function named login, logout and sign up is used to direct the user to the following URL or route specified by the 
python decorator.  

Now we need to ensure that login and signup is able to accept POST request.

After entering information inside the form and clicking on Submit, it should print the output of the information. 

Entering conditional statmements to ensure the user meets the requirements when creating their account.

Flash library is used to flash an error message when the user doesn't meet the sign up/login requirements

"""

@login_auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing")

@login_auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@login_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstname) < 2:
            flash('The firstname must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('The password must match', category='error')
        elif len(password1) < 7:
            flash('The password has to be greater than 6 characters', category='error')
        else:
            # Add user to database
            flash('Account created!', category='success')

    return render_template("signup.html")


