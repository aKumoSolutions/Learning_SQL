USE test;
-- Creating test table
CREATE TABLE test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    age INT,
    gender ENUM('M','F')
)

SELECT * FROM test;
-- Inserting data into table
INSERT INTO test (name, age, gender)
VALUES ('Emma', 21, 'F'),('John', 30, 'M'),('Thomas', 27, 'M'),('Chris', 44, 'M'), ('Sally', 23, 'F'),('Frank', 55, 'M');

-- Deleting John from table
DELETE FROM test
WHERE name = 'John';

-- Deleting all people that have gender = 'F'
DELETE FROM test
WHERE gender = 'F';

-- Deleting every single row in the table
DELETE FROM test;