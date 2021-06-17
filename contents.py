from app import app
from flask import session
from flask_sqlalchemy import SQLAlchemy
from db import db

def usersExercises(username):

    sql = "SELECT description, id, username FROM exercises WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    exercises = result.fetchall()

    return exercises

def allExercises():

    sql = "SELECT description, id, username FROM exercises"
    result = db.session.execute(sql)
    exercises = result.fetchall()

    return exercises

def newExercise(description, username):

    sql = "INSERT INTO exercises (description,username) VALUES (:description,:username)"

    try:

        db.session.execute(sql, {"description": description, "username": username})
        db.session.commit()

    except:

        return False

    return True

def exercise(id):

    sql = "SELECT description, username FROM exercises WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchone()

    return result

def comments(exerciseId):

    sql = "SELECT content, username FROM comments WHERE exercise=:exerciseId"
    comments = db.session.execute(sql, {"exerciseId": exerciseId}).fetchall()

    return comments

def newComment(exercise,username,content):

    sql = "INSERT INTO comments (exercise,username,content) VALUES (:exercise,:username,:content)"

    try:

        db.session.execute(sql, {"exercise": exercise, "username": username, "content": content})
        db.session.commit()

    except:

        return False

    return True
