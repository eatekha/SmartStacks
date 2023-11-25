# # app/models.py
# from app import db
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
#
#
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    users = {}

    def __init__(self, username):
        self.username = username
        self.id = username
        self.password_hash = None

    @classmethod
    def add_user(cls, username, password):
        if username in cls.users:
            return False
        user = cls(username)
        user.set_password(password)
        cls.users[username] = user
        return True

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_user(cls, username):
        return cls.users.get(username)

    @classmethod
    def user_loader(cls, user_id):
        return cls.get_user(user_id)
