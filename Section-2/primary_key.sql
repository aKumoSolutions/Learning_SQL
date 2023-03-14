USE test;

-- Adding Primary Key
ALTER TABLE addresses
ADD PRIMARY KEY (id);

-- Drop Primary Key
ALTER TABLE addresses
DROP PRIMARY KEY;
