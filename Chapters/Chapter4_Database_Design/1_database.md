## Database
A database is a collection of interrelated data which helps in the efficient retrieval, insertion, and deletion of data from the database and organizes the data in the form of tables, views, schemas, reports, etc. For Example, a university database organizes the data about students, faculty, admin staff, etc. which helps in the efficient retrieval, insertion, and deletion of data from it.

## A Database Management System (DBMS) 
DBMS is a software system that is designed to manage and organize data in a structured manner. It allows users to create, modify, and query a database, as well as manage the security and access controls for that database.

DBMS provides an environment to store and retrieve the data in coinvent and efficient manner.

### Key Features of DBMS

**Data modeling:** A DBMS provides tools for creating and modifying data models, which define the structure and relationships of the data in a database.

**Data storage and retrieval:** A DBMS is responsible for storing and retrieving data from the database, and can provide various methods for searching and querying the data.

**Concurrency control:** A DBMS provides mechanisms for controlling concurrent access to the database, to ensure that multiple users can access the data without conflicting with each other.

**Data integrity and security:** A DBMS provides tools for enforcing data integrity and security constraints, such as constraints on the values of data and access controls that restrict who can access the data.

**Backup and recovery:** A DBMS provides mechanisms for backing up and recovering the data in the event of a system failure.

**DBMS can be classified into two types:** Relational Database Management System (RDBMS) and Non-Relational Database Management System (NoSQL or Non-SQL)

**RDBMS:** Data is organized in the form of tables and each table has a set of rows and columns. The data are related to each other through primary and foreign keys. Example: MySQL, PostgreSQL, Sqlite, MariaDB, OracleDB etc. 

**NoSQL:** Data is organized in the form of key-value pairs, documents, graphs, or column-based. These are designed to handle large-scale, high-performance scenarios. Eg: MongoDB, Redis DB, Neo4j, ArangoDB etc. 


## Relational Database Management System
1. **Database**: A collection of related data stored in a structured format, typically organized into tables, indexes, views, and other objects.

2. **Table**: A structured set of data elements (rows and columns) organized in a grid format. Each column represents a specific attribute, while each row represents a unique record or entry.

3. **Column**: A vertical arrangement of data in a table, representing a specific attribute or field. Columns have a data type that defines the kind of data they can store (e.g., integer, string, date).

4. **Row**: A horizontal arrangement of data in a table, representing a single record or entry containing values corresponding to each column.

5. **Primary Key**: A column or a set of columns whose values uniquely identify each row in a table. It ensures data integrity and facilitates efficient data retrieval.

6. **Foreign Key**: A column or a set of columns in one table that references the primary key in another table. It establishes a relationship between the two tables, enforcing referential integrity.

7. **Index**: A data structure used to improve the speed of data retrieval operations on a table. It contains keys built from one or more columns, allowing for faster search and retrieval of data.

8. **Query**: A SQL statement used to retrieve, manipulate, or manage data in a database. Common types of queries include SELECT, INSERT, UPDATE, DELETE, and JOIN.

9. **View**: A virtual table generated from the result set of a SELECT query. Views allow users to query and manipulate data stored in multiple tables as if they were a single table.

10. **Constraint**: A rule or condition applied to data in a database to maintain data integrity and enforce business rules. Examples include primary key constraints, foreign key constraints, unique constraints, and check constraints.

11. **Normalization**: A process of organizing data in a database to reduce redundancy and dependency, thereby improving data integrity and minimizing data anomalies.

12. **Transaction**: A unit of work performed on a database, typically consisting of one or more SQL statements. Transactions ensure data consistency and integrity by either committing changes or rolling them back in case of errors.

13. **Stored Procedure**: A precompiled set of SQL statements stored in the database and executed as a single unit. Stored procedures can accept parameters, perform complex operations, and return results to the calling program.

14. **Trigger**: A database object that automatically executes a set of SQL statements in response to certain events, such as INSERT, UPDATE, or DELETE operations on a table.
