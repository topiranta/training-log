from app import app
from flask import redirect, render_template, request, session, abort
from db import db
import users
import secrets


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
    sql = "SELECT description, id FROM exercises"

    if not session['admin']:

        sql += "  WHERE username=:username"

    result = db.session.execute(sql, {"username" : username})
    exercises = result.fetchall()

    return render_template("index.html", exercises=exercises, username=username)


@app.route("/add", methods=["POST"])
def add():

    if session['csrf_token'] != request.form['csrf_token']:

        abort(403)

    exercise = request.form["exercise"]
    username = session['username']
    sql = "INSERT INTO exercises (description,username) VALUES (:exercise,:username);"

    try:

        db.session.execute(sql, {"exercise": exercise, "username": username})

    except:

        return render_template("error.html")

    db.session.commit()
    return redirect("/")

@app.route("/exercise/<int:id>")
def exercise(id):

    if not 'username' in session:

        return redirect('/')

    sql = "SELECT description, username FROM exercises WHERE id=:id"
    result = db.session.execute(sql, {"id":id}).fetchone()
    description = result[0]
    user = result[1]

    if not (result == None):

        if (session['username'] == user or session['admin']):

            return render_template("exercise.html", description=description, user=user)

        abort(403)

    abort(404)


@app.route("/create-user", methods=["POST"])
def createUser():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:

        return redirect("/?error=unmatching_passwords")

    if users.create(username, password1):

        return redirect("/")

    return redirect("/?error=username_not_available")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if users.login(username, password):

        return redirect("/")

    return redirect("/?error=login_failed")


@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/logout")
def logout():
    del session['username']
    return redirect('/')
