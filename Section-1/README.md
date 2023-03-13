# Section 1

## **Commands for database**

**Databases**
- **SHOW DATABASES**;
- **CREATE DATABASE 'name'**; ---> Will create a database using provided name
- **USE 'database name'**; ---> Will use this database to write and store data

--- 
**Tables**
- **CREATE TABLE 'name'**; ---> Will create a table inside of the specific database. Inside we can provide values to store inside of the table.
- **ALTER TABLE 'name'** ---> Will modify the table (No semicolon in the end)
- **DROP TABLE 'name'** ---> Will delete table
- **TRUNCATE TABLE 'name'** ---> Will delete all data inside of the table, but will leave the strucure of it


```sql
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(30), 
    last_name VARCHAR(30),
    gender ENUM('M','F'),
    phone_number VARCHAR(11)
);
```

---
<br>


## **Data Types**

<br>

### **Numeric Data Types**
- INT: Whole Numbers
- FLOAT(M,D): Decimal Numbers (approximate)
- DECIMAL(M,D): Decimal numbers (precise) 

<br>

### **Non-Numeric Data Types**

- CHAR(N): Fixel length character
- VARCHAR(N): Varying lenght character
- ENUM('M', 'F'): Value from a defined list
- BOOLEAN: True or False values

<br>

### **Date and Time Types**

- DATE: Date (YYYY-MM-DD)
- DATETIME: Date and Time (YYYY-MM-DD HH-MM-SS)
- TIME: Time (HHH-MM-SS)
- YEAR: Year (YYYY)

<br>

## **Key Types**

<br>

### **Primary Key**
 - A primary key is a column, or set of columns, which are uniquely identifies a record within a table.

 - A primary key must be unique

 - A primary key cannot be NULL 

 - A table can only have one primary key

### **Foreign Key**

- A foreign key is used to link two tables together

- A foreign key is a column whose values match the values of another table primary key column

- Table with the primary key is called the reference, or parent, table and the with foreign key is called the child table.

- A table can have multiple foreign keys.

<br>




