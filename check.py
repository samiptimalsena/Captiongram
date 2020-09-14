from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sakal;sjdal;sdjakl;d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

LikeComment = db.Table('LikeComment',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key = True),
                db.Column('caption_id', db.Integer, db.ForeignKey('captions.id'), primary_key = True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    captions=db.relationship('Captions', secondary = LikeComment, backref = db.backref('LikerCommenter', lazy = True), lazy = True)
    
    def __repr__(self):
        return f"User({self.id},{self.name})"

class Captions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Caption('{self.id},{self.caption}')"


    
