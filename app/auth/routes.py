# Import necessary modules from Flask and Flask-Login
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
# Import LoginForm from the forms module within the same package
from .forms import LoginForm
# Import the User model from the app's models module
from app.models import User
# Import the auth Blueprint
from . import auth

from flask import request, redirect, url_for
from flask_login import login_user
import urllib.parse as urlparse


@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    # Assume form is a LoginForm instance
    if form.validate_on_submit():
        user = User.check_user(form.username.data)
        login_user(User.get_user(user))
        return redirect('/home')
    return render_template('login.html', form=form)

# Define a route for logging out
@auth.route('/logout')
# Ensure that only logged-in users can access this route
def logout():
    # Redirect to the home page after logout
    return redirect('/home')
