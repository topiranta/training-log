from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

try:
	db.session.execute("CREATE TABLE exercises (id SERIAL PRIMARY KEY, description TEXT);")
except:
	print('could not create table probably because it exists already')

db.session.commit()

try:
	db.session.execute("INSERT INTO exercises (description) VALUES ('kovajuoksulenkki');")
	db.session.execute("INSERT INTO exercises (description) VALUES ('kovapyoralenkki');")
except:
	print('ei nyt onnistunu')
db.session.commit()

@app.route("/")
def index():
	
	result = db.session.execute("SELECT description FROM exercises")
	messages = result.fetchall()
	return str(messages)
