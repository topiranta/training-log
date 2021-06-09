from app import app
from flask import redirect, render_template, request, session
from db import db
import users


@app.route("/")
def index():
    if not 'username' in session:

        error = request.args.get('error')
        loginError = ''
        createError = ''

        if error == 'login_failed':

            loginError = 'Kirjautuminen epäonnistui: käyttäjä tai salasana on väärä'

        elif error == 'unmatching_passwords':

            createError = 'Syöttämäsi salasanat eivät täsmää'

        elif error == 'username_not_available':

            createError = 'Käyttäjätunnus ei ole vapaana'

        return render_template("login.html", login_error=loginError, create_error=createError)

    username = session['username']
    result = db.session.execute("SELECT description FROM exercises")
    exercises = result.fetchall()

    return render_template("index.html", exercises=exercises, username=username)


@app.route("/add", methods=["POST"])
def add():
    exercise = request.form["exercise"]
    sql = "INSERT INTO exercises (description) VALUES (:exercise);"

    try:

        db.session.execute(sql, {"exercise": exercise})

    except:

        return 'ei nyt onnistunu'

    db.session.commit()
    return redirect("/")


@app.route("/create-user", methods=["POST"])
def createUser():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:

        return redirect("/?error=unmatching_passwords")

    if users.create(username, password1):
        session['username'] = username
        return redirect("/")

    return redirect("/?error=username_not_available")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if users.login(username, password):
        session['username'] = username
        return redirect("/")

    return redirect("/?error=login_failed")


@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/logout")
def logout():
    del session['username']
    return redirect('/')
