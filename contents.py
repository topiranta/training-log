from app import app
from flask import session
from flask_sqlalchemy import SQLAlchemy
from db import db

def usersExercises(userid):

    sql = "SELECT exercises.description, exercises.id, users.username, exercisetypes.name, exercises.length, exercises.duration, exercises.bpm FROM exercises LEFT JOIN users ON exercises.userid = users.id LEFT JOIN exercisetypes ON exercises.exercisetype = exercisetypes.id WHERE exercises.userid=:userid"
    result = db.session.execute(sql, {"userid": userid})
    exercises = result.fetchall()

    return exercises

def allExercises():

    sql = "SELECT exercises.description, exercises.id, users.username, exercisetypes.name, exercises.length, exercises.duration, exercises.bpm FROM exercises LEFT JOIN users ON exercises.userid = users.id LEFT JOIN exercisetypes ON exercises.exercisetype = exercisetypes.id"
    result = db.session.execute(sql)
    exercises = result.fetchall()

    return exercises

def newExercise(description, userid, exercisetype, length, duration, bpm):

    sql = "INSERT INTO exercises (description,userid,exercisetype,length,duration,bpm) VALUES (:description,:userid,:exercisetype,:length,:duration,:bpm)"

    try:

        db.session.execute(sql, {"description": description, "userid": userid, "exercisetype": exercisetype, "length": length, "duration": duration, "bpm": bpm})
        db.session.commit()

    except:

        return False

    return True

def exercise(id):

    sql = "SELECT exercises.description, exercises.userid, users.username, exercisetypes.name, exercises.length, exercises.duration, exercises.bpm FROM exercises LEFT JOIN users ON exercises.userid = users.id LEFT JOIN exercisetypes ON exercises.exercisetype = exercisetypes.id WHERE exercises.id=:id"
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

def exercisetypes():

    sql = "SELECT id, name FROM exercisetypes"
    exercisetypes = db.session.execute(sql).fetchall()

    return exercisetypes
