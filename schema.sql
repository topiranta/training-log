CREATE TABLE userlevels (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    userlevel INTEGER REFERENCES userlevels
);
CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description TEXT,
    userid INTEGER REFERENCES users
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    exercise INTEGER REFERENCES exercises,
    userid INTEGER REFERENCES users
);