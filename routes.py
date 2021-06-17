from app import app
from flask import redirect, render_template, request, session, abort
import users, contents


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
    exercises = ''

    if not session['admin']:

        exercises = contents.usersExercises(username)

    else:

        exercises = contents.allExercises()

    return render_template("index.html", exercises=exercises, username=username)


@app.route("/exercise", methods=["POST"])
def addExcercise():

    if session['csrf_token'] != request.form['csrf_token']:

        abort(403)

    description = request.form["exercise"]
    username = session['username']

    if contents.newExercise(description, username):

        return redirect("/")

    return redirect("/error")

@app.route("/exercise/<int:id>")
def exercise(id):

    print(id)

    if not 'username' in session:

        return redirect('/')

    exercise = contents.exercise(id)
    description = exercise[0]
    user = exercise[1]
    comments = contents.comments(id)

    if not (exercise == None):

        if (session['username'] == user or session['admin']):

            return render_template("exercise.html", description=description, user=user, comments=comments, id=id)

        abort(403)

    abort(404)

@app.route("/comment", methods=["POST"])
def comment():

    if session['csrf_token'] != request.form['csrf_token']:

        abort(403)

    exercise = request.form['exercise']
    username = session['username']
    content = request.form['content']

    if contents.newComment(exercise,username,content):

        return redirect('/exercise/' + exercise)

    return redirect('/error')

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
