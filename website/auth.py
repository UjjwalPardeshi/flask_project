from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>fuckyou</p>"

@auth.route('/signup')
def Signup():
    return "<p>signup</p>"