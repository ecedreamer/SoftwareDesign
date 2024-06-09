## Database
A database is a collection of interrelated data which helps in the efficient retrieval, insertion, and deletion of data from the database and organizes the data in the form of tables, views, schemas, reports, etc. For Example, a university database organizes the data about students, faculty, admin staff, etc. which helps in the efficient retrieval, insertion, and deletion of data from it.

#### Symbol of Database
<img src="../../Images/database/database_symbol.png" width="500">

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

A relational database is a type of database that stores and organizes data in a structured way, based on the relational model

1. **Database**: A collection of related data stored in a structured format, typically organized into tables, indexes, views, and other objects.

2. **Table or Relation**: A structured set of data elements (rows and columns) organized in a grid format. Each column represents a specific attribute, while each row represents a unique record or entry.

3. **Column or Attribute**: A vertical arrangement of data in a table, representing a specific attribute or field. Columns have a data type that defines the kind of data they can store (e.g., integer, string, date).

4. **Row or Tuple**: A horizontal arrangement of data in a table, representing a single record or entry containing values corresponding to each column.
   
5. **Relationship:** The magic of relational databases lies in how these tables relate to each other.  Tables can be linked together using keys (special columns). This allows you to efficiently retrieve and manage data across different entities.
   
6. **Structured Query Language (SQL):**  Relational databases are queried using SQL, a standardized language specifically designed to interact with relational databases. SQL allows you to insert, update, delete, and retrieve data from the database.
   
7. **Keys:**  Keys are crucial for establishing relationships between tables. There are different types of keys eg, candidate key, super key, primary key, composite key, foreign key, alternate key etc. 

