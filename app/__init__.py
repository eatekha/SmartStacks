from flask import Flask
from flask_login import LoginManager
from app.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.user_loader(user_id)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
