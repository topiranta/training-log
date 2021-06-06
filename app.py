from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():


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
