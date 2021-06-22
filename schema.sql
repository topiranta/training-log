CREATE TABLE userlevels (
    id SERIAL PRIMARY KEY,
    level INTEGER,
    name TEXT UNIQUE
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    userlevel INTEGER REFERENCES userlevels
);
CREATE TABLE exercisetypes (
    id SERIAL PRIMARY KEY,
    name TEXT
);
CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description TEXT,
    exercisetype INTEGER REFERENCES exercisetypes,
    length INTEGER,
    duration INTEGER,
    bpm INTEGER,
    userid INTEGER REFERENCES users
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    exercise INTEGER REFERENCES exercises,
    userid INTEGER REFERENCES users
);
