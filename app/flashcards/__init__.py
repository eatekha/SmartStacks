from flask import Blueprint

flashcards = Blueprint('flashcards', __name__, template_folder='templates')

from . import routes
