from flask import render_template
from flask_login import login_required
from . import main


@main.route('/home')
@login_required
def home():
    cards_data = [
        {
            'title': '',
            'image': ''},
    ]
    return render_template('home.html', cards=cards_data)
