from flask import render_template, Blueprint
from flask_login import login_required
from . import main


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/protected')
@login_required
def protected():
    return "This is a protected area"
