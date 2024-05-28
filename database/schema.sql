 CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL
);

CREATE TABLE portfolios (
    portfolio_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    title VARCHAR(120),
    description TEXT
);

CREATE TABLE skills (
    skill_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    skill_name VARCHAR(64)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    project_name VARCHAR(120),
    project_description TEXT
);
