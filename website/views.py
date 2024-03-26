from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('signup')
def Signup():
    return render_template("sign_up.html")


# @auth.route('/login')
# def login():
#     return "<p>login</p>"

# @auth.route('/logout')
# def logout():
#     return "<p>fuckyou</p>"

# @auth.route('/signup')
# def Signup():
#     return "<p>signup</p>"