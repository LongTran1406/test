CREATE DATABASE my_database;
USE my_database;

SHOW DATABASES;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

INSERT INTO users (name, email, password) 
VALUES 
	
    ('John Doe', 'john.doe@example.com', 'password123'),
    ('Jane Smith', 'jane.smith@example.com', 'mypassword456'),
    ('Alice Johnson', 'alice.johnson@example.com', 'alicepass789');

SELECT * FROM users;
SELECT * FROM users WHERE users.email = 'tranthelong1406@gmail';

DROP TABLE users

DROP DATABASE my_database;
