## Relational Keys
Relational keys are fundamental concepts in database management systems (DBMS). They act as unique identifiers for rows within tables and establish relationships between different tables. This document explores the main types of relational keys with examples.

Consider three tables

#### Customer Table
| customer_id | customer_name    | email                  | Times Visited  |
|-------------|------------------|------------------------|----------------|
| 1           | John Doe         | customer1@example.com  | 10             |
| 2           | Ram Bahadur Rai  | ram@example.com        | 21             |
| 3           | Hari Tamang      | hari.tamang@gmail.com  | 32             |

#### Order Table
| order_id | customer_id | order_date  | order_amount |
|----------|-------------|-------------|--------------|
| 1        | 1           | 2024-01-15  | 100.00       |
| 2        | 2           | 2024-01-16  | 150.00       |
| 3        | 1           | 2024-01-17  | 200.00       |
| 4        | 3           | 2024-01-18  | 250.00       |

#### Student Table
|student_id | roll_no | name           | email                    | batch |
|-----------|---------|----------------|--------------------------|-------|
|          1| 1       | Alice Johnson  | alice.johnson@example.com| 2023  |
|          2| 2       | Bob Smith      | bob.smith@example.com    | 2023  |
|          3| 1       | Carol Danvers  | carol.danvers@example.com| 2024  |
|          4| 2       | David Brown    | david.brown@example.com  | 2024  |


### 1. Candidate Key
- A candidate key is a minimal set of attributes that can uniquely identify a row in a table. 
- Each table can have multiple candidate keys.

**Example:**

- Candidate keys: `customer_id`, and `email`.

### 2. Super Key
- A super key is any set of attributes that can uniquely identify a row in a table. 
- A super key can be a candidate key or a superset of a candidate key.

**Example:**

In the `employees` table, examples of super keys are:
- `customer_id`
- `email`
- `customer_id, customer_name`
- `email, times_visited`

### 3. Primary Key
- A primary key is a candidate key chosen by the database designer to uniquely identify rows in a table. 
- There can be only one primary key per table, and it cannot contain NULL values.

**Example:**
- `customer_id`


### 4. Composite Key
- A composite key is a candidate key that consists of two or more attributes. These attributes together uniquely identify a row in the table.

**Example (Hypothetical):**
In the Student table, `roll_no` and `batch` uniquely identify a row in a table. 
- `roll_no, batch` 

### 5. Foreign Key
- A foreign key is an attribute in one table that references the primary key of another table. 
- A foreign key can be null also. 

**Example:**
- `customer_id` in an Order table is the foreign key since it is referencing the primary key of the customer table. 


### 6. Alternate Key: 
An alternate key is any other candidate key that wasn't chosen as the primary key. It can also uniquely identify rows in the table, but there can only be one primary key, while there can be multiple alternate keys.