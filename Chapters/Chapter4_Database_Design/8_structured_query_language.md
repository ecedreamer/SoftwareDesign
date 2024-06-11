## Structured Query Language (SQL)
Structured Query Language (SQL) is a standardized language designed for managing data stored in relational databases. These databases organize information in tables with rows and columns, allowing for connections between different data points.
It can be used across different DBMSs such as SQLITE, MySQL, PostgreSQL, SQL Server, and Oracle etc. 


## General Database Command using SQL

### 1. Create a new database
if you are using SQLite database, create a database manually using sqlite cli or DBeaver or other tools.
```sql
-- creating a new database
CREATE DATABASE mydatabase;


--- deleting a database
DROP DATABASE mydatabase;

```

### 2. Creating Tables

Syntax: 
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    column3 datatype constraints,
    ...
);
```

**Example:**
For SQLite database
```sql
CREATE TABLE batch (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_name TEXT NOT NULL
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT,
    batch_id INTEGER NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batch(id)
);
```

For MySQL database

```sql
CREATE TABLE batch (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    batch_name TEXT NOT NULL,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT,
    batch_id INTEGER NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batch(id)
);
```

### 3. Inserting Data
**Syntax:**
```sql
INSERT INTO table(col1, col2, col3) 
    VALUES ("col1 value1", "col2 value1", "col3 value1"),
           ("col1 value2", "col2 value2", "col3 value2");
```

**Example:**
```sql
INSERT INTO batch (batch_name, start_date, end_date)
VALUES ('AI-36', '2024-01-01', '2027-01-01'),
       ('CS-36', '2024-01-01', '2027-01-01');


-- Inserting 3 students for batch 'AI-36'
INSERT INTO student (name, email, address, batch_id)
VALUES ('Student 1', 'student1@example.com', 'Address 1', 1),
       ('Student 2', 'student2@example.com', 'Address 2', 1),
       ('Student 3', 'student3@example.com', 'Address 3', 1);

-- Inserting 2 students for batch 'CS-36'
INSERT INTO student (name, email, address, batch_id)
VALUES ('Student 4', 'student4@example.com', 'Address 4', 2),
       ('Student 5', 'student5@example.com', 'Address 5', 2);

-- Inserting other 2 students
INSERT INTO student (name, email, address, batch_id)
VALUES ('Dipak Niroula', 'dipak@example.com', 'Satdobato', 1),
       ('Rupak Kafle', 'rupak@example.com', 'Bhaktapur', 2);
```

### 4. Retrieving Data from table
**Syntax:**
```sql
SELECT columns from table_name;

SELECT columns from table_name where conditions;
```

**Examples:**
```sql
SELECT * FROM student;

SELECT id, email, batch_id from student;

SELECT * FROM student WHERE name="Student 4";

SELECT * FROM student WHERE name LIKE "%pak%";

```