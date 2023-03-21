USE coffee_store;


-- Example of how to use IN
SELECT * FROM customers WHERE last_name IN ('Taylor', 'Bluth', 'Armstrong');

-- Example of how to use NOT IN

SELECT * FROM customers WHERE first_name NOT IN ('Katie', 'John', 'George');