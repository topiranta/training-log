from app import app
from flask import session, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import secrets

def create(username, password):

	password_hash = generate_password_hash(password)
	try:

		sql = "INSERT INTO users (username,password,userlevel) VALUES (:username,:password, 1) RETURNING id"
		result = db.session.execute(sql, {"username":username,"password":password_hash})
		userid = result.fetchone()[0]
		db.session.commit()

		session['userid'] = userid
		session['username'] = username
		session['csrf_token'] = secrets.token_hex(16)
		session['userlevel'] = 1

	except:

		print('pieleen män')
		return False

	return True

def login(username, password):

	try:

		sql = "SELECT users.password, userlevels.level, users.id FROM users LEFT JOIN userlevels ON users.userlevel = userlevels.id WHERE username=:username"
		user = db.session.execute(sql, {"username":username}).fetchone()

		if not (user == None):


			if check_password_hash(user[0], password):

				session['username'] = username
				session['csrf_token'] = secrets.token_hex(16)
				session['userlevel'] = user[1]
				session['userid'] = user[2]

				return True

		return False

	except:

		return False

def logout():

	session.clear()

def loggedin():

	if not 'username' in session:

		return False

	return True

def username():

	if not loggedin():

		return None

	return session['username']

def userid():

	if not loggedin():

		return None

	return session['userid']

def userlevel():

	if not loggedin():

		return None

	return session['userlevel']

def csrf():

	if not loggedin():

		return None

	return session['csrf_token']

def users():

	sql = "SELECT username, userlevels.name, users.id FROM users LEFT JOIN userlevels ON users.userlevel = userlevels.id"
	result = db.session.execute(sql)
	users = result.fetchall()
	return users

def userlevels():

	sql = "SELECT level, name FROM userlevels"
	result = db.session.execute(sql)
	userlevels = result.fetchall()
	return userlevels

def updateuser(userid, username, userlevel):

	sql = "UPDATE users SET (username, userlevel) = (:username, :userlevel) WHERE id=:userid"
	db.session.execute(sql, {"userid":userid,"username":username,"userlevel":userlevel})
	db.session.commit()
