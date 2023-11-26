from flask import render_template
from flask_login import login_required
from . import flashcards


@flashcards.route('/flashcards')
def scroller():
    # Your flashcard screen logic here
    return render_template('scroller.html')


@flashcards.route('/protected')
@login_required
def protected():
    return "This is a protected area"
