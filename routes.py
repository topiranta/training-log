from app import app
from flask import redirect, render_template, request, session
from db import db
import users

@app.route("/")
def index():

	if not 'username' in session:

		return render_template("login.html")

	result = db.session.execute("SELECT description FROM exercises")
	exercises = result.fetchall()
	return render_template("index.html", exercises=exercises)

@app.route("/add", methods=["POST"])
def add():

	exercise = request.form["exercise"]
	sql = "INSERT INTO exercises (description) VALUES (:exercise);"
	try:
		db.session.execute(sql, {"exercise":exercise})
	except:
		return 'ei nyt onnistunu'
	db.session.commit()

	return redirect("/")

@app.route("/create-user",methods=["POST"])
def createUser():
	username = request.form["username"]
	password = request.form["password"]
	if users.createUser(username, password):
		return redirect("/")
	return render_template("error.html")