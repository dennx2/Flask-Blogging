from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from .. import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    date_created = db.Column(db.DateTime, default = datetime.now())
    posts = db.relationship("Post", backref="user", passive_deletes=True)