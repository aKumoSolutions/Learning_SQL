# Alter Table

## **Add and remove primary key**
---
### Add Primary Key to a table
```sql
ALTER TABLE <tablename>
ADD PRIMARY KEY (columnname);
```

### Remove Primary key from a table

```sql
ALTER TABLE <tablename>
DROP PRIMARY KEY;
```
---
## **Add and remove foreign key**
### Add Foreign Key to a table
```sql
ALTER TABLE <tablename>
ADD CONSTRAINT <constaintname>
FOREIGN KEY (<columnname>) REFERENCES <tablename>(<columnname>);
```

### Drop Foreign Key to a table
```sql
ALTER TABLE <tablename>
FOREIGN KEY (<columnname>) REFERENCES <tablename>(<columnname>);
```

---

## **Add and remove unique constraint**
By adding a unique constraint, database will not write same data to the column. 

### Add unique constraint to a column
```sql
ALTER TABLE <tablename>
ADD CONSTRAINT <constraintname> UNIQUE (<columnname>);
```

### Remove unique constraint from a column
```sql
ALTER TABLE <tablename>
DROP INDEX <constraintname>;
```


## **Change Column Name**

```sql
ALTER TABLE <tablename> CHANGE `old_column_name` `new_column_name` <data type>;
```

## **Change Column Data Type**

```sql
ALTER TABLE <tablename> MODIFY <columnname> <datatype>;
```
