CREATE TABLE users (
    username TEXT UNIQUE PRIMARY KEY,
    password TEXT,
    admin BOOLEAN
);
CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description TEXT,
    username TEXT REFERENCES users
);