CREATE TABLE userlevels (
    id SERIAL PRIMARY KEY,
    level INTEGER,
    CHECK (level > 0),
    CHECK (level < 10),
    name VARCHAR (16) UNIQUE,
    CHECK (length(name) > 1)
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR (16) UNIQUE,
    CHECK (length(username) > 0),
    password VARCHAR (200),
    CHECK (length(password) > 1),
    userlevel INTEGER REFERENCES userlevels
);
CREATE TABLE exercisetypes (
    id SERIAL PRIMARY KEY,
    name VARCHAR (16),
    CHECK (length(name) > 1)
);
CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description VARCHAR (20),
    CHECK (length(description) > 0),
    exercisetype INTEGER REFERENCES exercisetypes,
    length INTEGER,
    CHECK (length > 0),
    CHECK (length <= 1000),
    duration INTEGER,
    CHECK (duration > 0),
    CHECK (duration <= 3000),
    bpm INTEGER,
    CHECK (bpm >= 40),
    CHECK (bpm <= 250),
    userid INTEGER REFERENCES users
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content VARCHAR (64),
    CHECK (length(content) > 0),
    exercise INTEGER REFERENCES exercises,
    userid INTEGER REFERENCES users
);
