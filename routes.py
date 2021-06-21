from app import app
from flask import redirect, render_template, request, session, abort
import users, contents


@app.route("/")
def index():
    if not users.loggedin():

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

    exercises = ''

    if not (users.userlevel() > 1):

        exercises = contents.usersExercises(users.userid())

    else:

        exercises = contents.allExercises()

    return render_template("index.html", exercises=exercises, username=users.username())


@app.route("/exercise", methods=["POST"])
def addExcercise():

    if users.csrf() != request.form['csrf_token']:

        abort(403)

    description = request.form["exercise"]

    if contents.newExercise(description, users.userid()):

        return redirect("/")

    return redirect("/error")

@app.route("/exercise/<int:id>")
def exercise(id):

    if not users.loggedin():

        return redirect('/')

    exercise = contents.exercise(id)
    description = exercise[0]
    userid = exercise[1]
    username = exercise[2]
    comments = contents.comments(id)

    if not (exercise == None):

        if (users.userid() == userid or (users.userlevel()>1)):

            return render_template("exercise.html", description=description, user=username, comments=comments, id=id)

        abort(403)

    abort(404)

@app.route("/comment", methods=["POST"])
def comment():

    if users.csrf() != request.form['csrf_token']:

        abort(403)

    exercise = request.form['exercise']
    userid = users.userid()
    content = request.form['content']

    if contents.newComment(exercise,userid,content):

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

    users.logout()
    return redirect('/')

@app.route("/users")
def userslist():

    if not (users.loggedin() and (users.userlevel() > 1)):

        abort(403)

    allusers = users.users()
    alluserlevels = users.userlevels()

    if users.userlevel() == 2:

        return render_template("users.html", users=allusers)

    elif users.userlevel() == 3:

        return render_template("usersadmin.html", users=allusers, userlevels=alluserlevels)

@app.route("/updateuser", methods=["POST"])
def updateuser():

    if users.csrf() != request.form['csrf_token'] or not users.userlevel() > 2:

        abort(403)

    userid = request.form["userid"]
    username = request.form["username"]
    userlevel = request.form["userlevel"]

    users.updateuser(userid, username, userlevel)

    return redirect('/users')