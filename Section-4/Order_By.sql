USE coffee_store; 


-- Example of ascending order
SELECT * FROM products ORDER BY price ASC;


-- Example of descending order 

SELECT * FROM products ORDER BY price DESC;


-- Combining Where clause with order by

SELECT * FROM orders WHERE customer_id = 1 ORDER BY order_time ASC;