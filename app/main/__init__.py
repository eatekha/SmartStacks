import os
from flask import Blueprint

template_dir = os.path.abspath('templates')


main = Blueprint('main', __name__, template_folder=template_dir)
