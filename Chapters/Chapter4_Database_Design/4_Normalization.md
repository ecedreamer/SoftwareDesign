## Database Normalization
Database normalization is a process of organizing data in a relational database to minimize redundancy and improve data integrity. It involves structuring your database into multiple tables with defined relationships between them. This approach offers several advantages:

**Reduced Data Redundancy:** By eliminating duplicate data entries, you save storage space and minimize the chance of inconsistencies arising from updates in multiple places.

**Improved Data Integrity:** Normalization ensures data remains accurate and consistent throughout the database. Updates made in one table are reflected wherever the data is referenced.

**Enhanced Data Efficiency:** Normalized databases allow for faster retrieval and manipulation of specific data sets.


## Dependencies
### Functional Dependency
Given a relation (table) R, an attribute A (or a set of attributes) is said to functionally determine another attribute B if, for every pair of tuples (rows) in R, whenever the values of A are the same, the values of B are also the same. This is denoted as A→B.

In other words, if two rows of a table have the same value for attribute A, then they must have the same value for attribute B.

**Example:** In a Customers table with attributes customer_id, customer_name, and city, the FD customer_id -> customer_name holds true. This means that knowing the customer_id uniquely determines the customer_name.

**Anomaly caused by Functional Dependency:**

**Update Anomaly:** If the FD is not enforced, updating a value in the determinant (e.g., customer_id) might require updating the dependent attribute (e.g., customer_name) in multiple rows if it's duplicated elsewhere. This can lead to inconsistencies if the update is missed in some rows.

### Partial Dependency
A partial dependency (PD) is a special case of a functional dependency. It occurs when a determinant is only a part of the candidate key (all attributes that uniquely identify a row). In simpler terms, a non-key attribute depends on only a part of the key.

**Example:** Consider a Students table with attributes student_id, class_id, and major. If the only candidate key is student_id, then a PD might exist like class_id -> major. Here, major depends on class_id, but class_id is not the entire candidate key.

**Anomaly caused by Partial Dependency:**

**Insert Anomaly:** If a PD exists, you might insert a record with a valid value for the partial key (e.g., class_id) but a missing value for the dependent attribute (major). This violates data integrity as a complete picture of a student might be missing essential information.


### Transitive Dependency
A transitive dependency (TD) is an indirect dependency between attributes. It occurs when two FDs exist: X -> Y and Y -> Z. The transitive dependency then implies X -> Z, even though there's no direct FD between X and Z.

**Example:** Imagine a Courses table with attributes course_id, department_id, and instructor_id. If course_id -> department_id and department_id -> instructor_id hold true, then a TD exists: course_id -> instructor_id.

**Anomaly caused by Transitive Dependency:**

**Delete Anomaly:** If a TD exists, deleting a row based on the first determinant (e.g., course_id) might leave "orphaned" data in related tables. For instance, deleting a course might leave an instructor record without an associated course if the instructor information is only stored in the department table.

## Normal Forms
### First Normal Form (1NF):
Ensures all data items within a column are atomic (single value) and there are no repeating groups within a table.

### Second Normal Form (2NF):
Complies with 1NF and eliminates partial dependencies. This occurs in a table where there is a primary key composed of more than one key. 
A partial dependency occurs when a non-key attribute depends on only a part of the primary key.

### Third Normal Form (3NF)
Adheres to 2NF and removes transitive dependencies. This occurs when one non-key attribute depends on another non-key attribute, which in turn depends on the primary key.