from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from app.models import User
from . import auth


@auth.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            print(form.username.data, form.password.data)
            return redirect(url_for('main.home'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)


#
# @auth.route('/login', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.get_user(form.username.data)
#         if user:
#             flash('Username already exists')
#         else:
#             user = User(username=form.username.data)
#             user.set_password(form.password.data)
#             user.save()
#             login_user(user)
#             return redirect(url_for('main.home'))
#     return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
