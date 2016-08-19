# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import datetime

blog = Flask(__name__)
blog.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/blog'
db = SQLAlchemy(blog)

class Account(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(256), unique=True)
    userpass = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True)
    state = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    level = db.Column(db.Integer)

    def __init__(self,username,userpass,email):
        self.username = username
        self.userpass = userpass
        self.email = email
        self.state = config.state.active
        self.level = config.level.common
        self.create_time = datetime.datetime.now()
        self.modify_time = datetime.datetime.now()

    def __repr__(self):
        return '<account %r>' % self.username