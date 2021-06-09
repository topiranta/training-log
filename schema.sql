CREATE TABLE users (
    username TEXT UNIQUE PRIMARY KEY,
    password TEXT
);
CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description TEXT,
    username TEXT REFERENCES users
);