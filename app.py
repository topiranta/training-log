from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():

#	return 'moikkamoi'

	result = db.session.execute("SELECT description FROM exercises")
	messages = result.fetchall()
	return str(messages)

@app.route("/insert")
def insert():

	try:
		db.session.execute("INSERT INTO exercises (description) VALUES ('tosikovajuoksulenkki');")
		db.session.execute("INSERT INTO exercises (description) VALUES ('tosikovapyoralenkki');")
	except:
		return 'ei nyt onnistunu'
	db.session.commit()

	return '/'
