-- CREATE DATABASE test;
USE test;

-- Creating a test database

CREATE TABLE addresses (
    id INT NOT NULL PRIMARY KEY,
    house_number INT,
    city VARCHAR(20),
    poscode VARCHAR(7)
);

CREATE TABLE people (
    id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    address_id INT NOT NULL
    -- FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE pets (
    id INT,
    name VARCHAR(20),
    species VARCHAR(20),
    owner_id INT
    -- FOREIGN KEY (owner_id) REFERENCES people(id)
);