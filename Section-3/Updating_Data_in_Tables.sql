USE coffee_store;

SELECT * FROM products

-- Updating just one column of the table
UPDATE products
SET coffee_origin = 'Sri Lanka'
WHERE id = 7;

SET SQL_SAFE_UPDATES=0;

-- Updating 2 column of the table
UPDATE products
SET price = 3.25, coffee_origin = 'Ethiopia'
WHERE name = 'Americano';

-- Updating columns that have same values
UPDATE products
SET coffee_origin = 'Colombia'
WHERE coffee_origin = 'Brazil';
