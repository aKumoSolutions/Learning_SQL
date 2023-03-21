USE coffee_store;

SELECT first_name, phone_number FROM customers WHERE gender = 'F' AND last_name = 'Bluth';


SELECT name FROM products WHERE price > 3.00 OR coffee_origin = 'Sri Lanka';

SELECT * FROM customers WHERE gender = 'M' AND phone_number IS NULL;