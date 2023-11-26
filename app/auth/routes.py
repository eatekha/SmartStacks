# Import necessary modules from Flask and Flask-Login
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
# Import LoginForm from the forms module within the same package
from .forms import LoginForm
# Import the User model from the app's models module
from app.models import User
# Import the auth Blueprint
from . import auth

# Define a route for logging in, supporting both GET and POST methods
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the current user is already authenticated
    if current_user:
        # If so, redirect them to the home page
        return redirect(url_for('main.home'))

    # Create an instance of LoginForm
    form = LoginForm()

    # Check if the form is submitted and valid
    if form.validate_on_submit():
        # Retrieve the user by username
        user = User.get_user(form.username.data)

        # Check if the user exists and the password is correct
       # if user and user.check_password(form.password.data):
        if authenicate(form.username.data, form.password.data):
                # Log the user in
                login_user(user)
                # For debugging: print the username and password
                print(form.username.data, form.password.data)
                # Redirect to the home page after successful login
                return redirect(url_for('main.home'))

            # If login details are incorrect, show a flash message
        flash('Invalid username or password')

    # Render the login template with the form if GET request or form validation fails
    return render_template('login.html', form=form)

# Define a route for logging out
@auth.route('/logout')
# Ensure that only logged-in users can access this route
@login_required
def logout():
    # Log the user out
    logout_user()
    # Redirect to the home page after logout
    return redirect(url_for('main.home'))

def authenicate(username, password):
     return True