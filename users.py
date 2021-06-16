from app import app
from flask import session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import secrets

def create(username, password):

	password_hash = generate_password_hash(password)
	try:

		sql = "INSERT INTO users (username,password,admin) VALUES (:username,:password, FALSE)"
		db.session.execute(sql, {"username":username,"password":password_hash})
		db.session.commit()

	except:

		return False

	session['username'] = username
	session['csrf_token'] = secrets.token_hex(16)
	return True

def login(username, password):

	try:
		sql = "SELECT password, admin FROM users WHERE username=:username"
		user = db.session.execute(sql, {"username":username}).fetchone()

		if not (user == None):


			if check_password_hash(user[0], password):

				session['username'] = username
				session['csrf_token'] = secrets.token_hex(16)
				session['admin'] = user[1]

				return True

		return False

	except:

		return False

