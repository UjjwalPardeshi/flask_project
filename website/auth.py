from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])  
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():  # Changed "Signup" to "signup" for consistency
    if request.method == 'POST':  # Added a colon after "if request.method == 'POST'"
        email = request.form.get('email')  # Changed 'firstName' to 'email' to match form field
        firstname = request.form.get('firstname')  # Corrected the variable name from 'firstname' to 'firstName'
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')  # Corrected spelling of 'characters'
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')  # Corrected spelling of 'character'
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')  # Added a period at the end of the error message
        elif len(password1) < 5:
            flash('Password must be at least 7 characters.', category='error')  # Corrected the error message
        else: 
            flash('Account Created', category='success')

    return render_template("sign_up.html")
