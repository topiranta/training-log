from app import app
from flask import session
from flask_sqlalchemy import SQLAlchemy
from db import db

def usersExercises(userid):

    sql = "SELECT exercises.description, exercises.id, users.username FROM exercises LEFT JOIN users ON exercises.userid = users.id WHERE exercises.userid=:userid"
    result = db.session.execute(sql, {"userid": userid})
    exercises = result.fetchall()

    return exercises

def allExercises():

    sql = "SELECT exercises.description, exercises.id, users.username FROM exercises LEFT JOIN users ON exercises.userid = users.id"
    result = db.session.execute(sql)
    exercises = result.fetchall()

    return exercises

def newExercise(description, userid):

    sql = "INSERT INTO exercises (description,userid) VALUES (:description,:userid)"

    try:

        db.session.execute(sql, {"description": description, "userid": userid})
        db.session.commit()

    except:

        return False

    return True

def exercise(id):

    sql = "SELECT exercises.description, exercises.userid, users.username FROM exercises LEFT JOIN users ON exercises.userid = users.id WHERE exercises.id=:id"
    result = db.session.execute(sql, {"id": id}).fetchone()

    return result

def comments(exerciseId):

    sql = "SELECT comments.content, users.username FROM comments LEFT JOIN users ON comments.userid = users.id WHERE exercise=:exerciseId"
    comments = db.session.execute(sql, {"exerciseId": exerciseId}).fetchall()

    return comments

def newComment(exercise,userid,content):

    sql = "INSERT INTO comments (exercise,userid,content) VALUES (:exercise,:userid,:content)"

    try:

        db.session.execute(sql, {"exercise": exercise, "userid": userid, "content": content})
        db.session.commit()

    except:

        return False

    return True
