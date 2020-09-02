from datetime import datetime
from flask import current_app
from captiongram import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150),nullable=False)
    last_name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    
    
    def __repr__(self):
        return f"User('{self.first_name + self.last_name}', '{self.email}', '{self.first_name}')"


class Captions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(80), nullable=False)
    caption_image = db.Column(db.String(120), nullable=False, default='/static/img/avatar.svg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_name = db.Column(db.String(50),nullable=False)
    up_loaded = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        return f"Caption('{self.caption}')"

