from app import db


class Todo(db.Model):
    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text
        self.complete = False

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return self.text
