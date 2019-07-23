"""
Leon Santen

This is a package for database in webapp_run.py
"""
from datetime import datetime
from webapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pair_posts = db.relationship('Pair', backref='author', lazy=True) #this is a releationship not a column -- backreference to Pair. You can find out author of a pair post by using pair.author #lazy=True --> sqlalchemy will load data directly when used
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"User('{self.username}', '{self.id}')"

class Pair(db.Model): #data table for transition pair
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    secondname = db.Column(db.String(30), nullable=False)
    firstartist = db.Column(db.String(30), nullable=False)
    secondartist = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Pair('{self.firstname}', '{self.secondname}', '{self.date_posted}' )"