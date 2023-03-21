USE coffee_store;

SELECT name, price FROM products WHERE coffee_origin IN ('Colombia', 'Indonesia')
ORDER BY name ASC;


SELECT * FROM orders WHERE order_time BETWEEN '2017-02-01' AND '2017-02-28' 
AND customer_id IN (2,4,6,8) ORDER BY order_time ASC;


SELECT first_name, phone_number, last_name FROM customers 
WHERE last_name LIKE '%ar%';