from postr import db, app
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(100), unique=False, nullable=False)
	user_posts = db.relationship('Post', backref='user', lazy='dynamic')

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.set_password(password)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<User %r>' % self.username

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	board_id = db.Column(db.String, unique=True, nullable=False)
	title = db.Column(db.String(120), unique=False, nullable=True)
	timestamp = db.Column(db.DateTime, nullable=False)
	body = db.Column(db.Text, unique=False, nullable=False)
	img = db.Column(db.String(200), unique=True, nullable=True)
	posts_user = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self):
		self.board_id = board_id
		self.title = title
		self.timestamp = timestamp
		self.body = body
		self.img = img
		self.user = user

	def __repr__(self):
		return '<Post %r>' % self.id