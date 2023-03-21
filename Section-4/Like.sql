USE coffee_store; 

/*

%  -- any number of character 
_  -- just one character 

*/


SELECT * FROM customers WHERE last_name LIKE 'W%';

SELECT * FROM customers WHERE last_name LIKE '%o%';

SELECT * FROM customers WHERE first_name LIKE '_o_';