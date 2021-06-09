from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def createUser(username, password):

	password_hash = generate_password_hash(password)
	try:
		sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
		db.session.execute(sql, {"username":username,"password":password_hash})
		db.session.commit()
	except:

		return False

	return True