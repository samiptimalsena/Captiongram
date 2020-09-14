from datetime import datetime
from flask import current_app
from captiongram import db, login_manager
from flask_login import UserMixin

LikedPost = db.Table('LikeComment',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key = True),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key = True)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150),nullable=False)
    last_name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    liked_posts = db.relationship('Post', secondary=LikedPost, backref=db.backref('LikedBy', lazy=True), lazy=True)
    
    def __repr__(self):
        return f"User('{self.first_name + self.last_name}', '{self.email}', '{self.first_name}')"

    def like_post(self,post):
        if not self.has_liked_post(post):
            self.liked_posts.append(post)
        
    def unlike_post(self,post):
        if self.has_liked_post(post):
            self.liked_posts.remove(post)

    def has_liked_post(self,post):
        return post in self.liked_posts


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(80), nullable=False)
    caption_image = db.Column(db.String(120), nullable=False, default='/static/img/avatar.svg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_name = db.Column(db.String(50),nullable=False)
    up_loaded = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        return f"Caption('{self.caption}')"




    

