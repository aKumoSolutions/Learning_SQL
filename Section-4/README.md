# **Selecting From the Table**

## **Select Statement** 

```sql
USE coffee_store;
SELECT * FROM customers;
SELECT last_name FROM customers;
SELECT last_name, phone_number FROM customers;
```


## **Inequality Signs**

```
>   --   greater than  
>=  --   greater that or equal
<   --   less than
<=  --   less than or equal
```

**Example**

```sql
SELECT * FROM products WHERE price < | <= | > | >= 3.00;
```

## **Null Values**

```sql
-- Null
SELECT * FROM customers WHERE phone_number IS NULL;

-- Not Null
SELECT * FROM customers WHERE phone_number IS NOT NULL;
```


## **In, Not In**

```sql
-- Example of how to use IN
SELECT * FROM customers WHERE last_name IN ('Taylor', 'Bluth', 'Armstrong');

-- Example of how to use NOT IN

SELECT * FROM customers WHERE first_name NOT IN ('Katie', 'John', 'George');
```
