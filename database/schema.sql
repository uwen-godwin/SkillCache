CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL
);

CREATE TABLE portfolio (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user(id),
    title VARCHAR(120) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE skill (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user(id),
    skill_name VARCHAR(80) NOT NULL
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user(id),
    project_name VARCHAR(120) NOT NULL,
    project_description TEXT NOT NULL
);
