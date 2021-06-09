from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def create(username, password):

	password_hash = generate_password_hash(password)
	try:

		sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
		db.session.execute(sql, {"username":username,"password":password_hash})
		db.session.commit()

	except:

		return False

	return True

def login(username, password):

	try:
		sql = "SELECT password FROM users WHERE username=:username"
		user = db.session.execute(sql, {"username":username}).fetchone()

		if not (user == None):


			if check_password_hash(user[0], password):

				return True

		return False

	except:

		return False

