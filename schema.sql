CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    description TEXT
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);