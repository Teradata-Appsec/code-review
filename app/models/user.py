from app import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(200))

    def __repr__(self):
        return self.username


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
